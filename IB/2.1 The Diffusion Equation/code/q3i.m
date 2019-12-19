T=2

%Note must set N and C beforehand in NumericalScheme.m
NumericalScheme

m=T/dt


Uins=Uinsulfunc
Uins=@(X)Uins(X,T)

V=[] %X, but variable X is in use.
U_anal=[]
for i=1:N+1
    V(i)=(i-1)*dx
    U_anal=[U_anal; Uins(V(i))]
end

U_numerical=transpose(X(m+1,:))

E=U_numerical-U_anal

