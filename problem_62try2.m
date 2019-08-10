tic
cubes = vpi(5000:10000).^3;
convert = @(n) n(n~=-16);
flag = 0;
for i = 1:length(cubes)
    count = 0;
    for j = i:length(cubes)
        if isperm(convert(vecSplit(cubes(j))),convert(vecSplit(cubes(i))))
            count = count + 1;
        end
        if count == 5% || count >= 3
            disp(cubes(i))
            flag = 1;
            break
        end
    end
    if flag
        break
    end
end
time = toc;