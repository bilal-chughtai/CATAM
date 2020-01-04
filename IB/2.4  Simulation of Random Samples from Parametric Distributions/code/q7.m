n=50
U=rand(n,1)
V=rand(n,1)
theta_0=2.2
X=-log(1-U)/theta_0
Y=-log(1-V)/theta_0
Z=X+Y

l=@(m) 0


for i=1:n
    
    li=@(theta) 2*log(theta)+log(Z(i))-theta*Z(i);
    l=@(theta) l(theta)+li(theta);  
end

fplot(l,[0.1,4])
hold on
%line([sum(X)*log(2)/n sum(X)*log(2)/n],[-10 0],'LineWidth',1)
ylabel('l_n(theta)')



thetahat=2*n/sum(Z)
