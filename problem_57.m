tic
syms t
out = 1 + 1 / t;
count = 0;
for i = 1:7
    
    expanded = subs(out, t, 2 + (1 / t));
    %disp(expanded)
    evaluated = double(subs(expanded,t,2));
    [num,den] = rat(evaluated);
    if numel(num2str(num)) > numel(num2str(den))
        count = count + 1;
    end
    out = expanded;
end
disp(count)
out = toc;
disp(out)
    