a = [];
for i = 1:500
    for j = 1:2000
        if length(strcat(num2str(i),num2str(j),num2str(i*j))) == 9
            if all(num2str(strcat(num2str(i),num2str(j),num2str(i*j)))- '0')
                if all(ismember([1,2,3,4,5,6,7,8,9],num2str(strcat(num2str(i),num2str(j),num2str(i*j)))- '0'))
                    a = [a,i*j];
                end
            end
        end
    end
end
b = unique(a);