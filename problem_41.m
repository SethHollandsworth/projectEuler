a = 7654321;

for i = 1:factorial(numel(num2str(a)))
    numTest = str2double(nthperm(num2str(a),i));
    if isprime(numTest)
        disp(numTest)
        break
    end
end