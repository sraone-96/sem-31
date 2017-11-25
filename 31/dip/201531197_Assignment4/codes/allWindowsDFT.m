function [R, mse] = allWindowsDFT(image, scale)
    clc;
   
    I = imread(image);
    
    classicalQuantization
   
    [rows, cols] = size(I);
   
    R = ones(size(I));
   
    rows = rows/8;
    cols = cols/8;
    i = 1;
        for u = 1:rows
        j = 1;
        for v = 1:cols
            J = I(i:i+7,j:j+7);
            FD = dct2(J);
            imq = quantization(FD, Q, scale);
            im = dequantization(imq, Q, scale);
            
            cim = idct2(im);
            R(i:i+7,j:j+7) = cim;
            j = j+8;
        end
        i = i+8;
    end
    subplot(1, 2, 1)
    imshow(uint8(I))
    subplot(1, 2, 2)
    imshow(uint8(R))
end