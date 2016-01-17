function [model, energy] = hmmEm(x, k, A, E, s)
% EM algorithm to fit the parameters of HMM model (a.k.a Baum-Welch algorithm)
% with discrete emission probability of latent variables
% x: 1 x n sequence of observations
% A: k x k transition matrix
% E: k x d emission matrix
% s: k x 1 initial probability
%
% model: model parameters
% energy: log likelihood function,evaluated with normalization quantity c


n = size(x,1);
d = max(x);
% sparse representation of design matrix in 1-of-K encoding schema,
% dimension: n * d
X = sparse(1:n,x,1,n,d);

if nargin < 3
    A = normalize(rand(k,k),2);
    E = normalize(rand(k,d),2);
    s = normalize(rand(k,1),1);
end

%probability given the latent variable, p(\vec{x}_n|\vec{z}n), n x k
M = X*E';

tol = 1e-4;
maxIter = 500;
energy = -inf(1,maxIter);
for iter = 2:maxIter
%     E-step
    [gamma,alpha,beta,c] = hmmSmoother(M,A,s);
    energy(iter) = sum(log(c(c>0)));
    if energy(iter)-energy(iter-1) < tol*abs(energy(iter-1)); break; end   % check likelihood for convergence
%     M-step
    % xi is the joint marginal posterior of z_{n-1} and z_n
    xi = A.*(alpha(1:n-1,:)'*bsxfun(@times,beta(2:n,:).*M(2:n,:),1./c(2:end)));
    A = normalize(xi,2);
    %A = normalize(A.*(alpha(1:n-1,:)'*bsxfun(@times,beta(2:n,:).*M(2:n,:),1./c(2:end))),2);
    [s,~] = normalize(gamma(1,:),2); % normalization?
    s = s';
    % update emission probabilities
    E = bsxfun(@times,gamma'*X,1./sum(gamma',2));
    M = X*E';
end
energy = energy(2:iter);
model.A = A;
model.E = E;
model.s = s;


