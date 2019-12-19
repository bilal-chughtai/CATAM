function [ value ] = Uinsul(X,T)
% evaluates the analytical U for fixed boundary conditions, at X,T. We
% perform 10 iterations.

value=1;

for n = 1:25
    
    value=value-2*sin((n-1/2)*pi*X)*exp(-(n-1/2)^2*pi^2*T)/(pi*(n-1/2));
end


end