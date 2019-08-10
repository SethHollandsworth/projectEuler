maxCycle = [0,0];
prime = primes(1000);
prime = prime(2:end);
for i = 1:length(prime)
    n = 2;
    prod = 0;
    count = 0;
    while prod ~= 1
        prod = mod(10^n,prime(i));
        n = n + 1;
        if prod ~= 1
            count = count + 1;
        end
        if count > maxCycle(2)
            maxCycle(1) = prime(i);
            maxCycle(2) = count;
        end
    end
end