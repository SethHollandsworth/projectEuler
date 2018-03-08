odds = 3:2:100001;
countPrimes = 0;
diagNum = -3;
for spiral = 1:length(odds)
    spiralSquared = odds(spiral)^2;
    countPrimes = countPrimes + sum([isprime(spiralSquared)  isprime(spiralSquared-spiral*2)  isprime(spiralSquared-spiral*4)  isprime(spiralSquared-spiral*6)]);
    diagNum = diagNum + 4;
    ratio = countPrimes/diagNum;
    if ratio <= .1
        break
    end
end
%because odds starts at 3 instead of 1, subtract 1 from spiral
disp(odds(spiral-1))