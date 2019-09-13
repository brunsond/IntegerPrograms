function [x,y] = ldsolver(a,b,c)
%Computes one solution [x,y] to the linear Diophantine equation ax+by = c, if it exists.
%This program requires the use of Matlab symbolic toolkit.
i = 1;
r(1) = mod(a,b);
q(1) = floor(a/b);
while (r(i)>0)
    i = i+1;
    a = b;
    b = r(i-1);
    q(i) = floor(a/b);
    r(i) = mod(a,b);
end
gc_factor = b; %Greatest common factor of a and b.
if mod(max(gc_factor,c),min(gc_factor,c))~=0
    disp('no solution')
else
    syms a b
    R_1 = a-q(1)*b;
    temp = b;
    for j = 2:i-1
       R = temp-q(j)*R_1;
       temp = R_1;
       R_1 = R;
    end
    f = c/gc_factor;
    R = f*R;
    [x,y] = coeffs(R);
end
