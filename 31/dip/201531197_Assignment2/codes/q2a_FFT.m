clc;
clear all;
close all;
Im = imread('football.jpg');
Im = rgb2gray(Im);
figure,
imshow(Im);

Mx = size(Im,1);
Ny = size(Im,2);

M1 = 2^(ceil(log2(Mx)));
N1 = 2^(ceil(log2(Ny)));

F = zeros(M1,N1);
F(1:Mx,1:Ny) = Im;
Im2 = zeros(M1,N1);
Im2 = transpose(F);

for i=1:M1
    A = myFFT(Im2(1:N1,i));
    C(i,1:N1) = transpose(A);    
end
F1_new = C;
F3 = zeros(M1,N1);
for i=1:Mx
    for j=1:N1
        F3(i,j) = F1_new(i,j);
    end
end
F3_new = zeros(M1,N1);
for j=1:N1
    F3_new(:,j) = myFFT(F3(:,j));
end
figure;
imshow(F3_new);
J = ifft2(ifftshift(F3_new));
final = zeros(Mx,Ny);
for i=1:Mx
    for j=1:Ny
        final(i,j) = J(i,j);
    end
end

figure,imshow(uint8(abs(final)));
title('final output');