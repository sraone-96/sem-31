close all;
clear;
clc;

srcFiles = dir('C:\Users\SRAVAN\Desktop\academics\dip\assignment2\Assign2_imgs\Assign2_imgs\image_blending_with_laplacian_pyramid\example3\*.png');
im1=strcat('C:\Users\SRAVAN\Desktop\academics\dip\assignment2\Assign2_imgs\Assign2_imgs\image_blending_with_laplacian_pyramid\example3\',srcFiles(1).name);
im2=strcat('C:\Users\SRAVAN\Desktop\academics\dip\assignment2\Assign2_imgs\Assign2_imgs\image_blending_with_laplacian_pyramid\example3\',srcFiles(2).name);
%srcFiles = dir('C:\Users\SRAVAN\Desktop\academics\dip\assignment2\Assign2_imgs\Assign2_imgs\image_blending_with_laplacian_pyramid\example1\*.jpg');
im3=strcat('C:\Users\SRAVAN\Desktop\academics\dip\assignment2\Assign2_imgs\Assign2_imgs\image_blending_with_laplacian_pyramid\example3\',srcFiles(3).name);

%figure,imshow(im1);
%figure,imshow(im2);
%figure,imshow(im3);
temp=30;
i1=imread(im1);
i2=imread(im2);
mask=imread(im3);

%figure,imshow(i1);
%figure,imshow(i2);
%figure,imshow((uint8(mask)));
mask=im2double(mask);
i1=double(i1);
i2=double(i2);
sigma=50;
mask=imgaussfilt(mask,sigma);
%figure,imshow(uint8(mask));
%G=fspecial('gaussian',[50,50],30);
%mask=imfilter(mask,G);
%figure,imshow(mask);
%figure,imshow(i1);
%figure,imshow(i2);
Itemp1=imresize(i1,0.25);
Itemp2=imresize(i2,0.25);
mask1=imresize(mask,0.25);

%subplot(1,2,1),
%imshow(uint8(mask1));
I1=Itemp1;
I2=Itemp2;
for i=1:size(I1,1)
for j=1:size(I1,2)
    for k=1:3
  I1(i,j,k)=Itemp1(i,j,k).* mask1(i,j);
    end
end
end
for i=1:size(I2,1)
for j=1:size(I2,2)
    for k=1:3
  I2(i,j,k)=Itemp2(i,j,k).* (1-mask1(i,j));
    end
end
end
f1=I1+I2;
figure,imshow(uint8(f1));

Itemp21=imresize(i1,0.5);
Itemp22=imresize(i2,0.5);
mask21=imresize(mask,0.5);
%subplot(1,2,2),
%imshow(mask21);
Itemp21=getlaplacian(Itemp21,temp);
Itemp22=getlaplacian(Itemp22,temp);
%figure,imshow(Itemp21);
%figure,imshow(Itemp22);

I21=Itemp21;
I22=Itemp22;
%size(I21)
for i=1:size(Itemp21,1)
for j=1:size(Itemp21,2)
    for k=1:3
  I21(i,j,k)=Itemp21(i,j,k).* mask21(i,j);
    end
end
end
for i=1:size(Itemp22,1)
for j=1:size(Itemp22,2)
    for k=1:3
  I22(i,j,k)=Itemp22(i,j,k).* (1-mask21(i,j));
    end
end
end
f2=I21+I22;

f2=f2+(imresize(f1,[size(f2,1),size(f2,2)]));
figure,imshow(uint8(f2));

Itemp31=imresize(i1,0.75);
Itemp32=imresize(i2,0.75);
mask31=imresize(mask,0.75);
%figure,imshow(mask31);
Itemp31=getlaplacian(Itemp31,temp);
Itemp32=getlaplacian(Itemp32,temp);
I31=Itemp31;
I32=Itemp32;
for i=1:size(Itemp31,1)
for j=1:size(Itemp31,2)
    for k=1:3
  I31(i,j,k)=Itemp31(i,j,k).* mask31(i,j);
    end
end
end
for i=1:size(Itemp32,1)
for j=1:size(Itemp32,2)
    for k=1:3
  I32(i,j,k)=Itemp32(i,j,k).* (1-mask31(i,j));
    end
end
end
f3=I31+I32;
f3=f3+(imresize(f2,[size(f3,1),size(f3,2)]));
figure,imshow(uint8(f3));


Itemp41=imresize(i1,1);
Itemp42=imresize(i2,1);
mask41=imresize(mask,1);
%figure,imshow(mask41);
Itemp41=getlaplacian(Itemp41,temp);
Itemp42=getlaplacian(Itemp42,temp);
I41=Itemp41;
I42=Itemp42;
for i=1:size(Itemp41,1)
for j=1:size(Itemp41,2)
    for k=1:3
  I41(i,j,k)=Itemp41(i,j,k).* mask41(i,j);
    end
end
end
for i=1:size(Itemp42,1)
for j=1:size(Itemp42,2)
    for k=1:3
  I42(i,j,k)=Itemp42(i,j,k).* (1-mask41(i,j));
    end
end
end
f4=I41+I42;
f4=f4+(imresize(f3,[size(i1,1),size(i1,2)]));
figure,imshow(uint8(f4));


function final=getlaplacian(image,k)
G=fspecial('gaussian',[5,5],k);
final=image-imfilter(image,G);
%figure,imshow(final);
end