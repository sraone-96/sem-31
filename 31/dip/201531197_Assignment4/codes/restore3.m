[i1, map] = imread('Assign4_imgs/restore_03.gif');
i1 = ind2rgb(i1, map);
%imshow(i1);

a = [200 45]; b= [214 35];
% estimates for length of motion blur
LEN = 20; THETA = 35; NSR = .0275;
PSF = fspecial('motion', LEN, THETA);

restored = deconvwnr(i1, PSF, NSR);
imshow(restored);
imwrite(restored, 'restored03.jpg');