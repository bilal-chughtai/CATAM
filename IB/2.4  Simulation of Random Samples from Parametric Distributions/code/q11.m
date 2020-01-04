n=50
z=norminv(0.9)
mu=4
for j = 1:25   
    X=generatenormal(mu,1,n)
    Xbar(j)=sum(X)/n
    upper(j)=Xbar(j)+z/sqrt(n)
    lower(j)=Xbar(j)-z/sqrt(n)
    if mu <=upper(j) & mu>=lower(j)
        contains(j)=1
    else
        contains(j)=0
    end
end

count=0
for i=1:25
    if contains(i)==1
        count=count+1
    end
end

        
        
