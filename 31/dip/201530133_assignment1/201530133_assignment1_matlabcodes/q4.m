%% STEREO MATCHING

%% CODE:
im = imread('stereo_pair.jpg');
imsize = size(im);

firsthalf = im(:, 1:round(imsize(2) / 2)-1, :);
secondhalf = im(:, round(imsize(2) / 2):end, :);
firstgray = rgb2gray(firsthalf);
secondgray = rgb2gray(secondhalf);
firstfeatures = detectHarrisFeatures(firstgray);
[features1,valid_points1] = extractFeatures(firstgray,firstfeatures);
secondfeatures = detectHarrisFeatures(secondgray);
[features2,valid_points2] = extractFeatures(secondgray,secondfeatures);
indexPairs = matchFeatures(features1,features2);
matchedPoints1 = valid_points1(indexPairs(:,1),:);
matchedPoints2 = valid_points2(indexPairs(:,2),:);
figure;
subplot(1,2,1);
showMatchedFeatures(firstgray,secondgray,matchedPoints1,matchedPoints2);
match1 = matchedPoints1.Location;
[x,y]= size(match1);
match2 = matchedPoints2.Location;

[x,y] = size(match2);
match1 = reshape(match1, [2 x]);

match2 = reshape(match2, [2 x]);

v = homography_solve(match1, match2);

imp = secondhalf;
for i=1:size(firsthalf, 1)
    for j=1:size(firsthalf, 2)
        p = [i j 1]';
        ppn = v * p;
        ppn = floor(ppn ./ ppn(3))+1;
        for o=1:2
            ppn(o) = min(max(ppn(o), 1), size(secondhalf, o));
        end
        imp(ppn(1), ppn(2), :) = firsthalf(p(1), p(2), :);
    end
end
subplot(1,2,2);
imshow(imp - secondhalf);