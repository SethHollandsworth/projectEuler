%teens as a cell array
teens = {'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'};
%running sum
summed = 0;
%goes through all number up until 1000
for i = 1:999
    %goes number by number to add in stuff
    summed = summed + problem_17func(i);
end
%running sum for the teens
count = 0;
%hardcode teens cause they mess stuff up
for j = 1:length(teens)
    count = count + length(teens{j});
end
%for each time the teens popup
count = count * 10;
%adds teens, all the other numbers, and "one thousand"
finalSum = summed + count + 11;
disp(finalSum)