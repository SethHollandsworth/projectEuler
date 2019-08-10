%vecSplit = @(n) num2str(n)-'0';
combo = @(n) str2double(strrep(num2str(n),' ',''));
%circular primes
primeList = primes(1000000);
finalList = 0;
count = 1;
primeListPrime = [];
for i = 1:length(primeList)
    if ~any(ismember(num2str(primeList(i))-'0',[0,2,4,6,8]))
        primeListPrime(count) = primeList(i);
        count = count+1;
    end
end
%%
%{
final = 0;
for i = 1:length(primeListPrime)
    split = vecSplit(primeListPrime(i));
    count = 0;
    factSplit = factorial(length(split));
    for j = 0:factSplit-1
        perm = nthperm(split,j);
        if isprime(combo(perm))
            count = count + 1;
        end
        if count == factSplit
            final = final + 1;
        end
    end
end
%}
%{
final = 0;
for i = 1:length(primeListPrime)
    split = vecSplit(primeListPrime(i));
    allPerms = perms(split);
    [r,c] = size(allPerms);
    vec = [];
    for j = 1:r
        vec(j) = combo(allPerms(j,:));
    end
    if all(ismember(vec,primeListPrime))
        final = final+1;
    end
end
%}
final = 0;
for i = 1:length(primeListPrime)
    splitUp = vecSplit(primeListPrime(i));
    splitLength = length(vecSplit(primeListPrime(i)));
    count = 1;
    rotated = primeListPrime(i);
    for j = 1:splitLength
        if isprime(rotated)
            count = count + 1;
            rotated = circshift(vecSplit(rotated),1);
            rotatedLog = rotated >= 0;
            rotated = rotated(rotatedLog);
            if count == splitLength
                final = final + 1;
                
            end
        end
    end
end
            
        
%disp(length(finalList))
disp(final)