
X=0;

    
  
    
    
    Ufixflux=@(X,T) 1;
    for n = 1:25
        Ufixflux=@(X,T)Ufixflux(X,T)+2*cos(n*pi*X)*exp(-n^2*pi^2*T);
    end
   
    
    
    Uinsflux=@(X,T)0
    for n = 1:25
        Uinsflux=@(X,T)Uinsflux(X,T)+2*cos((n-1/2)*pi*X)*exp(-(n-1/2)^2*pi^2*T);    
    end
    
    
    epsilon= @(X,T) X/sqrt(T);
    
    Usemiflux=@(X,T)2*exp(-(epsilon(X,T)/2)^2)/(sqrt(pi*T));
    
    Ufixflux=@(T)-Ufixflux(0,T)
    Uinsflux=@(T)-Uinsflux(0,T)
    Usemiflux=@(T)-Usemiflux(0,T)

fplot(Ufixflux,[0.0625,2])
hold on
fplot(Uinsflux, [0.0625,2])
hold on
fplot(Usemiflux, [0.0625,2])
legend('fixed','insulated','semi-infinite')
xlabel('T')
ylabel('-U_X')