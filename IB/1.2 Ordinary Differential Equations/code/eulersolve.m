function [X,Y] = eulersolve(f,x_0,y_0,h,n)
%implementation of the euler method

Y=[y_0];
X=[x_0];

for i=1:n
    X=[X; X(i)+h];
    Y=[Y;Y(i)+h*f(X(i),Y(i))];
end

