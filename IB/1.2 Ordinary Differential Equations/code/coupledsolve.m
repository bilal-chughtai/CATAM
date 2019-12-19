omega=1
delta=0
gamma=1
w=1
t_0=0
y_0=[0,0] %values y(0) y'(0)
h=0.01
n=1500
a=1


f=@(t,y) [y(2), -gamma*y(2)-delta^(3)*y(1)^2*y(2)-omega^2*y(1)+a*sin(w*t)]
[T,Y]=RK4solve(f,t_0,y_0,h,n)

plot(T,Y(:,1))