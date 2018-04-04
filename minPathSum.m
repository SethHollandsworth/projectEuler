load p081mat.mat
m = 80;
n = 80;
temp = zeros(length(mat));
temp(1,1) = mat(1,1);
for i = 2:m
    temp(i,1) = temp(i-1,1) + mat(i,1);
end
for j = 2:n
    temp(1,j) = temp(1,j-1) + mat(1,j);
end

for i = 2:m
    for j = 2:n
        temp(i,j) = min([temp(i-1,j) temp(i,j-1)]) + mat(i,j);
    end
end
num = temp(m,n);