function x = mh_gaussian(n,mu,sigma)
%n = 25000;
if nargin < 3
    mu = 1;
    sigma = 1;
end

x = zeros(n, 1);
x(1) = 0.5;
for i = 1: n-1
    x_c = normrnd(x(1), 0.05);
    if rand < min(1, normpdf(x_c,mu,sigma)/normpdf(x(i),mu,sigma))
        x(i+1) = x_c;
    else
        x(i+1) = x(i);
    end
end
