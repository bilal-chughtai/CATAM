function [ A ] = D( A,i,q,inverse )
    %divides row i of A by q
    A(i,:)=A(i,:)*inverse(q);
end

