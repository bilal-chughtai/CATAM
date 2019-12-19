function [ C ] = actr( A,p )
    %annihilate column to row
    %we first transpose so we can work with rows, then take the kernel, then
    %tranpose again
    B=transpose(A)
    B=kernel(B,p)
    C=transpose(B)
end

