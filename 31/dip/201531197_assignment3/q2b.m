clc;
clear; 
close all;
I=imread('Cricket4.jpeg');
I = rgb2gray(I);
I=double(I);
globalmean = mean(mean(mean(I(:,:,:))));
a=0.0085;b=1.265;
xwd=1;ywd=1;
k=3;
for i=1:size(I,1)-k
for j=1:size(I,2)-k
Itemp=I(i:i+2,j:j+2);
vxy=var(var(Itemp(:,:)));
Txy(j) = a*vxy+b*globalmean;
if(Txy(j)>255 && j~=1)
Txy(j)=Txy(j-1);
end
for s=1:3
for e=1:3

if Itemp(s,e)>Txy(j)
out(i+xwd,j+ywd) = 1;
else
out(i+xwd,j+ywd) = 0;
end

end
end
end
end

figure,imshow(out);
