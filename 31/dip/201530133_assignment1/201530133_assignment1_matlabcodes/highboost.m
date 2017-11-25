%% HIGH BOOST FILTERING

%% CODE:
clear all;
for color=1:3;
    im= imread('blur2.jpg');
    im=im(:,:,color);
    sigma = 1;
    lambda = 2;
    figure;
    imshow(im);
    k = 1/(2*pi*sigma*sigma);
    %k=1;
    ker_size = 5;
    mid=floor(ker_size/2);
    window = zeros(ker_size,ker_size);
    [x,y]=size(im);
    for i=1:ker_size
        for j=1:ker_size
            window(i,j)= k*exp(-1*(((i-mid-1)^2+(j-mid-1)^2)/(2*sigma*sigma)));
        end
    end
    %window = window.*265;
    %window = floor(window);
    padim =padarray(im,[mid,mid]);
    [x2,y2]=size(padim);
     for i = 1:x2-ker_size+1
        for j =1:y2-ker_size+1
            Temp = double(padim(i:i+ker_size-1,j:j+ker_size-1)).*window;
            gauss(i,j)=sum(Temp(:));
        end
     end
     subt = im - uint8(gauss);
    final =  im + lambda*subt;
    %final = round(final./10000);
    %final = conv(im,window);
    %figure;
    %imshow(uint8(final));
    newim(:,:,color)=uint8(final);
end
figure;
imshow(newim);