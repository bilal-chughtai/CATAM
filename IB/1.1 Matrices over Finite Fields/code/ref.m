function [A] = ref( A,p )
%Algorithm: Start with input matrix A. Take i=j=1. If A_ij=0 try to
%find another row k in A with A_kj not 0. If this exists swap row 1 with
%row k. If not take i=2 and repeat... 
%If no suitable pivot we are 0 matrix - done.
%Once we have a pivot we divide whole row by pivot.
%Then subtract multiples of this row from other rows to ensure whole column is 0's 
%Increase i,j by 1 and repeat until j reaches number of columns or i
%reaches number of rows

rows=size(A,1);
columns=size(A,2);
i=1;
j=1;
inverse=findinverses(p);

while j<= columns

%find the pivot row and swap it in to place
    if mod(A(i,j),p)==0
        while j<=columns
    
            for k = i:rows
                if mod(A(k,j),p)~=0
                    A=T(A,k,i);
                    break % out of inner while loop - now have a pivot
                end
            end
        
            if mod(A(i,j),p)==0
                j=j+1; %keeps adding 1 to j until we find a non zero term
            else
                break
            end
        end
    
    %we are done once the inner while finishes and j increases past columns
        if j>columns 
            A=mod(A,p);
            break
        end
    end

    A=mod(A,p);

%divide pivot row to get 1
    A=D(A,i,A(i,j),inverse);
    A=mod(A,p);
%subtract rows below
    for k= i+1:rows
        A=S(A,k,A(k,j),i);  
    end

% we now add 1 to i and j and loop this until we reach the bottom right
% corner

    i=i+1;
    j=j+1;

    if j>columns | i>rows
        A=mod(A,p);
    break %out of the first while and hence end the program
    
    end
end



    





