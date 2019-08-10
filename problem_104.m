clear;clc
for i = 2749
    num = fibonacci(i);
    num = vecSplit(num);
    index = num==-16;
    num(index) = [];
    if isperm(num(1:9),[1,2,3,4,5,6,7,8,9])
        disp('woo')
    end
end