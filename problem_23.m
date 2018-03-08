tic
%preallocate for speed
abundant = zeros(1,6965);
%gets all nonAbundant numbers
count = 1;
for i = 1:28123
    divisors = divisor(i);
    if i < sum(divisors(1:end-1))
        abundant(count) = i;
        count = count + 1;
    end
end
%%
%preallocate for speed
abundantSums = zeros(1,24259096);
count = 1;
%gets array of sums of abundant numbers
for j = 1:length(abundant)
    for k = j:length(abundant)
        abundantSums(count) = abundant(j)+abundant(k);
        count = count + 1;
    end
end

allNums = 1:28123;
%finds all the numbers that can't be expressed as an abundant sum
nonAbundant = allNums(~ismember(allNums,abundantSums));
time = toc;
fprintf('%d %.4f\n',sum(nonAbundant),time)
 