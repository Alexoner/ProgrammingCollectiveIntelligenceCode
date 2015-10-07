function x = discreternd(p, n)
% Sampling from a discrete distribution (multinomial).
% Written by Michael Chen (sth4nth@gmail.com).
if nargin == 1
    n = 1;
end
r = rand(1,n);
% cumulative sum
p = cumsum(p(:));
% x = sum(repmat(r,length(p),1) > repmat(p/p(end),1,n),1)+1;
% histogram count
[~,x] = histc(r,[0;p/p(end)]);
