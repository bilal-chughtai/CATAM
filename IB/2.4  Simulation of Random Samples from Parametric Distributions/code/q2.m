n=1000
U=rand(n,1)
theta_0=1.2
X=-log(1-U)/(theta_0)

l=@(m) 0


for i=1:n
    
    li=@(m) log(log(2))-log(m)-log(2)*X(i)/m;
    l=@(m) l(m)+li(m);  
end

fplot(l,[0.1,1])
%hold on
%line([sum(X)*log(2)/n sum(X)*log(2)/n],[-10 0],'LineWidth',1)
xlabel('m')
ylabel('l_n(m)')

m=log(2)/theta_0
mhat=sum(X)*log(2)/n

