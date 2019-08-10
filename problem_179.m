counts = 0;
for i = 1:10^7
    if length(factor(i)) == length(factor(i+1))
        counts = counts + 1;
    end
end