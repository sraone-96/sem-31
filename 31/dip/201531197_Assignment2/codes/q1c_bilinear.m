clear;
close all;
clc;
im=imread('lighthouse.png');
figure,imshow(im);
i2=zeros(2*size(im,1),2*size(im,2),3);
im=double(im);
i2=double(i2);
for i=1:size(i2,1)
for j=1:size(i2,2)
    if(rem(i,2)==1 & rem(j,2)==1)
        for k=1:3
    i2(i,j,k)=im(floor(i/2)+1,floor(j/2)+1,k);
        end
        end
end
end
%imshow(uint8(i2));
for i=1:2:size(i2,1)
for j=2:2:size(i2,2)
    %if(rem(i,2)==1 & rem(j,2)==1)
       if(j==size(i2,2))
        for k=1:3
            i2(i,j,k)=i2(i,j-1,k);
        end
       else
            for k=1:3
          i2(i,j,k)=(i2(i,j-1,k)+i2(i,j+1,k))/2;
            end
       end
end
end
for i=2:2:size(i2,1)
for j=1:2:size(i2,2)
    %if(rem(i,2)==1 & rem(j,2)==1)
       if(i==size(i2,1))
        for k=1:3
    i2(i,j,k)=i2(i-1,j,k);
        end
       else
            for k=1:3
          alpha=floor( (i2(i-1,j,k)+i2(i+1,j,k) )/2);
          i2(i,j,k)=alpha;
            end
       end
end
end


for i=2:2:size(i2,1)-2
for j=2:2:size(i2,2)-2
    if(rem(i,2)==0 & rem(j,2)==0)
       %if(i==size(i2,1))
        for k=1:3
    i2(i,j,k)=floor((i2(i,j-1,k)+i2(i,j+1,k))/2);
        end
              end
end
end
figure,imshow(uint8(i2));