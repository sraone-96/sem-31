clc;
close all;
clear;
I = imread('football.jpg');
M = size(I,1);
N = size(I,2);
d0 = 10;
n = 1;
%figure;
%imshow(I);
FI = fft2(I);
FI = fftshift(FI);
%figure;
%imshow(FI);
q = zeros(M,N);
for i = 1:M
    for j = 1:N
        dis = (((i - M/2)^2) + (j - N/2)^2)^(1/2);
       
        q(i,j) = exp(-((dis^2)/(2*((d0)^2))));
    end
end
mask = cat(3,q,q,q);
filtered = FI.*mask;
%figure;
%imshow(filtered);
filtered = ifftshift(filtered);
final = real(ifft2(filtered));
figure;
imshow(uint8(final));