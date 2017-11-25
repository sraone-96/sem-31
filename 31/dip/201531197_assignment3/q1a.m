close all;
clear all;
im=imread('circle4.jpeg');
itest=im;
im=rgb2gray(im);
im=edge(im,'canny');
im=255*double(im);
imshow(uint8(im)); figure,

Threshold=180;

[M N]=size(im);

count=zeros(M,N,100);
r1=10;
r2=100;
for i=1:size(im,1)
for j=1:size(im,2)
if(im(i,j)==255)
for r=r1:r2
for angle=0:360
a=floor(i-r*cos(angle*pi/180));
b=floor(j-r*sin(angle*pi/180));
if(a>=1 && b>=1 && a<=M && b<=N)
count(a,b,r)=count(a,b,r)+1;
end
end
end
end
end
end

output=zeros(M,N);
k=1;
for i=1:M
for j=10:N
for r=1:100
if(count(i,j,r)>=Threshold)
for angle=0:360
a=floor(i-r*cos(angle*pi/180));
b=floor(j-r*sin(angle*pi/180));
if(a>=1 && b>=1 && a<=M && b<=N)
output(a,b)=255;
end
end
end
end
end
end
for i=1:size(itest,1)
for j=1:size(itest,2)
    if(itest(i,j)~=255)
    itest(i,j)=1;
    end
end
end
%output=output.*itest;
imshow(uint8(output));
                        


