im = imread('hist_equal.jpg');
im = rgb2gray(im);
im2= rgb2gray(imread('hist_equal2.jpg'));
cdf2 = cumsum(imhist(im2))/numel(im2);
cdf = cumsum(imhist(im))/numel(im);
%display(cdf);
%display(numel(im));
figure;
%subplot(4,1,1);
%imshow(im);
%subplot(4,1,2);
%imhist(im);
%subplot(4,1,3);
%stem(cdf);
M= zeros(256);

for idx = 1:256
   %  display(idx);
   %  display('\n');
    % display(cdf(idx));
    % display('\n');
     %display(cdf(idx) - cdf2);
    % display('cdf2 \n');
  %   display(cdf2);
      [~,ind] = min(abs(cdf(idx) - cdf2));
          M(idx) = ind-1;
          
end
%subplot(4,1,4);
stem(M(double(im)+1));