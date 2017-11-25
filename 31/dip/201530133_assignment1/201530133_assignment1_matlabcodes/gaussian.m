%% GAUSIAN FILTER
%% CODE:
    clear all;
    for color=1:3
        im= imread('gauss.jpg');
        im=im(:,:,color);
        sigma = 2;
        %figure;
        %imshow(im);
        k = 1/(2*pi*sigma*sigma);
        %k=1;
        ker_size = 8;
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
                final(i,j)=sum(Temp(:));
            end
         end
        %final = round(final./10000);
        %final = conv(im,window);
        figure;
        %subplot(1,2,1);
        %imshow(im);
        %subplot(1,2,2);
        %imshow(uint8(final));
        finalim(:,:,color)=uint8(final);
        %title(strcat('Kersize:', int2str(ker_size),'sigma: ',int2str(sigma)));
    end
    imshow(finalim);