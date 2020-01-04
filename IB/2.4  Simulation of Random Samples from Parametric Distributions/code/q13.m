k=40
n=500
chi=[]
for i=1:n
X=generatenormal(0,1,k);
chi(i)=sum(X.^2);
end

x = 0:0.2:max(chi);
y = n*max(chi)/50*chi2pdf(x,k);  
plot(x,y)
hold on
histogram(chi,50) 
legend('pdf of chi square', 'histogram')
    



%normalise needs area
