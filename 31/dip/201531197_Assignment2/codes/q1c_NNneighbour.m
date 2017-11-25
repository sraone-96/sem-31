img=imread('lighthouse.png');
img=double(img);
img2=zeros(2*size(img,1),2*size(img,2),3);
img2=double(img2);
figure,imshow(uint8(img));
for i=1:size(img2,1)
for j=1:size(img2,2)
    if(rem(i,2)==1 & rem(j,2)==1)
        for k=1:3
    img2(i,j,k)=img(floor(i/2)+1,floor(j/2)+1,k);
        end
        end
end
end
%imshow(uint8(img2));

for i=1:2:size(img2,1)-2
for j=1:2:size(img2,2)-2
for k=1:3
    img2(i,j+1,k)=img2(i,j,k);
    img2(i+1,j,:)=img2(i,j,k);
    img2(i+1,j+1,k)=img2(i,j,k);
end
end
end


figure,imshow(uint8(img2));