clc
clear all
L = 10;
T0 = 300;
Icguess_target = fzero(@(x) bar_res(x),-1);
[x,y] = ode45(@bar_temp, [0 L], [T0 Icguess_target]);
figure
plot(x,y(:,1));
xlabel('x');
ylabel('T');
title('Temperature districbution in a heated rod');

function dTdx = bar_temp(x,y)
h_const = 0.05;
sigma = 2.7*10^(-9);
%T_inf = 200;
T_inf = 200
dTdx = [y(2);-h_const*(T_inf-y(1))-sigma*(T_inf^4-y(1)^4)];
end
function r = bar_res(Icguess)
T0 = 300;
TL = 400;
L = 10;
[x,y]= ode45(@bar_temp, [0 L], [T0 Icguess]);
r = y(end,1)-TL;
end
