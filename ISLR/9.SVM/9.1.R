
x1=-10:10
x2=1 + 3*x1
plot(x1,x2,type = "l",col = "red")
text(c(0),c(-20),"greater than 0",col = "red")
text(c(0),c(20),"less than 0",col="red")
lines(x1, 1 - x1/2)
text(c(0),c(-15),"less than 0")
text(c(0),c(15),"greater than 0")
