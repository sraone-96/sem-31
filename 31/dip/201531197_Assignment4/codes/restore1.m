i1 = imread('Assign4_imgs/restore_01.jpg');
%imshow(log(1+abs(fftshift(fft2(i1)))), []);

% estimates for length of motion blur
LEN = 30; THETA = 0; NSR = .0275;
PSF = fspecial('motion', LEN, THETA);

restored = deconvwnr(i1, PSF, NSR);
imwrite(restored, 'restored01.jpg');