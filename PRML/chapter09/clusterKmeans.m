function [label,m] = clusterKmeans(X, k)
% Perform k-means clustering.
%   X: n x d data matrix
%   k: number of seeds or clusters
%   m: density parameters,k-by-d matrix
% Written by Michael Chen (sth4nth@gmail.com).
[n,d] = size(X);
tol = 1e-6;
maxiter = 100;
iter = 1;
last = ceil(k*rand(1,n)');  % random initialization of latent variables
label = ceil(k*rand(1,n)');  % random initialization of latent variables
m = initkm(X,k);
%while any(label ~= last)
while iter < maxiter && any(label ~= last)
    %[u,~,label] = unique(label);   % remove empty clusters
    %k = length(u);
    last = label;
    [~,label] = max(bsxfun(@minus,X*m',dot(m',m',1)/2),[],2); % assign samples to the nearest centers
    E = sparse(1:n,label,1,n,k,n); % transform label into n-by-k indicator(latent variable) matrix
    m = (E*spdiags(1./sum(E,1)',0,k,k))'*X;    % compute m of each cluster
    iter = iter + 1
    if dot(last,label,1) < tol,
        disp(last)
        disp(label)
        break;
    end
end
[~,~,label] = unique(label);


function center = initkm(data,cluster_n) 
% INITKM Find the initial centers for a K-means clustering algorithm.  
 
% Roger Jang, 990831 
% ===== Method 0: Randomly pick rows
    [n,d] = size(data);
    center = ones(cluster_n,d);
    perm = randperm(n);
    for i = 1: cluster_n,
        center(i,:) = data(perm(i),:);
    end
% ====== Method 1: Randomly pick cluster_n data points as cluster centers 
%class_n = max(data_class); 
%center = []; 
%center_class = []; 
%for i = 1:class_n, 
	%this_data = data(find(data_class==i), :); 
	%this_data_n = size(this_data, 1); 
	%tmp = randperm(this_data_n); 
	%index = tmp(1:cluster_n); 
	%center = [center; this_data(index, :)]; 
	%center_class = [center_class; i*ones(cluster_n, 1)]; 
%end 
 
% ====== Method 2: Choose cluster_n data points closest to the mean vector 
%mean_vec = mean(data); 
%dist = distfcm(mean_vec, data); 
%[a,b] = sort(dist); 
%center = data(b(1:cluster_n), :); 
 
% ====== Method 3: Choose cluster_n data points furthest to the mean vector 
%mean_vec = mean(data); 
%dist = distfcm(mean_vec, data); 
%[a,b] = sort(dist); 
%b = fliplr(b); 
%center = data(b(1:cluster_n), :); 
