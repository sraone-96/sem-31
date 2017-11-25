i1 = imread('Assign4_imgs/restore_04.jpg');
%imshow(i1);

a = [290 313]; b = [314 322];
% estimates for length of motion blur
LEN = 25; THETA = -20; NSR = .03;
PSF = fspecial('motion', LEN, THETA);

restored = deconvwnr(i1, PSF, NSR);
%imshow(restored);
imwrite(restored, 'restored04.jpg');