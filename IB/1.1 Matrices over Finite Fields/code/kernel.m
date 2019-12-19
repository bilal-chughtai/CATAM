function [ker] = kernel(A,p)
%The algorithm is described in the write up

[B] = ref(A,p);
l = calculatel(B); %members of l are the "fixed" components
rows=size(B,1);
columns=size(B,2);
%r=rank, n=nullity.
r=nnz(l);
%nnz counts non zero terms in the array l
n=columns-r;

if n==0
    ker=zeros(rows,1);
    return 
end

d=0; %d counts how many lin indep elements sof kernel we have so far

for c=columns:-1:1 %loop through columns from bottom
 
    if ismember(c,l) %if fixed do nothing
    else %if component free
        d=d+1;
        x=zeros(columns,1); %initialise vector x
        x(c)=1; %set the free variable to 1
    
        for i=rows:-1:1 % solve the silmutaneous equations, starting from the bottom
            
            if l(i)==0 | l(i)==columns % l(i)=0 means free component, we have already set them all to 0 by the algorithm
                                       % l(i)=columns means we have the equation x_i=0, so no calculation needed
            else % for the fixed x_i which we must calculate

                for j=l(i)+1:columns % formula to calculate  them
                    x(l(i))=x(l(i))-B(i,j)*x(j);
                end
            end
        end
    
        ker(:,d)=x; %append vector x to end of kernel matrix.
    end
    
end
ker=mod(ker,p);     
end

