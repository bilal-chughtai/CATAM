%Note you must set h in the script beforehand
h=0.1
n=10/h


omega=1 %capital omega
delta=0
gamma=1 
w=sqrt(3) %lower case omega
a=1
t_0=0

y_0=[0,0]

f=@(t,y) [y(2), -gamma*y(2)-delta^(3)*y(1)^2*y(2)-omega^2*y(1)+a*sin(w*t)]


A=w*gamma/(w^2*gamma^2+(w^2-1)^2)
B=(2*w*(w^2-1)+gamma^2*w)/(sqrt(4-gamma^2)*(w^2*gamma^2+(1-w^2)^2))
C=-a*(w^2-omega^2)/(w^2*gamma^2+(w^2-omega^2)^2)
D=-w*gamma*a/(w^2*gamma^2+(w^2-omega^2)^2)
y_anal=@(t)C*sin(w*t)+D*cos(w*t) + exp(-gamma*t/2)*(A*cos(sqrt(4-gamma^2)*t/2)+B*sin(sqrt(4-gamma^2)*t/2))



[T,Y]=RK4solve(f,t_0,y_0,h,n)


Y_anal=[0]
for i=2:n+1
    Y_anal=[Y_anal; y_anal(T(i))]
end

E=Y(:,1)-Y_anal





 %plot(T,Y(:,1))
% hold on
%fplot(y_anal)
