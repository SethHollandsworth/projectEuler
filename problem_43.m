pandigital = 1234567890;
specialPan = 0;
format long

for i = 1:factorial(numel(num2str(pandigital))-1)
    temp = nthperm(num2str(pandigital),i);
    numTest = str2double(temp);
    if mod(str2double(temp(8:10)),17) == 0
        if mod(str2double(temp(7:9)),13) == 0
            if mod(str2double(temp(6:8)),11) == 0
                if mod(str2double(temp(5:7)),7) == 0
                    if mod(str2double(temp(4:6)),5) == 0
                        if mod(str2double(temp(3:5)),3) == 0
                            if mod(str2double(temp(2:4)),2) == 0
                                specialPan = specialPan + str2double(temp);
                            end
                        end
                    end
                end
            end
        end
    end
end
disp(specialPan)