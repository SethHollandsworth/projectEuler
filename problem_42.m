%{
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
%}

%% Pre-allocate array of Triangle numbers to create lookup table
n = 1:100;
triangle = .5.*n.*(n+1);

%% Compute Value of Each Word
numWords = numel(p042words); % Number of words in text file
wordValues = zeros(1, numWords); % Pre allocate word values

for i = 1:numWords
    wordValues(i) = wordval(p042words{i}); 
end

%% Figure out which word values are triangle numbers
triangleWordCount = 0; % Initalize the number of triangle words as zero

% Loop through word values to find out number of triangle words
for i = 1:numWords
   if (ismember(wordValues(i), triangle))
       triangleWordCount = triangleWordCount + 1; % Increment Count
   end
end

%% Display Results
fprintf('This text file contains %d triangle words.\n', triangleWordCount);
