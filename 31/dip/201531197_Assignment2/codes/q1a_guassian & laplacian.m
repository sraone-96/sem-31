close all;
clear;
clc;

srcFiles = dir('C:\Users\SRAVAN\Desktop\academics\dip\assignment2\Assign2_imgs\Assign2_imgs\image_blending_with_laplacian_pyramid\example1\*.jpg');
im1=strcat('C:\Users\SRAVAN\Desktop\academics\dip\assignment2\Assign2_imgs\Assign2_imgs\image_blending_with_laplacian_pyramid\example1\',srcFiles(1).name);
%im2=strcat('C:\Users\SRAVAN\Desktop\academics\dip\assignment2\Assign2_imgs\Assign2_imgs\image_blending_with_laplacian_pyramid\example1\',srcFiles(2).name);

i1=imread(im1);
%i2=imread(im2);

i1=double(i1);
%i2=double(i2);
g1=getgaussian(i1,4);
g1=uint8(255 * mat2gray(g1));
g1=double(g1);
l11=i1-g1;

i11=imresize(g1,0.75);

g2=getgaussian(i11,4);
g2=uint8(255 * mat2gray(g2));
g2=double(g2);

l12=i11-g2;

i12=imresize(g2,0.5);

g3=getgaussian(i12,4);
g3=uint8(255 * mat2gray(g3));
g3=double(g3);

l13=i12-g3;
i13=imresize(g3,0.75);

figure,imshow(uint8(l11)*10);
figure,imshow(uint8(l12)*10);
figure,imshow(uint8(l13)*10);

%figure,imshow(uint8(i11));
%figure,imshow(uint8(i12));
%figure,imshow(uint8(i13));
function G=getgaussian(image,k)
I=image;
sigma = k;
sz = 3;
[x,y]=meshgrid(-sz:sz,-sz:sz);
M = size(x,1)-1;
N = size(y,1)-1;
Exp_comp = -(x.^2+y.^2)/(2*sigma*sigma);
Kernel= exp(Exp_comp)/(2*pi*sigma*sigma);
Output=zeros(size(I));
%I = padarray(I,[sz sz]);
G=imfilter(I,Kernel);
%G=G(3:size(image,1)-2,3:size(image,2)-2);
end