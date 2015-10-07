function [gamma, alpha, beta, c] = hmmSmoother(M, A, s)
% HMM smoothing alogrithm (normalized forward-backward a.k.a normalized alpha-beta algorithm)
% for discrete emission distribution
% M: p(x_n|z_n) matrix,n x k
% A: transition matrix,kxk
% s: initial state probability
%
% alpha:normalized quantity in recursion,nxk matrix
% beta: normalized quantity in recursion,n*k matrix
% gamma:responsibility,a.k.a posterior probability of latent variables,n*k matrix

[T,K] = size(M);
At = A';
c = zeros(T,1); % normalization constant
alpha = zeros(T,K);
% normalized pi_k*p(x_1|\phi_k)
[alpha(1,:),c(1)] = normalize(s'.*M(1,:),2);
for t = 2:T
    [alpha(t,:),c(t)] = normalize((alpha(t-1,:)*At).*M(t,:),2);
end
beta = ones(T,K);
for t = T-1:-1:1
    beta(t,:) = (beta(t+1,:).*M(t+1,:))*A'/c(t+1);
end
gamma = alpha.*beta;

