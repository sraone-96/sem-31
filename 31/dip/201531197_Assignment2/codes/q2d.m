clc;
close all;
clear;

I = imread('notch1.png');
%I=uint8(I);
%figure,imshow(I);
[M,N] = size(I);
d0 = 100;
n = 1;
k=2;
FI = fft2(I);
FI = fftshift(FI);
figure,imshow(real(FI));
for i=1:M
    for j=1:N
        for k=-1:1
   %if(j==136+k || j==186+k || (i==79+k & j==171+k) || (i==178+k & j==150+k)|| (j==161))
    %if ((j==161) || (i==80+k & j==137+k) || (i==79+k & j==171+k) || (i==178+k & j==50+k) || (i==178+k & j==186+k))
   if( (i==79+k & (j>115 & j<206))||(i==178+k & (j>110 & j<220))|| (j==161 & (i<101 || i>145)) || (j==136+k & (i>45 & i<115)) || (j==171+k & (i>45 & i<115))  ||  (j==186+k & (i>134 & i<224)) || (j==151+k & (i<224 & i>142)))
    FI(i,j)=0; 
   end
   end
    end
end

figure,imshow(real(FI));

filtered = ifftshift(FI);
%figure,imshow(filtered);
final = real(ifft2(filtered));
final=uint8(final);
figure;
imshow((final));