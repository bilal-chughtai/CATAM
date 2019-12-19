function [ f ] = Usemiinffunc()
%K=1
f=@(X,T)erfc(X/(2*sqrt(T)));
end

