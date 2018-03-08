tic
primesBelowMil = primes(10000);
default = 0;
newSum = 0;
%arbitrary values
for j = 500:600
    %length of vec goes up by one each time loop runs
    vec = 1:j;
    %goes until vec will hit the index of the last number in primesBelowMil
    for i = 1:length(primesBelowMil)-(length(vec)-1)
        %replaces old values if better ones are met
        if length(vec) > default && isprime(sum(primesBelowMil(vec))) && sum(primesBelowMil(vec)) <= 1000000
            default = length(vec);
            newSum = sum(primesBelowMil(vec));
        end
        %moves index up by one
        vec = vec + 1;
    end
end
time = toc;