%make variable for problem 81
%have to import data through import wizard and 
%change max i value to how big the matrix is
myVar = [];
for i = 1:80
    eval(sprintf('myVar = [myVar,VarName%d];',i))
end
