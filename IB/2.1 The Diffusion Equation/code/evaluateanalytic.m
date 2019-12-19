T=0.25 %this value must be changed

Ufix=Ufixedfunc
Ufix=@(X)Ufix(X,T)
Uins=Uinsulfunc
Uins=@(X)Uins(X,T)
Usemi=Usemiinffunc
Usemi=@(X)Usemi(X,T)

Ufixtabulate=[]
Uinstabulate=[]
Usemitabulate=[]

x=[]

for n=1:9
    x(n)=(n-1)*0.125
    Ufixtabulate=[Ufixtabulate; Ufix(x(n))]
    Usemitabulate=[Usemitabulate; Usemi(x(n))]
    Uinstabulate=[Uinstabulate; Uins(x(n))] 
end

fplot(Ufix,[0,1])
hold on
fplot(Uins,[0,1])
hold on
fplot(Usemi,[0,1])
legend('fixed','insulated','semi-infinite')
xlabel('X')
ylabel('U')
    
    