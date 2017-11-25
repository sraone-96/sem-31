%% MEDIAN FILTERING

%% CODE:
clear all;
for color=1:3
    im= imread('gauss.jpg');
    im=im(:,:,color);
    %figure;
   % imshow(im);
    ker_size =8;
    mid=floor(ker_size/2);
    padim = padarray(im,[mid,mid]);
    [x2,y2] = size(padim);
    for i=1:x2-2*mid-1
        for j=1:y2-2*mid-1
            window = padim(i:i+ker_size-1,j:j+ker_size-1);
            temp = sort(window(:));
            val = temp(round((ker_size*ker_size)/2));
            newim(i,j)=val;
        end
    end
    %figure;
    %imshow(newim);
    final(:,:,color)=newim;
end
figure;
imshow(final);