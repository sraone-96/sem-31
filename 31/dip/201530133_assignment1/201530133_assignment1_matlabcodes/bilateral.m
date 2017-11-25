imgnf=imread(carpet_01_noflash.tif);
imgf=imread(carpet_00_flash.tif);
bifilter2(imgnf,imgf,15,5,0.35);

function pic = bifilter2( image1, image2, n, sigma1, sigma2)
pic=im2double(image1);
pic2=im2double(image2);
figure;
imshow(pic);
fsize = n;
sigma = sigma1;
sigma2=sigma2;
fsi = round(fsize/2)-1;
inds = -fsi : fsi;

picpad = padarray(pic2, [fsi fsi]);
picpadnoflash = padarray(pic, [fsi fsi]);
[ht,wid,pkh] = size(picpad);

ind = round(fsize / 2)-1;


for i = 1 + ind: ht - ind
    for j = 1 + ind: wid - ind
        box = picpad(i - ind: i + ind, j - ind: j + ind, :);
        boxnoflash = picpadnoflash(i - ind: i + ind, j - ind: j + ind, :);
        
        [X Y] = meshgrid(inds, inds);
        gf = exp(-(X.^2 + Y.^2) / (2*sigma*sigma));
        for eachcolor=1:3
            dl(:,:,eachcolor)=box(:,:,eachcolor) - picpad(i,j,eachcolor);
        end
        
        dL = box(:,:,1) - picpad(i,j,1);
        H = exp(-(dl(:,:,1).^2+dl(:,:,2).^2+dl(:,:,3).^2)/(2*sigma2^2));
        
        for eachcolor=1:3
            temp(:, :, eachcolor) = box2(:, :, eachcolor) .* H;
        end
        
        for eachcolor=1:3
            temp(:, :, eachcolor) = temp(:, :, eachcolor) .* gf;
        end
        
        for eachcolor=1:3
            temp(eachcolor) = sum(sum(temp(:, :, eachcolor)));
        end

        norm = gf .* H;
        norm = sum(sum(norm(:)));
        for eachcolor=1:3
            pic(i, j, eachcolor) = temp(eachcolor)/norm;
        end
    
    end
end
size(pic);
size(image1);
end