function logic = isIncreasing(n)
if length(n) == 1
    logic = true;
elseif n(1) <= n(2)
    logic = isIncreasing(n(2:end));
else
    logic = false;
end
end