function [model, llh] = regressEbFp(X, t, alpha, beta)
% Fit empirical Bayesian linear model with Mackay fixed point method
% X: d x n data
% t: 1 x n response
if nargin < 3
    alpha = 0.02;
    beta = 0.5;
end
[n,d] = size(X);
X = [ones(n,1) X];
d = d + 1;

xbar = mean(X,1);
tbar = mean(t,1);

%X = bsxfun(@minus,X,xbar);
%t = bsxfun(@minus,t,tbar);

C = X'*X;
Xt = X'*t;
dg = sub2ind([d,d],1:d,1:d);
I = eye(d);
tol = 1e-4;
maxiter = 100;
% initialize likelihood function
llh = -inf(1,maxiter+1);
for iter = 2:maxiter
    % Hessian matrix (3.81)
    A = beta*C;
    A(dg) = A(dg)+alpha;
    % U'*U = A
    U = chol(A);
    % V*V' = A^{-1}=SN
    V = U\I;

    % (3.84)
    w = beta*(V*(V'*Xt));
    % L2 regularization
    w2 = dot(w,w);
    % sum of squares error
    err = sum((t-X*w).^2);
    % log|A|
    logdetA = 2*sum(log(diag(U)));
    % evidence approximation: log of the marginal likelihood (3.86)
    llh(iter) = 0.5*(d*log(alpha)+n*log(beta)-alpha*w2-beta*err-logdetA-n*log(2*pi));
    if llh(iter)-llh(iter-1) < tol*abs(llh(iter-1)); break; end
    
    % trace of S equals sum of eigenvalues and
    % make use of trace of product property
    trS = dot(V(:),V(:));
    gamma = d-alpha*trS;
    % (3.92)
    alpha = gamma/w2;
    % (3.95)
    beta = (n-gamma)/err;
end
b = tbar-dot(w,xbar);

llh = llh(2:iter);
model.b = b;
model.w = w;
model.alpha = alpha;
model.beta = beta;
model.xbar = xbar;
model.V = V;
