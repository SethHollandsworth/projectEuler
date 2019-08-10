isBouncy = @(numTest) ~(isDecreasing(numTest) || isIncreasing(numTest));
ratio = 0;
count = 0;
bouncy = 0;
%ratio you're trying to find
n = .99;
while true
    if count == 1587000
        disp(ratio)
    end
    if abs(ratio - n) < 0.00000000000001
        disp(count)
        break
    end
    numTest = vecSplit(count);
    if isBouncy(numTest)
        bouncy = bouncy + 1;
    end
    count = count + 1;
    ratio = bouncy/count;
    
    
end