function z = entropy(x)
% Compute entropy H(x) of a discrete variable x.
% Written by Mo Chen (mochen80@gmail.com).

% numel(A, IDX1, IDX2):Return the number of elements in the object A
n = numel(x);
% reshape():return a matrix shaped in specified dimension
x = reshape(x,1,n);
% [Y,I,J] = unique(X):return the unique elements of X,sorted in ascending order
% X(I) == y and y(J) == X
[u,~,label] = unique(x)
% sparse matrix representation: storing only NONZERO elements,typically 
% in two dimension fashion.
% S = sparse (I, J, SV, M, N, NZMAX):
%   I and J: integer index vectors,
%   SV: a 1-by-'nnz' vector of real complex values 
%   M and N:overall dimension of the sparse matrix
%   construct sparse matrix :
%   S(I(K),J(K)) = SV(K) or SV if SV is scalar
%   with overall dimensions M,N.

% mean(X,DIM,OPT):
%   compute the mean of the elements of the vector X along DIM dimension
p = full(mean(sparse(1:n,label,1,n,numel(u),n),1));
% dot(X, Y, DIM):Compute the dot product of two vectors
z = -dot(p,log2(p+eps));
