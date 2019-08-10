format long
total = 0;
n = 100000000;
for i = 1:n
    pete = sum(randi(4,[1 9]));
    colin = sum(randi(6,[1 6]));
    if pete > colin
        total = total + 1;
    end
end

disp(total/n)