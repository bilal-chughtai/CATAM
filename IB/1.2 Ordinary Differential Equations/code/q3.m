f=@(x,y) -4*y+3*exp(-x)
anal_y=@(x)exp(-x)-exp(-4*x)
y_0=0
x_0=0
h=0.4
n=10

[X,Y_E]=eulersolve(f,x_0,y_0,h,n)
[X,Y_RK4]=RK4solve(f,x_0,y_0,h,n)   

fplot(anal_y,[0,4])
hold on
plot(X,Y_E)
hold on
plot(X,Y_RK4)
legend('analytical solution','Euler Solution','RK4 solution')
xlabel('x')
ylabel('y')