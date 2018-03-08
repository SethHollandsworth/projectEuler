a = -1000:1000;
b = primes(1000);
largestPrimeNum = [0,0,0];
n = 0;
for i = 1:length(a)
    for j = 1:length(b)
        while n^2+a(i)*n+b(j) > 0 && isprime(n^2+a(i)*n+b(j))
            n = n+1;
            if n > largestPrimeNum(1)
                largestPrimeNum(1) = n;
                largestPrimeNum(2) = a(i);
                largestPrimeNum(3) = b(j);
            end
        end
        n = 0;
    end
end