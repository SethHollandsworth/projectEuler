n = 100000;
allNums = 1:n;
prime = primes(n+100);
oddComposite = allNums(~ismember(allNums,prime) & ~rem(allNums,2)==0);
%goes for length of oddComposite
for j = 1:length(oddComposite)
    %initialize i
    i = 1;
    %initialize false
    val = false;
    %runs as long as prime is less than oddComposite
    while prime(i) < oddComposite(j)
        %checks to see if the number is an integer
        if rem(sqrt((oddComposite(j)-prime(i))/2),1)==0
            val = true;
        end
        i = i + 1;
    end
    if ~val
        disp(oddComposite(j))
    end
end