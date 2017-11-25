clear;
close all;
clc;
i=imread('Cricket4.jpeg');
%imshow(i);
%{
cform = makecform('srgb2lab');
lab_he = applycform(i,cform);
%imshow(lab_he)

ab = double(lab_he(:,:,2:3));
nrows = size(i,1);
ncols = size(i,2);
ab = reshape(ab,nrows*ncols,2);
%imshow(ab);
%}
nrows = size(i,1);
ncols = size(i,2);
ab=double(reshape(i,nrows*ncols,3));
nColors=3;
iters=150;
%initial_cluster_centers  = random_initialization( ab, nColors );
randidx = randperm(size(ab, 1));
initial_cluster_centers = ab(randidx(1:nColors), :);

[unnecessary, cluster_center,cluster_idx] = run_KMeans(ab,initial_cluster_centers,iters);

for i=1:size(cluster_idx,1)
    if(cluster_idx(i)==2)
    cluster_idx(i)=255;
    else
        cluster_idx(i)=0;
    end
end

pixel_labels = uint8(reshape(cluster_idx,nrows,ncols));
%pixel_labels=pixel_labels/max(pixel_labels(:))
%pixel_labels=255-pixel_labels;
imshow(pixel_labels);
