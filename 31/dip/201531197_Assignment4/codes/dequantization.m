function [im] = dequantization(imq, quantMatrix, scale)
    % compute quantization matrix
    quantizationMatrix = scale*quantMatrix;
    % dequantize the IDCT image
    im = imq.*quantizationMatrix;
end