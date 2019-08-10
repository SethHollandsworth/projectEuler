%change format for big numbers
format long
%arbitrary upper value for n
n = 286:60000;
%calculate a lot of pentagonal numbers
pentagon = n.*(3.*n-1)./2;
%calculate a lot of hexagonal numbers
hexagon = n.*(2.*n-1);
%a lot of triangular numbers
triangle = n.*(n+1)./2;
%see if triangles and pentagons are the same
triangleAndPentagon = triangle(ismember(triangle,pentagon));%triangle(triangle==pentagon)
%see if all 3 are in common
all3 = triangleAndPentagon(ismember(triangleAndPentagon,hexagon));

fprintf('the next triangular number that is all 3 is %d\n',all3)
