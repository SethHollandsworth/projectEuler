function value = wordval(word)
% This function has undefined behavior for words with not uppercase A-Z
% characters. 64 is ascii code for one below 'A'
    % Input - String containing upper-case A-Z
    % Output - Word Value (A = 1, B = 2, ..., Z = 26)
    
    %{
    Casey's Way
    if (length(word) > 1)
        % Recursive Case - first letter + rest of word
       value = word(1) - 64 + wordval(word(2:end));
    else
        % Base Case - Single Letter
        value = word(1) - 64;
    end
    %}
    
    %my way
    value = sum(double(word)-64);
    
    
end
