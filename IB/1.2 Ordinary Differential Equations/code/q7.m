%must set gamma and w first
gamma=0.25
w=2

omega=1
delta=0 
a=1
t_0=0

y_0=[0,0]
h=0.1
n=40/h

f=@(t,y) [y(2), -gamma*y(2)-delta^(3)*y(1)^2*y(2)-omega^2*y(1)+a*sin(w*t)]


    A=w*gamma/(w^2*gamma^2+(w^2-1)^2)
    B=(2*w*(w^2-1)+gamma^2*w)/(sqrt(4-gamma^2)*(w^2*gamma^2+(1-w^2)^2))
    C=-a*(w^2-omega^2)/(w^2*gamma^2+(w^2-omega^2)^2)
    D=-w*gamma*a/(w^2*gamma^2+(w^2-omega^2)^2)
    %y_anal=@(t)-*sin(w*t-atan(w*gamma/(1-w^2)))/(sqrt(w^2*gamma^2+(w^2-1)^2)) + exp(-gamma*t/2)*(A*cos(sqrt(4-gamma^2)*t/2)+B*sin(sqrt(4-gamma^2)*t/2))
    y_anal=@(t)C*sin(w*t)+D*cos(w*t) + exp(-gamma*t/2)*(A*cos(sqrt(4-gamma^2)*t/2)+B*sin(sqrt(4-gamma^2)*t/2))


[T,Y]=RK4solve(f,t_0,y_0,h,n)

fplot(y_anal,[0,40])
hold on
plot(T,Y(:,1))
legend('Analytical Solution','Numerical Solution')
xlabel('t')
ylabel('y')