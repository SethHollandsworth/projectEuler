i = 5;
j = 5;
runningTotal = 0;
while i ~= 1 || j ~= 1
    runningTotal = runningTotal + myVar(i,j);
    if i == 1
        j = j-1;
    elseif j == 1
        i = i-1;
    elseif myVar(i-1,j) < myVar(i,j-1)
        i = i-1;
    elseif myVar(i-1,j) > myVar(i,j-1)
        j = j-1;
    end
end
runningTotal = runningTotal + myVar(1,1)
