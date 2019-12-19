f=@(x,y) exp(x);
anal_y=@(x) exp(x)
y_0=1;
x_0=0;
h=0.5
n=2/h

[X,Ye]=eulersolve(f,x_0,y_0,h,n)
[X,Ylf]=LFsolve(f,x_0,y_0,h,n)
[X,Yrk4]=RK4solve(f,x_0,y_0,h,n)

fplot(anal_y,[0,2])
hold on
plot(X,Ye)
hold on
plot(X,Ylf)
hold on
plot(X,Yrk4)
legend('Analytical Solution','Euler','LF','RK4')
xlabel('x')
ylabel('y')