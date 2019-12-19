f=@(x,y) -4*y+3*exp(-x)
anal_y=@(x)exp(-x)-exp(-4*x)
y_0=0
x_0=0
p=anal_y(0.4)
H=[]
E_E=[]
E_LF=[]
E_RK4=[]

for k=0:15
    n=2^k
    h=0.4/n;     
    H=[H;h];
    

   [X,Y_E]=eulersolve(f,x_0,y_0,h,n);
   [X,Y_LF]=LFsolve(f,x_0,y_0,h,n);
   [X,Y_RK4]=RK4solve(f,x_0,y_0,h,n);
    
   E_E=[E_E;Y_E(n+1)-p];
   E_LF=[E_LF;Y_LF(n+1)-p]
   E_RK4=[E_RK4;Y_RK4(n+1)-p]
end

lH=log(H)

plot(log(H),log(abs(E_E)))
hold on
plot(log(H),log(abs(E_LF)))
hold on
plot(log(H),log(abs(E_RK4)))
legend('Euler','Leapfrog','RK4')

xlabel('log(h)')
ylabel('log(abs(E))')

