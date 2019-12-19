function [l] = calculatel(M)
%determines locations of pivot elements in the ref matrix
for i = 1:size(M,1) %loop through rows
    for j = 1:size(M,2) %loop through columns
        if M(i,j)==1 %find the first 1 in the row
            l(i)=j; 
            break %out of the for loop
        end
        if j==size(M,2) %if we get to the end of the column, and havn't found a 1
            l(i)=0;
        end
    end

end

