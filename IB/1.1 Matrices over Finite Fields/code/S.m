function [A] = S(A,k,q,i)  
    %Subtract from row k, q times row i
    A(k,:)=A(k,:)-q*A(i,:);
end

