function [ value ] = Ufixed(X,T)
% evaluates the analytical U for fixed boundary conditions, at X,T. We
% perform 10 iterations.

value=1-X;

for n = 1:25
    
    value=value-2*sin(n*pi*X)*exp(-n^2*pi^2*T)/(pi*n);


end

