% test sample discrete
p = [0.1,0.4,0.3,0.05,0.1,0.05];
n = 2000;
hist(rndDiscrete(p,n));
pause;
x = mh_gaussian(25000);
hist(x,100);
