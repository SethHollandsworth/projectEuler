maxPrimes = [0,0,0];
for a = -999:999
    for b = -1000:1000
        n = 0;
        while n^2+a*n+b >= 0 && isprime(n^2+a*n+b)
            n = n+1;
            if n > maxPrimes(1)
                maxPrimes(1:3) = [n,a,b];
            end
        end
    end
end
disp(maxPrimes(2)*maxPrimes(3))