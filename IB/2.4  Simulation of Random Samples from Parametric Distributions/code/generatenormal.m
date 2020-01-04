function [ X ] = generatenormal( mu,sigma,n )

for i = 1:n
    
    A=rand;
    B=rand;
    phi=2*pi*A;
    V=-2*log(1-B);
    X(i)=mu+sigma*sqrt(V)*cos(phi);
    
end


end

