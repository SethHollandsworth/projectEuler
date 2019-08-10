%Lychrel numbers
tic
lychrelCount = 0;
for i = 1:10000
    numStore = i;
    for j = 1:50
        numStore = numStore + str2double(fliplr(num2str(numStore)));
        if numStore == str2double(fliplr(num2str(numStore)))
            break
        end
        if j == 50
            lychrelCount = lychrelCount + 1;
        end
    end
end
time = toc;
