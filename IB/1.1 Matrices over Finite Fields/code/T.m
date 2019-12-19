function [A] = T(A,i,j)
    %transposes rows i and j in a matrix A
    temp=A(i,:);
    A(i,:)=A(j,:);
    A(j,:)=temp;
end

