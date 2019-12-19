omega=1
delta=0
gamma=1
w=sqrt(3)
a=1
t_0=0
syms t

A=w*gamma/(w^2*gamma^2+(w^2-1)^2)
B=(2*w*(w^2-1)+gamma^2*w)/(sqrt(4-gamma^2)*(w^2*gamma^2+(1-w^2)^2))


y=-sin(w*t-atan(w*gamma/(1-w^2)))/(sqrt(w^2*gamma^2+(w^2-1)^2)) 
q=exp(-gamma*t/2)*(A*cos(sqrt(4-gamma^2)*t/2)+B*sin(sqrt(4-gamma^2)*t/2))

%PI(0)
%CF(0)



dy=diff(y)
dq=diff(q)
double(subs(dy,t,0))
double(subs(dq,t,0))

% k=diff(diff(y))+gamma*diff(y)+y
% fplot(k)
% hold on
% fplot(sin(sqrt(3)*t))

fplot(y+q)


fplot(y+q)



