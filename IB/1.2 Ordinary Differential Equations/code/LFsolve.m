function [X,Y] = LFsolve( f,x_0,y_0,h,n )
%we do the first step by euler

X=[x_0;x_0+h];
Y=[y_0; y_0+h*f(x_0,y_0)];

for i=2:n
    X=[X;X(i)+h];
    Y=[Y;Y(i-1)+2*h*f((X(i)),Y(i))];
end


end

