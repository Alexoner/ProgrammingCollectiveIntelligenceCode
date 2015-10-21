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

% demo variational bayesian gaussian mixture model with old faithful dataset
%read data
fprintf('Demonstrating variational bayesian gaussian mixture model with old faithful dataset');
fd = fopen('../data/faithful.txt','r');
X = fscanf(fd,'%f',[2,272]);
fclose(fd);
train_data = X;
%standardize the data
train_data = train_data - repmat(mean(train_data,2),1,size(train_data,2));
train_data = train_data./repmat(var(train_data,[],2),1,size(train_data,2));
[dim N] = size(train_data)
fflush(stdout);
ncentres = 15;
[label,model,llh ] = mixGaussVb(train_data',ncentres);
figure;
spread(train_data,label');

pause;

% demo vb
fprintf('Demonstrating variational bayesian gaussian mixture model with GMM generated data');
k = 2;
n = 1000;
[X,t] = rndKCluster(2,k,n);
X = X';
t = t';
ncentres = 4;
[label,model,llh] = mixGaussVb(X,ncentres);
fprintf('Bayesian Gaussian Mixture Model,lower bound: %f\n',llh(end)/n);
plot(llh);
figure;
spread(X',t');
%spread(X,t);
%hold on;
figure;
%[~,label] = max(model.R,[],2);
spread(X',label);
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
