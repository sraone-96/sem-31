i1 = imread('Assign4_imgs/restore_02.jpg');
%imshow(i1);

% estimates for length of motion blur
a = [855 797]; b = [703 721]; c = a-b;

LEN = 23; THETA = 0; NSR = .03;
PSF = fspecial('motion', LEN, THETA);

restored = deconvwnr(i1, PSF, NSR);
%imshow(restored);
imwrite(restored, 'restored02.jpg');
