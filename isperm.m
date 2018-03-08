function perm = isperm(x,y)
    if length(x) == 1 && length(y) == 1 && ismember(x(1),y)
        perm = true;
    elseif ismember(x(1),y)
        yindex = find(y==x(1));
        y(yindex(1)) = [];
        perm = isperm(x(2:end),y);
    else
        perm = false;
    end
end