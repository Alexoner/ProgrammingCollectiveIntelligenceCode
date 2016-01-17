function [z,p] = hmmDecode(x,s,A,E)
% Viterbi algorithm in https://en.wikipedia.org/wiki/Viterbi_algorithm#Example
% x: n-by-1 observation vector
% s: initial prior probability of latent variables
% A: transmission probability matrix
% E: emission probability matrix
n = length(x);
k = length(A);
Z = zeros(n,k);
s = log(s)
A = log(A)
E = log(E)
% tracking path giving rise to maximum joint probability
Z = zeros(n,k);
% messages from factor node to variable node
w = zeros(n,k);
Z(1,:) = 1:k;
w(1,:) = s(1)' + E(:,x(1))';
for t = 2 : n,
    % idx: z_{t} that maximizes the message
    [v,idx] = max(bsxfun(@plus,A,w(t-1,:)),[],1);
    w(t,:) = E(:,x(t))'+ v;
    % rearrange the path matrix,so that each column of Z matrix corresponds to
    % a path(sequence) that maximize the joint probability of previous nodes
    %, known as message passed out, with current(the tth) latent variable's state 
    % as the row index
    Z = Z(:,idx);
    % current latent variable's states,used in next pass
    Z(t,:) = 1:k;
end
[v,idx] = max(w(n,:),[],2);
% maximum joint probability
p = exp(v);
z = Z(:,idx);
