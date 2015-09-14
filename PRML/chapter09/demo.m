
% =======demonstrate kmeans algorithm

clear; close all;
k = 2;
n = 1000;
[X,t] = rndKCluster(2,k,n);
spread(X,t);
X = X';
t = t';

[label,m] = clusterKmeans(X,k);
%spread(m);
hold on;
%plot(m(1,:),m(2,:),'kd');
% scatter(X,Y,S,C):
% X:X coordinate;Y: Y coordinate;S:size;C:color
scatter(m(:,1),m(:,2),256,1:k);
hold off;
pause;


% =============demonstrate EM algorithm for Gaussian Mixture Models
clear; close all;
k = 2;
n = 1000;
[X,t] = rndKCluster(2,k,n);
[label,model,llh] = mixGaussEm(X,2);
plot(llh);
figure;
spread(X,t);
hold on;
scatter(model.mu(1,:),model.mu(2,:),256,1:k);
hold off;
