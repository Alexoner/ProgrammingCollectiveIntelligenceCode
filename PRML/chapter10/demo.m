clear; close all;

%% regression
% n = 100;
% beta = 1e-1;
% X = rand(1,n);
% w = randn;
% b = randn;
% t = w'*X+b+beta*randn(1,n);
% 
% x = linspace(min(X)-1,max(X)+1,n);   % test data

%k = 2;
%n = 1000;
%[X,t] = rndKCluster(2,k,n);
%%X = X';
%%t = t';
%[label,model,llh] = vbgm(X,4);
%plot(llh);
%figure;
%%spread(X',t');
%spread(X,t);
%hold on;
%figure;
%[~,label] = max(model.R,[],2);
%spread(X,label');
%pause;
%%scatter(model.m(:,1),model.m(:,2),256,1:k);
%hold off;
%pause;


k = 2;
n = 1000;
[X,t] = rndKCluster(2,k,n);
X = X';
t = t';
[label,model,llh] = mixGaussVb(X,4);
fprintf('Bayesian Gaussian Mixture Model,lower bound: %f\n',llh(end)/n);
plot(llh);
figure;
spread(X',t');
%spread(X,t);
%hold on;
figure;
[~,label] = max(model.R,[],2);
spread(X',label');
pause;
%scatter(model.m(:,1),model.m(:,2),256,1:k);
%hold off;
pause;

X = rand(3,100);
t = rand(1,100);
%%
% [model,energy] = regressVb(X,t);
% % figure
% plot(energy);
% y = linInfer(x,model);
% figure;
% hold on;
% % plotBand(x,y,2*sigma);
% plot(X,t,'o');
% plot(x,y,'r-');
% hold off

%%
%[model,energy] = regressVb(X,t);
% figure
%x = linspace(min(X)-1,max(X)+1,t);   % test data
%plot(energy);
%y = linInfer(x,model);
%figure;
%hold on;
% plotBand(x,y,2*sigma);
%plot(X,t,'o');
%plot(x,y,'r-');
%hold off
