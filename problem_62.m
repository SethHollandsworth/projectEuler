n = 100000;
vecSplit = @(n) num2str(n)-'0';
cubeDigits = cell(1,n);
for i = 345:n
    index = i-344;
    cubeNum = vpi(i)^3;
    temp = vecSplit(cubeNum);
    cubeDigits{index} = temp(temp ~= -16);
end

for j = 1:length(cubeDigits)
    count = 0;
    for k = j+1:length(cubeDigits)
        if length(cubeDigits{j})==length(cubeDigits{k}) && isperm(cubeDigits{j},cubeDigits{k})
            count = count + 1;
        end
        if count == 5
            flag = 1;
            disp(str2double(strrep(num2str(cubeDigits{j}),' ','')))
            break
        end
    end
    if flag == 1
        break
    end
end
