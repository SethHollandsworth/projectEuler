counts = 7769218;
for i = 9049196:10000000
    summed = i;
    while true
        summed = sum(vecSplit(summed).^2);
        if summed == 89
            counts = counts + 1;
            break
        end
        if summed == 1
            break
        end
    end
end