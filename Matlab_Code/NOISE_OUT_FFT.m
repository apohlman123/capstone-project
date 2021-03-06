%26Apr19
%Hi-Fi Audio Production Instrument
%Clay Sauter and Austin Pohlman
    %This code will recieve input data from CSV files...
    %...and compute the FFT for frequency-domain analysis
%NOTE THAT DATA MUST BE TAKEN AT 5MS/s with 100ms in time window
%This equates to 10Hz/sample resolution, 500000 data points
clc
clear all
%Read input data from CSV from row 9-500008 (0ms-100ms)
Data     = csvread('Output_Noise_Floor_5MS_s.csv',9,1,[9 1 500008 1]);
n        = length(Data);
fs       = 1/2E-7;
T        = 2E-7;

%Time Domain
time = 0:T:1E-3-T;
subplot(3,1,1)
%First +slope 0-crossing is at Data(4009)
plot(time,Data(4009:9008))

%When data uses negative times, fftshift shifts T=0 to start of array
%Then we use fftshift again to get +/- frequency domain
%P2 is the raw FFT data (needs to be FFTshifted)
%P1 is the positive frequency side only, but then is doubled to account for
%Power contributions from negative freq domain...
X        = fft((Data));
X_shift  = fftshift(fft((Data)));
P2    = abs(X/n); %Scaled FFT data
P1 = P2(1:n/2+1); %P1 is positive frequency half of data
P1(2:end-1) = 2*P1(2:end-1); %Double P1 amplitude to "add" negative frequency components
f = fs*(0:(n/2))/n; %Frequency vector
f_shift = (-n/2:n/2-1)*(fs/n);
P2_shift = abs(X_shift/n);

P1 = P1/max(P1);


subplot(3,1,2)
%Plot from 20Hz-20kHz
plot(f(3:2001),mag2db(P1(3:2001)))
subplot(3,1,3)
plot(f(3:2001),P1(3:2001))
%Index 250001 is f=0Hz for double-sided spectrum
%plot(f_shift(248001:252001),mag2db(P2_shift(248001:252001)))

%Now do calculations
    %1. Calculate Energy of Noise signal (Sum of Magnitude^2 * df)
E_N = sum(P1.^2)*10
