clc;
close all;
clear;

I = rgb2gray(imread('football.jpg'));
%figure,imshow(I);
[M,N,l] = size(I);
d0 = 100;
n = 1;
FI = fft2(I);
FI = fftshift(FI);
figure,imshow(real(FI));
lapl=[0,1,0;1,-4,1;0,1,0];
L=fft2(double(lapl),M,N);
L=fftshift(L);
figure,imshow(real(L));
%mask = cat(3,L,L,L);
filtered = FI.*L;
%filtered=filtered+(-1 * min(filtered(:)));
%figure;
%imshow(filtered);

filtered = ifftshift(filtered);
%figure,imshow(filtered);
final = (ifft2(filtered));
figure;
imshow(uint8(final));