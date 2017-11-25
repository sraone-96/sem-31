img=imread('parabola3.jpg');
I=rgb2gray(img);
[N,M]=size(I);
[E,thresh]=edge(I,'canny',0.35);

rtrain = [0.003,0.004,0.005,0.006,0.007,0.008];

R=6;
counter=zeros(N,M,R);
[yindex xindex]=find(E);

for index=1:length(xindex)
    for r=1:R
    for x0=1:M
    y0=yindex(index)-rtrain(r)*(xindex(index)-x0)^2;
    y0=round(y0);
    if y0< N & y0>=1
        counter(y0,x0,r) = counter(y0,x0,r)+1;
    end
    end
    end
end

Ar=max(counter,[],3);

SE=strel('disk',40);

countmax=imdilate(Ar,SE);

thresh=90;

ydetect = [];
xdetect= [];
rdetect= [];

for r=1:R
    [y0 x0]=find((countmax(:,:) == counter(:,:,r)) & counter(:,:,r) > thresh);
    ydetect=[ydetect; y0];
    xdetect=[xdetect; x0];
    rdetect=[rdetect; rtrain(r)*ones(length(x0),1)];
end
i2=img;
for i=1:size(img,1)
    for j=1:size(img,2)
    i2(size(img,1)-i+1,size(img,2)-j+1,:)=img(i,j,:);
    end
end
%imshow(i2);


imshow(E,[]),title('Parabola Detection');

for i=1:length(xdetect)
    x0=xdetect(i);
    y0=ydetect(i);
    r0=rdetect(i);
    for x=1:M
        y=round(y0+r0*(x-x0)^2);
        if y<=N & y>=1
            rectangle('Position',[x y 1 1],'Edgecolor','r');
        end
    end
end








