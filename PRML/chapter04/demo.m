% TODO: contour for multiclass


clear; close all;
k = 2;
n = 1000;
[X,t] = rndKCluster(2,k,n);
X = X';
t = t';

% linspace (BASE, LIMIT, N):
% Return a row vector with N linearly spaced elements between BASE and LIMIT.
% meshgrid():
%   Given vectors of X and Y coordinates, return matrices XX and YY corresponding to a full 2-D grid
%   XX: copies of rows from X, as one dimension's coordinate;
%   YY: copies of columns from Y,another dimension's coordinate
[x1,x2] = meshgrid(linspace(min(X(:,1)),max(X(:,1)),n), linspace(min(X(:,2)),max(X(:,2)),n));
[model, llh] = classLogitBin(X,t-1);
plot(llh);
figure;
spread(X',t');

w = model.w;
%y = w(1)*x1+w(2)*x2+w(3);
y = w(2)*x1+w(3)*x2+w(1);

hold on;
pause;
% plot 1 contour of y,given coordinates composed of x1 and x2
contour(x1,x2,y,1);
hold off;
%%
% clear; close all;
% k = 3;
% n = 1000;
% [X,t] = rndKCluster(2,k,n);
% 
% [x1,x2] = meshgrid(linspace(min(X(1,:)),max(X(1,:)),n), linspace(min(X(2,:)),max(X(2,:)),n));
% [model, llh] = classLogitMul(X,t);
% plot(llh);
% figure;
% spread(X,t);
% 
% W = model.W;
% % y = w(1)*x1+w(2)*x2+w(3);
% 
% hold on;
% contour(x1,x2,y,1);
% hold off;
