N=8;
C=1/2;

dx=1/N;
dt=C*(dx)^2;

%we have to go up to t=2 maximum, hence we run the numerical scheme up to
%t=2

rows=2/dt +1;
columns=N+1; %+1's required as we have a 0 entry

%we set up a matrix of the required size who's elements will be the various
%X(m+1,n+1)=U_n^m (as in the project) (see project for description)

X=zeros(rows,columns);

%Initial and boundary data tells us U_n^0=0 and U_0^m=1 m=/=0, with
%U_0^0=0.5. Hence first column is all 1's, bar the first element.

X(:,1)=zeros(rows,1)+1;
X(1,1)=0.5;

%Now we loop through the rows, applying the numerical scheme.

for m=0:rows-1 %this is the actual value of m, hence we need to offset by 1 in matrix indexing
                % loop at m calculates the U_*^m+1
    
    for n=1:columns-2 %the case for U_N^* is slightly different, due to the boundary condition
        
        X(m+2,n+1)=X(m+1,n+1)+C*(X(m+1,n+2)-2*X(m+1,n+1)+X(m+1,n));
        
    end
    
    %U_N^*
    
    X(m+2,columns)=X(m+1,columns)+C*(2*X(m+1,columns-1)-2*X(m+1,columns));
end




