function [label, model, L] = mixGaussVb(X, init, prior)
% Perform variational Bayesian inference for Gaussian mixture.
%   X: n x d data matrix
%   init: k (1 x 1) or label (1 x n, 1<=label(i)<=k) or center (d x k)
%
%   label: n*k clustering lables
%   model: model parameters
%   L: variational lower bound
%
% Reference: Pattern Recognition and Wachine Learning by Christopher W. Bishop (P.474)
% Written by Wichael Chen (sth4nth@gmail.com).
% Modified by onerhao@gmail.com.

fprintf('Variational Bayesian Gaussian mixture: running ... \n');
[n,d] = size(X);
[model.R,k] = initialization(X,init);
if nargin < 3
    prior.alpha = 1; % Dirichlet hyper prior parameter
    prior.beta = 1;  % Gaussian
    prior.m = mean(X,1)'; % Gaussian mean
    prior.nu = d+1;  % Wishart
    prior.W = eye(d);   % Wishart,%W != inv(W)
end
tol = 1e-13;
maxiter = 5000;
L = -inf(1,maxiter);
label = zeros(n,1);
converged = false;
iter = 0;

while  ~converged && iter < maxiter
    iter = iter+1;
    model = vmax(X, model, prior);
    model = vexp(X, model);
    L(iter) = vbound(X,model,prior)/n;
    if iter > 1
        converged = abs(L(iter)-L(iter-1)) <= tol*abs(L(iter));
        if  L(iter)<L(iter-1) 
            %fprintf('Lower bound decreased by %f ,threshold: %f\n', ...
                %abs(L(iter-1)-L(iter)),...
                %tol*abs(L(iter)));
        end
    end
    [~,label(:)] = max(model.R,[],2);
    %[~,~,label] = unique(label);
    %spread(X',label');
end

L = L(1:iter);
if converged
    fprintf('Converged in %d steps.\n',iter);
else
    fprintf('Not converged in %d steps.\n',maxiter);
end

function [R,k] = initialization(X, init)
[n,d] = size(X);
if length(init) == 1  % random initialization
    k = init;
    idx = randsample(n,k);
    m = X(idx,:);
    % k-means initialization
    [~,label] = max(bsxfun(@minus,X*m',dot(m',m',1)/2),[],2); % assign samples to the nearest centers
    [u,~,label] = unique(label);
    while k ~= length(u)
        idx = randsample(n,k);
        %m = X(:,idx);
        m = X(idx,:);
        [~,label] = max(bsxfun(@minus,X*m',dot(m',m',1)/2),[],2); % assign samples to the nearest centers
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
    %[~,label] = max(bsxfun(@minus,m'*X,dot(m,m,1)'/2),[],1);
    [~,label] = max(bsxfun(@minus,X*m',dot(m',m',1)/2),[],2); % assign samples to the nearest centers
    R = full(sparse(1:n,label,1,n,k,n));
else
    error('ERROR: init is not valid.');
end

% variational Maximization step
function model = vmax(X, model, prior)
alpha0 = prior.alpha;
beta0 = prior.beta;
m0 = prior.m;
nu0 = prior.nu;
W0 = prior.W;
R = model.R;

% k x 1, add a non-zero term for the components with zero responsibilities
nk = sum(R,1)' + 1e-20; % 10.51
alpha = alpha0+nk; % 10.58
% k x d mean vector
nxbar = R'*X;
% k x 1
beta = beta0+nk; % 10.60
% beta0 the prior beta  k x 1 vector,m0: the prior mean d x 1 vector
m = bsxfun(@times,bsxfun(@plus,beta0*m0',nxbar),1./beta); % 10.61
nu = nu0+nk; % 10.63

[k,d] = size(m);
W = zeros(d,d,k);
sqrtR = sqrt(R);

% k x d
xbar = bsxfun(@times,nxbar,1./nk); % 10.52
% k x d
xbarm0 = bsxfun(@minus,xbar,m0');
w = (beta0*nk./(beta0+nk));
for i = 1:k
    Xxbar = bsxfun(@minus,X,xbar(i,:));
    Xs = bsxfun(@times,bsxfun(@minus,X,xbar(i,:)),sqrtR(:,i));
    xbarm0i = xbarm0(i,:);
    W(:,:,i) = inv(W0+Xs'*Xs+w(i)*(xbarm0i*xbarm0i')); % 10.62
end

model.alpha = alpha;
model.beta = beta;
model.m = m;
model.nu = nu;
model.W = W; % Whishart: W = inv(W)

% variational Expectation step
function model = vexp(X, model)
alpha = model.alpha; % Dirichlet, k x 1
beta = model.beta;   % Gaussian,  k x 1
m = model.m;         % Gaussian,  k x d
nu = model.nu;         % Whishart,k x 1
W = model.W;         % Whishart: d x d x k.In the previous implementation,inv(W) = V'*V

n = size(X,1);
[k,d] = size(m);

logW = zeros(k,1);
% expectation of the quadratic term
EQ = zeros(n,k);
for i = 1:k
    U = chol(W(:,:,i));
    logW(i) = 2*sum(log(diag(U)));
    % ???
    %Q = (U'\bsxfun(@minus,X,m(:,i)));
    Q = bsxfun(@minus,X,m(i,:))*U;
    %EQ(:,i) = d/beta(i)+nu(i)*dot(Q,Q,1);    % 10.64
    EQ(:,i) = d/beta(i)+nu(i)*dot(Q,Q,2);    % 10.64
end

ElogLambda = sum(psi(bsxfun(@minus,nu+1,(1:d))/2),2)+d*log(2)+logW; % 10.65
Elogpi = psi(alpha)-psi(sum(alpha)); % 10.66

logRho = (bsxfun(@minus,EQ,(2*Elogpi+ElogLambda-d*log(2*pi))'))/(-2); % 10.46
logR = bsxfun(@minus,logRho,logsumexp(logRho,2)); % 10.49
R = exp(logR);

model.logR = logR;
model.R = R;
%[~,model.label] = max(model.R,[],2);

% variational lower bound
function L = vbound(X, model, prior)
alpha0 = prior.alpha;
beta0 = prior.beta;
m0 = prior.m;
nu0 = prior.nu;
W0 = prior.W;

alpha = model.alpha; % Dirichlet
beta = model.beta;   % Gaussian
m = model.m;         % Gaussian
nu = model.nu;         % Whishart
W = model.W;         % Whishart: inv(W) = V'*V
R = model.R;
logR = model.logR;


[k,d] = size(m);
nk = sum(R,1)' + 1e-20; % 10.51

U0 = chol(W0);
sqrtR = sqrt(R);
xbar = bsxfun(@times,R'*X,1./nk); % 10.52

S = zeros(d,d,k);
logW = zeros(k,1);
trSW = zeros(k,1);
trW0W = zeros(k,1);
xbarmWxbarm = zeros(k,1);
mm0Wmm0 = zeros(k,1);
for i = 1:k
    % compute trace of product of matrices ??
    %U = chol(W(:,:,i));
    %logW(i) = -2*sum(log(diag(U)));      
    
    %Xs = bsxfun(@times,bsxfun(@minus,X,xbar(:,i)),sqrtR(:,i));
    %V = chol(Xs'*Xs/nk(i));
    %Q = V/U;
    %trSW(i) = dot(Q(:),Q(:));  % equivalent to tr(SW)=trace(S/W)
    %Q = U0/U;
    %trW0W(i) = dot(Q(:),Q(:));

    %q = U'\(xbar(:,i)-m(:,i));
    %xbarmWxbarm(i) = dot(q,q);
    %q = U'\(m(:,i)-m0);
    %mm0Wmm0(i) = dot(q,q);

    U = chol(W(:,:,i));
    logW(i) = 2*sum(log(diag(U)));
    diff = xbar(i,:)-m(i,:);
    xbarmWxbarm(i) = diff*W(:,:,i)*diff';% (10.71)

    mdiff = m(i,:)' - m0;
    mm0Wmm0 = mdiff'*W(:,:,i)*mdiff;

    Xs  = bsxfun(@times,bsxfun(@minus,X,xbar(i,:)),sqrtR(:,i));
    S(:,:,i) = Xs'*Xs./nk(i);
    trSW(i) = trace(S(:,:,i)*W(:,:,i));
    trW0W(i) = trace(inv(W0)*W(:,:,k));
end

%ElogLambda = sum(psi(bsxfun(@minus,nu+1,(1:d)')/2),1)+d*log(2)+logW; % 10.65
ElogLambda = sum(psi(bsxfun(@minus,nu+1,(1:d))/2),2)+d*log(2)+logW; % 10.65

Elogpi = psi(alpha)-psi(sum(alpha)); %(10.66)

EpX = 0.5*dot(nk,ElogLambda-d./beta-nu.*trSW-nu.*xbarmWxbarm-d*log(2*pi));%(10.71)
Epz = dot(nk,Elogpi); %(10.72)
Eqz = dot(R(:),logR(:));%(10.75)
logCalpha0 = gammaln(k*alpha0)-k*gammaln(alpha0); %(B.23)
Eppi = logCalpha0+(alpha0-1)*sum(Elogpi);%(10.73)
logCalpha = gammaln(sum(alpha))-sum(gammaln(alpha));%(B.23)
Eqpi = dot(alpha-1,Elogpi)+logCalpha;%(10.76)

Epmu = sum(d*log(beta0/(2*pi))+ElogLambda-d*beta0./beta-beta0*(nu.*mm0Wmm0))/2;
logB0 = nu0*sum(log(diag(U0)))-0.5*nu0*d*log(2)-logmvgamma(0.5*nu0,d);
EpLambda = k*logB0+0.5*(nu0-d-1)*sum(ElogLambda)-0.5*dot(nu,trW0W);

Eqmu = 0.5*sum(ElogLambda+d*log(beta/(2*pi)))-0.5*d*k;
logB =  -nu.*(logW+d*log(2))/2-logmvgamma(0.5*nu,d);
EqLambda = 0.5*sum((nu-d-1).*ElogLambda-nu*d)+sum(logB);


L = EpX+Epz-Eqz+Eppi-Eqpi+Epmu-Eqmu+EpLambda-EqLambda;
