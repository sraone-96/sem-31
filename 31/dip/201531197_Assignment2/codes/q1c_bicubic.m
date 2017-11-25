clear;
close all;
clc;
i=imread('football.jpg');
k=2;
final=bicubic(i,k*size(i,1),k*size(i,2)); 
figure,imshow(uint8(final));
k=3;
final=bicubic(i,k*size(i,1),k*size(i,2));
figure,imshow(uint8(final));


function output_image = bicubic( input_image,xdim,ydim)  
I = input_image; 
I = double(rgb2gray(I));
[j k] = size(I);
x_new = xdim;
y_new = ydim;
 
x_scale = x_new./(j-1);
y_scale = y_new./(k-1);
temp_image = zeros(x_new,y_new);
Ix = double(zeros(j,k));
Iy = double(zeros(j,k));
Ixy = double(zeros(j,k));

Ix=getxd(I,j,k);
Iy=getyd(I,j,k);
Ixy=getxyd(I,j,k);

for count1 = 0:x_new-1
 for count2 = 0:y_new-1
 W = -(((count1./x_scale)-floor(count1./x_scale))-1);
 H = -(((count2./y_scale)-floor(count2./y_scale))-1);
 I11_index = [1+floor(count1./x_scale),1+floor(count2./y_scale)];
 I21_index = [1+floor(count1./x_scale),1+ceil(count2./y_scale)];
 I12_index = [1+ceil(count1./x_scale),1+floor(count2./y_scale)];
 I22_index = [1+ceil(count1./x_scale),1+ceil(count2./y_scale)];
 I11 = I(I11_index(1),I11_index(2));
 I21 = I(I21_index(1),I21_index(2));
 I12 = I(I12_index(1),I12_index(2));
 I22 = I(I22_index(1),I22_index(2));
 Ix11 = Ix(I11_index(1),I11_index(2));
 Ix21 = Ix(I21_index(1),I21_index(2));
 Ix12 = Ix(I12_index(1),I12_index(2));
 Ix22 = Ix(I22_index(1),I22_index(2));
 Iy11 = Iy(I11_index(1),I11_index(2));
 Iy21 = Iy(I21_index(1),I21_index(2));
 Iy12 = Iy(I12_index(1),I12_index(2));
 Iy22 = Iy(I22_index(1),I22_index(2));
 Ixy11 = Ixy(I11_index(1),I11_index(2));
 Ixy21 = Ixy(I21_index(1),I21_index(2));
 Ixy12 = Ixy(I12_index(1),I12_index(2));
 Ixy22 = Ixy(I22_index(1),I22_index(2));
 beta = [I11 I21 I12 I22 Ix11 Ix21 Ix12 Ix22 Iy11 Iy21 Iy12 Iy22 Ixy11 Ixy21 Ixy12 Ixy22];
 M_inv = [
 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0;
 0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0;
 -3,3,0,0,-2,-1,0,0,0,0,0,0,0,0,0,0;
 2,-2,0,0,1,1,0,0,0,0,0,0,0,0,0,0;
 0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0;
 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0;
 0,0,0,0,0,0,0,0,-3,3,0,0,-2,-1,0,0;
 0,0,0,0,0,0,0,0,2,-2,0,0,1,1,0,0;
 -3,0,3,0,0,0,0,0,-2,0,-1,0,0,0,0,0;
 0,0,0,0,-3,0,3,0,0,0,0,0,-2,0,-1,0;
 9,-9,-9,9,6,3,-6,-3,6,-6,3,-3,4,2,2,1;
 -6,6,6,-6,-3,-3,3,3,-4,4,-2,2,-2,-2,-1,-1;
 2,0,-2,0,0,0,0,0,1,0,1,0,0,0,0,0;
 0,0,0,0,2,0,-2,0,0,0,0,0,1,0,1,0;
 -6,6,6,-6,-4,-2,4,2,-3,3,-3,3,-2,-1,-2,-1;
 4,-4,-4,4,2,2,-2,-2,2,-2,2,-2,1,1,1,1
 ];
 alpha = M_inv*beta';
 temp_p=0;
 
 for counts = 1:16
 w_temp = floor((counts-1)/4);
 h_temp = mod(counts-1,4);
 temp_p = temp_p + alpha(counts).*((1-W)^(w_temp)).*((1-H)^(h_temp));
 end
 temp_image(count1+1,count2+1)=temp_p;
 end
end

output_image = temp_image;
end

function Ix=getxd(I,j,k)

for row = 1:j
 for col = 1:k
 if( (col==1) || (col==k) )
 Ix(row,col)=0;
 else
 Ix(row,col)=(0.5).*(I(row,col+1)-I(row,col-1));
 end
 end
end

end
function Iy=getyd(I,j,k)
for row = 1:j
 for col = 1:k
 if( (row==1) || (row==j) )
 Iy(row,col)=0;
 else
 Iy(row,col)=(0.5).*(I(row+1,col)-I(row-1,col));
 end
 end
end
end

function Ixy=getxyd(I,j,k)

for row = 1:j
 for col = 1:k
 if( (row==1) || (row==j) || (col==1) || (col==k) )
 Ixy(row,col)=0;
 else
 Ixy(row,col)=(0.25).*((I(row+1,col+1)+I(row-1,col-1)) - (I(row+1,col-1)+I(row-1,col+1)));
 end
 end
end
end