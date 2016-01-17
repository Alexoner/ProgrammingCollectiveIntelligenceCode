% TODO: contour for multiclass


clear; close all;
k = 2;
n = 1000;
[X,t] = rndKCluster(2,k,n);
% convert design matrix to n-by-d,target vector to n-by-1
X = X';
t = t';

% linspace (BASE, LIMIT, N):
% Return a row vector with N linearly spaced elements between BASE and LIMIT.
% meshgrid():
%   Given vectors of X and Y coordinates, return matrices XX and YY corresponding to a full 2-D grid
%   XX: copies of rows from X, as one dimension's coordinate;
%   YY: copies of columns from Y,another dimension's coordinate
[x1,x2] = meshgrid(linspace(min(X(:,1)),max(X(:,1)),n), linspace(min(X(:,2)),max(X(:,2)),n));
[model, llh] = classLogitBin(X,t-1,1e-1);
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

pause;
%%%%% multiple-class logistic regression
clear; close all;
k = 3;
n = 1000;
[X,t] = rndKCluster(2,k,n);
X = X';
t = t';

[x1,x2] = meshgrid(linspace(min(X(:,1)),max(X(:,1)),n), linspace(min(X(:,2)),max(X(:,2)),n));
[model, llh] = classLogitMul(X,t,1e-3,2);
plot(llh);
figure;
spread(X',t');

W = model.W;
%y = W(1)*x1+W(2)*x2+W(3);
y = W(1) + W(2)*x1 + W(3)*x2;

hold on;
contour(x1,x2,y,2);
hold off;
