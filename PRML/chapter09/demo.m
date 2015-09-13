

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
scatter(m(:,1),m(:,2),256,1:k);
hold off;
