function [inverse] = findinverses(p)

%initialise inverse
inverse=[];

%check if prime
if isprime(p)==0
    inverse='Please enter a prime';
    return
end

%loop to calculate the inverse
for a = 1:p-1
    for b=1:p-1
        if mod(a*b,p)==1
            inverse=[inverse b];
            break %out of the b loop
        end
    end
end


