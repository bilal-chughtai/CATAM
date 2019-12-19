function [X,Y] = RK4solve( f,x_0,y_0,h,n )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here

Y=[y_0]
X=[x_0]

for i=1:n
    
    X=[X; X(i)+h];
    k1=h.*f(X(i),Y(i,:));
    k2=h.*f(X(i)+h/2,Y(i,:)+k1/2);
    k3=h.*f(X(i)+h/2,Y(i,:)+k2/2);
    k4=h.*f(X(i)+h,Y(i,:)+k3);
    Y=[Y;Y(i,:)+(k1+2*k2+2*k3+k4)/6];
end

end
    

