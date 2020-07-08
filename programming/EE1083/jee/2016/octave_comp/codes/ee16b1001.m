%Octave code for Problem 1
clear;
close;
clc;

%begin function
function fn=recr(n,x) 

if(rem(n,3)==1)
fn=1./(1-x);           %f0

elseif(rem(n,3)==2)
fn=recr(1,recr(1,x));  %f1

end

endfunction %end function

%f100 which is equal to f1
a=recr(1,recr(100,3))   
b=recr(1,recr(1,2/3))   %f1
c=recr(1,recr(2,3/2))   %f2

%Gives the required result
Sum=a+b+c              
