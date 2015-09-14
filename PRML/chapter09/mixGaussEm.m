function [label, model, llh] = mixGaussEm(X, init)
% Perform EM algorithm for fitting the Gaussian mixture model.
%   X: n x d data matrix
%   init: k (1 x 1) or label (n x 1, 1<=label(i)<=k) or center (k x d)
%   @label:class labels(latent variables)
%   @model.mu:k-by-d mean matrix
%   @model.Sigma: d-by-d-by-k covariance matrix
%   @model.pik:k-by-1 mixing coefficients
% Written by Michael Chen (sth4nth@gmail.com),onerhao@gmail.com.

%% initialization
fprintf('EM for Gaussian mixture: running ... \n');
R = initialization(X,init);
[~,label(:,1)] = max(R,[],2);
R = R(:,unique(label));

tol = 1e-10;
maxiter = 1000;
llh = -inf(1,maxiter);
converged = false;
t = 1;
while ~converged && t < maxiter
    t = t+1;
    model = maximization(X,R);
    [R, llh(t)] = expectation(X,model);
   
    [~,label(:)] = max(R,[],2);
    u = unique(label);   % non-empty components
    if size(R,2) ~= size(u,1)
        R = R(:,u);   % remove empty components
    else
        converged = llh(t)-llh(t-1) < tol*abs(llh(t-1));
    end

end
llh = llh(2:t);
if converged
    fprintf('Converged in %d steps.\n',t-1);
else
    fprintf('Not converged in %d steps.\n',maxiter);
end

function R = initialization(X, init)
[n,d] = size(X);
if isstruct(init)  % initialize with a model
    R  = expectation(X,init);
elseif length(init) == 1  % random initialization
    k = init;
    idx = randsample(n,k);
    m = X(idx,:);
    [~,label] = max(bsxfun(@minus,X*m',dot(m,m,2)'/2),[],2);
    [u,~,label] = unique(label);
    while k ~= length(u)
        idx = randsample(n,k);
        m = X(idx,:);
        [~,label] = max(bsxfun(@minus,X*m',dot(m,m,2)'/2),[],2);
        [u,~,label] = unique(label);
    end
    R = full(sparse(1:n,label,1,n,k,n));
elseif size(init,1) == 1 && size(init,2) == n  % initialize with labels
    label = init;
    k = max(label);
    R = full(sparse(1:n,label,1,n,k,n));
elseif size(init,1) == d  %initialize with only centers
    k = size(init,2);
    m = init;
    [~,label] = max(bsxfun(@minus,m'*X,dot(m,m,1)'/2),[],1);
    R = full(sparse(1:n,label,1,n,k,n));
else
    error('ERROR: init is not valid.');
end

function [R, llh] = expectation(X, model)
% expectation step:
% soft assignment LATENT VARIABLES by
% computing posterior probabilities(responsibilities) of latent variables,
% with respect to MODEL PARAMETERS
mu = model.mu;
Sigma = model.Sigma;
% mixing coefficients
w = model.pik;

n = size(X,1);
k = size(mu,1);
logRho = zeros(n,k);

for i = 1:k
    % n-by-k log likelihood matrix
    logRho(:,i) = loggausspdf(X,mu(i,:),Sigma(:,:,i));
end
% log complete-data probability
logRho = bsxfun(@plus,logRho,log(w'));
% n-by-1 log denominator matrix in equation (9.23)
T = logsumexp(logRho,2);
llh = sum(T)/n; % loglikelihood
% (9.23)
logR = bsxfun(@minus,logRho,T);
R = exp(logR);


function model = maximization(X, R)
% maximization step: re-estimate model parameters.
% optimize(maximize) the expectation of log joint likelihood of
% OBSERVED VARIABLES AND LATENT VARIABLES(complete-data log likelihood)
% or observed data log-likelihood
% with respect to latent variables and model parameters
% @R: n-by-k responsibility(posterior) matrix
[n,d] = size(X);
k = size(R,2);

nk = sum(R,1)';
% mixing coefficients.
w = nk/n;
% (9.24)
mu = bsxfun(@times, R'*X, 1./nk);

Sigma = zeros(d,d,k);
sqrtR = sqrt(R);
for i = 1:k
    Xo = bsxfun(@minus,X,mu(i,:));
    Xo = bsxfun(@times,Xo,sqrtR(:,i));
    % (9.25):compute covariance
    Sigma(:,:,i) = Xo'*Xo/nk(i);
    Sigma(:,:,i) = Sigma(:,:,i)+eye(d)*(1e-6); % add a prior for numerical stability
end

model.mu = mu;
model.Sigma = Sigma;
model.pik = w;

function y = loggausspdf(X, mu, Sigma)
% log gaussian probability density function
% @X: input data 1-by-d vector/ n-by-d matrix
d = size(X,2);
X = bsxfun(@minus,X,mu);
% chol(): Cholesky decomposition of symmetric real matrix
% U'*U = Sigma
[U,p]= chol(Sigma);
if p ~= 0
    error('ERROR: Sigma is not PD.');
end
% Q = inv(U')*X;
% cov(X) = X'*X;
Q = U'\X';
q = dot(Q,Q,1);  % quadratic term (M distance)
% determinant of triangle matrix is the product of elements on diagonal
c = d*log(2*pi)+2*sum(log(diag(U)));   % normalization constant
y = -(c+q)/2;
