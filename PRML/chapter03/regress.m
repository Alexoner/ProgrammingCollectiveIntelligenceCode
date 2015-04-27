function model = regress(X, t, lambda)
% Fit linear regression model t=w'x+b
% X: n x d data
% t: n x 1 response
if nargin < 3
    lambda = 0;
end

% dimension of x
d = size(X,2);
xbar = mean(X,1);
tbar = mean(t,1);

% subtract by mean to normalize the data
X = bsxfun(@minus,X,xbar);
t = bsxfun(@minus,t,tbar);

% covariance matrix
S = X'*X;
% sub2ind:convert subscripts to a linear index
dg = sub2ind([d,d],1:d,1:d);
% add regularization quantity,lambda*I.(3.28)
S(dg) = S(dg)+lambda;
% w = S\(X*t');
R = chol(S);

% X\Y = mldivide(X,Y): matrix left divide
% solve linear equation Ax=B for x = A\B
% w = R\(R'\(X*t'));  % 3.15 & 3.28
 w = inv(X'*X)*X'*t
%w = X'\(X\(X*t'));
b = tbar-dot(w,xbar);  % 3.19

model.w = w;
model.b = b;
