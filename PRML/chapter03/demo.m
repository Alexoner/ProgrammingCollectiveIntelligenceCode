% Done
% demo for chapter 03
clear; close all;
n = 100;
beta = 1e-1;
X = rand(n,1);
w = randn;
b = randn;
t = X*w+b+beta*randn(n,1);

x = linspace(min(X)-1,max(X)+1,n)';   % test data
%%
model = regress(X, t);
y = linInfer(x, model);
figure;
hold on;
plot(X,t,'o');
plot(x,y,'r-');
hold off
%
[model,llh] = regressEbFp(X,t);
[y, sigma] = linInfer(x,model,t);
figure;
hold on;
%plotBand(x,y,2*sigma);
plot(X,t,'o');
plot(x,y,'r-');
hold off
%figure
%plot(llh);
%
[model,llh] = regressEbEm(X,t);
[y, sigma] = linInfer(x,model,t);
figure;
hold on;
%plotBand(x,y,2*sigma);
plot(X,t,'o');
plot(x,y,'r-');
hold off
%figure;
%plot(llh);
