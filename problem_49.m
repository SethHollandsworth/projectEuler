%all primes below 9999
numbers = primes(9999);
%gets rid of all primes that are 3 digits or fewer
primesTest = numbers(numbers>=1000);
%iterate through all 4-digit primes
for num = 1:numel(primesTest)
    
    