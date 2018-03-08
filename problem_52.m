convertN = @(n) num2str(n) - '0';
tic
for i = 100000:1000000
    numTest = convertN(i);
    multiples = [i*2 i*3 i*4 i*5 i*6];
    if all(ismember(convertN(multiples(1)),numTest))
        if all(ismember(convertN(multiples(2)),numTest))
            if all(ismember(convertN(multiples(3)),numTest))
                if all(ismember(convertN(multiples(4)),numTest))
                    if all(ismember(convertN(multiples(5)),numTest))
                        disp(i)
                        time = toc;
                    end
                end
            end
        end
    end                      
end