% demo
% x = rand(10,1000);
% [model, energy] = dimPcaVb(x);
d = 3;
n = 100;

k = 4;

A = normalize(rand(k,k),2);
E = normalize(rand(k,d),2);
s = normalize(rand(k,1),1);

z = zeros(n,1);
x = zeros(n,1);
% randomly sample a latent variable
z(1) = discreternd(s);
% randomly sample from emission distribution given the hidden variable
x(1) = discreternd(E(z(1),:));
for i = 2:n
    z(i) = discreternd(A(z(i-1),:));
    x(i) = discreternd(E(z(i),:));
end

scatter(1:n,x);

[model, energy] = hmmEm(x,k)
[z,p] = hmmDecode(x,model.s,model.A,model.E);
disp(p);
