clear;clc
vecSplit = @(n) num2str(n)-'0';
count = 1;
for i = 10:99
    for j = 10:99
        iSplit = vecSplit(i);
        jSplit = vecSplit(j);
        if i ~= j && i/j < 1 && (i/j == iSplit(1)/jSplit(2) && iSplit(2) == jSplit(1)) || (i/j == iSplit(2)/jSplit(1) && iSplit(1) == jSplit(2))
            frac{count} = [i,j];
            count = count + 1;
        end
    end
end
