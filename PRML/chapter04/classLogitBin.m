function [model, llh] = classLogitBin(X, t, lambda)
% logistic regression for binary classification (Bernoulli likelihood)
% Newton-Raphson iterative reweighted optimization scheme to solve the
% optimization problem
% @X: input n*d design matrix
% @t: n*1 response
% @lambda: regularization coefficient
% @model:
% @llh: log-likelihood function

% any(): return true if any element of the vector is non-zero
if any(unique(t) ~= [0;1])
    disp(unique(t));
    error('t must be a 0/1 vector!');
end
if nargin < 3
    lambda = 1e-4;
end
[n,d] = size(X)
% sub2ind: subscripts to linear index.Get diagonal indices
dg = sub2ind([d,d],1:d,1:d);
%X = [X; ones(1,n)];
X = [ones(n,1),X];
d = d+1;

% difference tolerance
tol = 1e-4;
% maximum iteration number
maxiter = 100;
% log-likelihood function
% inf(N,M):scalar,matrix whose elements are infinity
llh = -inf(1,maxiter);
converged = false;
% iteration pass index
iter = 1;


h = ones(n,1);
h(t==0) = -1;
w = zeros(d,1);
a = X*w;
while ~converged && iter < maxiter
    iter = iter + 1;
    y = sigmoid(a);
    
    gradient = X'*(y-t)+lambda*w;
    r = y.*(1-y);
    % equation (4.98)
    R = spdiags(r(:),0,n,n);    
    Hessian = X'*R*X;
    Hessian(dg) = Hessian(dg)+lambda;
    
    % equation (4.92):Newton-Raphson iterative
    p = -Hessian\gradient;

    wo = w;
    w = wo+p;
    a = X*w;   
    % regularized (posterior) optimization
    llh(iter) = -sum(log1pexp(-h.*a))-0.5*lambda*dot(w,w);
    converged = norm(p) < tol || abs(llh(iter)-llh(iter-1)) < tol;
    % in case the descent iteration diverge
    while ~converged && llh(iter) < llh(iter-1)
        p = 0.5*p;
        w = wo+p;
        a = X*w;    
        llh(iter) = -sum(log1pexp(-h.*a))-0.5*lambda*dot(w,w);
        converged = norm(p) < tol || abs(llh(iter)-llh(iter-1)) < tol;
    end
end
llh = llh(2:iter);
model.w = w;
