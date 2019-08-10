tic
count = 0;
%goes through all serial date numbers
for i = datenum('01-January-1901'):datenum('01-December-2000')
    %gets the string date in formet "dd-mm-yyyy"
    dateString = datestr(i);
    %checks to see if it's the first of the month
    if all(dateString(1:2) ==  '01')
        %checks to see if it's a sunday
        if weekday(i) == 1
            %count goes up
            count = count + 1;
        end
    end
end

time = toc;