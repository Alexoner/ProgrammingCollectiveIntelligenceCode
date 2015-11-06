N = 50000;
T1 = rand(1, N);
T2 = rand(1, N);

r = sqrt(-2*log(T2));
theta = 2*pi*T1;
X = [r.*cos(theta); r.*sin(theta)];
mu = [1; 2];
Sigma = [5 2; 2 1];
L = chol(Sigma);

X1 = repmat(mu, 1, N) + L*X;

nbin = 30;

hist3(X1', [nbin nbin]);
set(gcf, 'renderer', 'opengl');
set(get(gca, 'child'), 'FaceColor', 'interp', 'CDataMode', 'auto');

[z c] = hist3(X1', [nbin nbin]);
[x y] = meshgrid(c{1}, c{2});

figure;
surfc(x,y,-z);
