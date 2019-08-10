minNum = [0,10^7];
smallPrimes = primes(2000);
format long
j = 3:2:10^7-1;
%cut down a lot of the numbers to iterate through
for k = 1:length(smallPrimes)
    j = j(rem(j,smallPrimes(k))~=0);
end
%%
for i = 1:length(j)
    totiNum = totient(j(i));
    if isperm(vecSplit(totiNum),vecSplit(j(i))) && j(i)/totiNum < minNum(2)
        minNum = [j(i),j(i)/totiNum];
    end
end
%nums = 1:10^7;
%toti = totient(nums);
%numsOverToti = nums./toti;
%[minNum,minSpot] = min(totiNum);