function [X,Y_LF,Y,E] = q1(h)


f=@(x,y) -4*y+3*exp(-x);
anal_y=@(x)exp(-x)-exp(-4*x);
y_0=0;
x_0=0;

n=10/h;

[X,Y_LF]=LFsolve(f,x_0,y_0,h,n)

%constructing the analytical solution at each point
Y=[y_0];
for i=2:n+1
    Y=[Y;anal_y(X(i))];
end

E=Y_LF-Y

%to solve for gamma we have E=exp(gx) log(E)=gx hence g is the gradient of
%a log(absE) x graph - need to remove first line cant log0

Xm = X(2:end);
Em = E(2:end);

p=polyfit(Xm,log(abs(Em)),1)
plot(Xm,log(abs(Em)))
xlabel(p)
ylabel('log(|E|)')

end

