function [imq] = quantization(im, quantMatrix, scale)
    % compute quantization matrix
    quantizationMatrix = scale*quantMatrix;
    % apply quantization on the DCT matrix
    imq = im./quantizationMatrix;
    % round the quantized image
    imq = round(imq);
end