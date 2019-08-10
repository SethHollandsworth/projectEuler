odds = 3:2:1001;
summed = 0;
for spiral = 1:length(odds)
    spiralSquared = odds(spiral)^2;
    summed = summed + spiralSquared + (spiralSquared-spiral*2) + (spiralSquared-spiral*4) + (spiralSquared-spiral*6);
end
summed = summed + 1;
disp(summed)