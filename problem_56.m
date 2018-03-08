convertN = @(n) num2str(n) - '0';
maxSum = 1;
format long
for a = 1:100
    for b = 1:100
        num = a^b;
        summedDigits = vpa(convertN(num),100^100);
        summedDigits = sum(summedDigits(summedDigits>=0&summedDigits<=9));
        if summedDigits > maxSum
            maxSum = summedDigits;
        end
    end
end
disp(maxSum)