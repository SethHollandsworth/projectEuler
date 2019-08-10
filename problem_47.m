for i = 1:500000
    if length(unique(factor(i))) == 4 && length(unique(factor(i+1))) == 4 ...
            && length(unique(factor(i+2))) == 4 && length(unique(factor(i+3))) == 4
        disp(i)
        break
    end
end


