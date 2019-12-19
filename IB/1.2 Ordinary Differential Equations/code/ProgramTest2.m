f=@(x,y) [y(2),-y(1)];
anal_y=@(x) cos(x)
y_0=[1,0];
x_0=0;
h=1
n=5/h

[X,Y]=RK4solve(f,x_0,y_0,h,n)

fplot(anal_y,[0,5])
hold on
plot(X,Y(:,1))
legend('Analytical Solution','RK4 Solution')
xlabel('x')
ylabel('y')