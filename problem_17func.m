function numLetters = problem_17func(n)
%input number
%output how many letters it takes to write it
%SETH HOLLANDSWORTH
onesie = {'one','two','three','four','five','six','seven','eight','nine'};
tens = {'','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'};
hundred = {'hundred'};
%running total
numLetters = 0;
%if the number is over 100
if floor(n*.01) >= 1
    %adds in the number of letters for the hundreds place plus "hundred"
    numLetters = numLetters + length(onesie{floor(n*.01)}) + length(hundred{1});
    %if the number is other than a solid 100 divisible, add word "and"
    if mod(n,100) > 0
        numLetters = numLetters + 3;
    end
end
%if number has a tens place
if mod(floor(n*.1),10) >= 1
    %add in letters for the tens place
    numLetters = numLetters + length(tens{mod(floor(n*.1),10)});
end
%checks the ones places
onesPlace = mod(n,10);
%if there isn't a zero in the ones place then we add in the letterCount for
%ones
if onesPlace > 0
    numLetters = numLetters + length(onesie{mod(n,10)});
end
%if the number is a teen
if mod(n,100)>= 10 && mod(n,100)<=19
    %start over and only count the hundreeds place so we don't mess up the
    %entire total
    numLetters = 0;
    if floor(n*.01) >= 1
        numLetters = numLetters + length(onesie{floor(n*.01)}) + length(hundred{1});
        %if the number is other than a solid 100 divisible, add word "and"
        if mod(n,100) > 0
            numLetters = numLetters + 3;
        end
    end
end
end


