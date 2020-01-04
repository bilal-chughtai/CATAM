function [ f ] = Uinsulfunc()
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
f=@(X,T) 1

for n = 1:25
    fn=@(X,T) 2*sin((n-1/2)*pi*X)*exp(-(n-1/2)^2*pi^2*T)/(pi*(n-1/2));
    f=@(X,T) f(X,T)-fn(X,T)
end

end

    