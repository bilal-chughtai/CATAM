function [ f] = Ufixedfunc(  )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

f=@(X,T) 1-X

for n = 1:25
    fn=@(X,T) 2*sin(n*pi*X)*exp(-n^2*pi^2*T)/(pi*n);
    f=@(X,T) f(X,T)-fn(X,T);
end

end

