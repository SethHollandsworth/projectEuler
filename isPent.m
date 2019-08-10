function [boolean] = isPent(n)
boolean = rem((sqrt(24*n+1)+1)/6,1) == 0;
end