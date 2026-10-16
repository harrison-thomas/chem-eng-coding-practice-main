
%% Vapour Pressure of Water Calculation and Graphing
% This script calculates the vapour pressure of water at various temperatures
% log10(P) = A - B / (C + T), with T in degrees C and P in mmHg
% Author: Harrison Thomas, 2026

clear;
clc;
close all;

T_LOW = 1:1:99;
T_HIGH = 99:1:374;

A_LOW = 8.07131;
B_LOW = 1730.63;
C_LOW = 233.426;

A_HIGH = 8.14019;
B_HIGH = 1810.94;
C_HIGH = 244.485;

P_ATM = 760;

P_LOW = 10.^(A_LOW - B_LOW ./ (C_LOW + T_LOW));
P_HIGH = 10.^(A_HIGH - B_HIGH ./ (C_HIGH + T_HIGH));

ONE_BAR_TEMP = interp1(P_HIGH, T_HIGH, P_ATM);

% Plotting Pressure against Temperature

semilogy(T_LOW, P_LOW, "r")
hold on
semilogy(T_HIGH, P_HIGH, "b")
yline(P_ATM)
xline(ONE_BAR_TEMP)

ylabel("Pressure / mmHg")
xlabel("Temperature / °C")
legend("Water 1-99°C", "Water 100-374°C", "760 mmHg", "Temp at 760mmHg")
xticks([0, 50, ONE_BAR_TEMP, 150, 200, 250, 300, 350])
