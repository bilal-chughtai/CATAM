T=1
%must set values of N and C in NumericalScheme
NumericalScheme

m=T/dt

V=[]
for i=1:N+1
    V(i)=(i-1)*dx
end
U_numerical=transpose(X(m+1,:))

Uins=Uinsulfunc
Uins=@(X)Uins(X,T)

fplot(Uins,[0,1])
hold on
plot(V,U_numerical)
legend('analytical','numerical')
xlabel('X')
ylabel('U')
    

