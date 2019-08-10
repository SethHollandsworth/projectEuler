vec = (1:1000000)./totient(1:1000000);
[~,answer] = max(vec);
disp(answer)