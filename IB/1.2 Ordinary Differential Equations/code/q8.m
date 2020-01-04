%must set delta beforehand
delta=20  
omega=1
gamma=0
w=1
a=1
t_0=0
y_0=[0,0]
h=0.01
n=60/h
f=@(t,y) [y(2), -gamma*y(2)-delta^(3)*y(1)^2*y(2)-omega^2*y(1)+a*sin(w*t)]
[T,Y]=RK4solve(f,t_0,y_0,h,n)

A=-4^(1/3)
B=-1/8
C=1/8
y_anal=@(t)delta^(-1)*(A*cos(t))+B*sin(t)+C*sin(3*t)

fplot(y_anal,[0,60])
hold on
plot(T,Y(:,1))
xlabel('t')
ylabel('y')
legend('Series','Numerical')

