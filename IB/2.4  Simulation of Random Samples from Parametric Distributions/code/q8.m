n=100
N=200
theta_0=2.2

for i=1:N
U=rand(n,1)
V=rand(n,1)
X=-log(1-U)/theta_0
Y=-log(1-V)/theta_0
Z=X+Y
thetahat(i)=2*n/sum(Z)
end

histogram(thetahat,25)
xlabel('\theta')
ylabel('frequency')