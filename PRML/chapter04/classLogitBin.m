function [model, llh] = classLogitBin(X, t, lambda)
% logistic regression for binary classification (Bernoulli likelihood)
% Newton-Raphson iterative reweighted optimization scheme to solve the
% optimization problem
%if any(unique(t) ~= [0,1])
if unique(t) ~= [0,1]
    error('t must be a 0/1 vector!');
end
if nargin < 3
    lambda = 1e-4;
end
[n,d] = size(X);
dg = sub2ind([d,d],1:d,1:d);
%X = [X; ones(1,n)];
X = [ones(n,1),X];
d = d+1;

tol = 1e-4;
% maximum iteration number
maxiter = 100;
% log-likelihood function
llh = -inf(1,maxiter);
converged = false;
% iteration pass index
iter = 1;


h = ones(n,1);
h(t==0) = -1;
w = zeros(d,1);
z = X*w;
while ~converged && iter < maxiter
    iter = iter + 1;
    y = sigmoid(z);
    
    g = X'*(y-t)+lambda*w;
    r = y.*(1-y);
    R = spdiags(r(:),0,n,n);    
    H = X'*R*X;
    H(dg) = H(dg)+lambda;
    
    p = -H\g;

    wo = w;
    w = wo+p;
    z = X*w;   
    llh(iter) = -sum(log1pexp(-h.*z))-0.5*lambda*dot(w,w);
    converged = norm(p) < tol || abs(llh(iter)-llh(iter-1)) < tol;
    while ~converged && llh(iter) < llh(iter-1)
        p = 0.5*p;
        w = wo+p;
        z = X*w;    
        llh(iter) = -sum(log1pexp(-h.*z))-0.5*lambda*dot(w,w);
        converged = norm(p) < tol || abs(llh(iter)-llh(iter-1)) < tol;
    end
end
llh = llh(2:iter);
model.w = w;
