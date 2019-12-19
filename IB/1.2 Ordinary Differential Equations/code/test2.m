omega=1
delta=0
gamma=1
% gamma=0.5
% gamma=1
% gamma=1.9
w=2
% w=2
a=1
t_0=0

A=a/gamma
B=a/sqrt(4-gamma^2)

y=@(t)-a*cos(t)/gamma + exp(-gamma*t/2)*(A*cos(sqrt(4-gamma^2)*t/2)+B*sin(sqrt(4-gamma^2)*t/2))

fplot(y)