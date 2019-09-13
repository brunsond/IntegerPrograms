function y = partitions(x)

%Calculates the partitions y of integer x, including the single partition.

%e.g. The partitions of x = 4 are:
%4
%3  1
%2  2
%2  1   1
%1  1   1   1
%So, y(4) = 5.

if (x-floor(x) ~= 0)
    print('Error. x must be integral.')
elseif (x<0)
    print('Error. x must be nonnegative.')
else
    x = int64(x);
    j = 1;
    poly = 1;   %Generating function polynomial.
    while j<=x
        new_factor = [];
        new_factor(1) = 1;
        num_sets = x/j;
        i = 2;
        k = 1;
        while k <= num_sets
            new_factor(i:i+(j-1)) = [zeros(1,j-1),1];
            k = k+1;
            i = i+j;
        end
        poly = conv(poly,fliplr(new_factor));
        j = j+1;
    end
end
n = length(poly)-1; %Highest degree in resulting polynomial.
y = poly(n-x+1);

end
