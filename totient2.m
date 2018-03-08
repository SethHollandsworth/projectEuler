%function k = totient2(n)
l=1; k=87109;
while(k>1)
    p=unique(factor(k));
    k=round(k*((p-1)./p));
    l=l+1;
end