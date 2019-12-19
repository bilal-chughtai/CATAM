function [B] = artc(A,p)
    %annihilate row to column
    %this one is simple; we just take the kernel of A
    B=kernel(A,p)
end

