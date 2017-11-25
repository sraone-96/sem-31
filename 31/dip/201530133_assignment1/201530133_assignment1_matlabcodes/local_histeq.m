%% LOCAL HISTOGRAM EQUALISATION
%% Code:

clear all;
im = imread('histeq_net2.jpg');
%im = rgb2gray(im);
no_of_bins = 256;
[x1,y1] = size(im);
mat_len = 100; 
mat_wid = 100; 
mid_val = round(mat_len*mat_wid/2);
mid_val_len = floor(mat_len/2);
mid_val_wid = floor(mat_wid/2);
padim = padarray(im, [mid_val_len,mid_val_wid]);
[x2,y2] = size(padim);
%imshow(padim);

for i=1:(x2-2*mid_val_len-1)
    for j = 1:(y2-2*mid_val_wid-1)
        
        inc=1;
        window = padim(i:i+mat_len-1,j:j+mat_wid-1);
        cdf =imhist(window);
        cdf=cumsum(cdf);
        newimg(i,j) = round(cdf(window(mid_val_len,mid_val_wid)+1)/(mat_len*mat_wid)*255);
%         for k=0:mat_len-1
%             for l=0:mat_wid-1
%                 if(inc== mid_val)
%                     ele = padim(i+k-1,j+l-1)+1;
%                 end
%                     pixel = padim(i+k,j+l)+1;
%               %  l=l+1;
%                     cdf(pixel) = cdf(pixel) + 1;
%                     inc=inc+1;
%             end
%             %k=k+1;
%         end
%         %cumulative = zeros(1,256);
%         %display(cumulative);
%         %cumulative(1)=pdf(1);       
%         for p=2:256
%             cdf(p) = cdf(p) + cdf(p-1);  
%         end
%         %cumulative = cumulative./(mat_len*mat_wid);
%         %cumulative = cumulative.*256;
%         %cumulative = round(cumulative);
%         %newimg(i,j)=cumulative(padim(i+mid_val_len,j+mid_val_wid)+1);
%         newimg(i,j) = round(cdf(ele)/(mat_len*mat_wid)*255);
%         % j=j+1;
    end
    %i=i+1;
end

%% Input Image
figure;
subplot(1,2,1);
imshow(im);

%% Output Image
%figure;
subplot(1,2,2);
imshow(uint8(newimg));
        



