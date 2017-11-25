close all;
clear;
clc;
i=rgb2gray(imread('football.jpg'));
F= fft2(double(i));
figure,imshow(real(F));
H=zeros(size(F));
H=double(H);
D0=50;
for i=1:size(H,1)
    for j=1:size(H,2)
    D=sqrt((size(H,1)/2-i)^2 + (size(H,2)/2-j)^2);
    if(D<D0)
       %disp(D);
        H(i,j)=1;
    end
    end

end
figure,imshow((H));
FINAL=F.*H;
figure,imshow(real(FINAL));
FINAL=ifftshift(FINAL);
final=real(ifft2(FINAL));
figure,imshow(uint8(final));