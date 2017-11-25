%% SPHERICAL TRANSFORM

%% CODE:
clear all;
im = imread('gauss.jpg');
figure;
imshow(im);
[x,y,cl]=size(im);
xc = floor(x/2);
yc = floor(y/2);
rmax = floor(x/2);
r_index = 2.2;

for p=1:25
    newim = im;
    for i=1:x
        for j=1:y
            
            dx = i-xc;
            dy = j-yc;
            r= sqrt(dx*dx + dy*dy);
            z = sqrt(rmax^2 - r^2);
            betax=0;
            betay=0;
            if(r~=0 && z~=0)
                betax= (1-(1/r_index))*asin(dx/(sqrt(dx^2 + z^2)));
                betay = (1-(1/r_index))*asin(dy/(sqrt(dy^2 + z^2)));
            end
            a=i;
            b=j;
            if(r<=rmax)
                a = i-z*tan(betax);
                b = j-z*tan(betay);
            end
            w = min(x,round(a));
            s = min(y,round(b));
            newim(w,s,1)=im(i,j,1);
            newim(w,s,2)=im(i,j,2);
            newim(w,s,3)=im(i,j,3);
        end
    end
    r_index = r_index-0.07;
    rmax = rmax - 10;
    %imwrite('GIF','spherical.gif');
    %frame = getframe(1);
    %ima{p} = uint8(newim);
    filename='spherical2.gif';
    [A,map] = rgb2ind(uint8(newim),256);
    if p == 1
        imwrite(A,map,filename,'gif','LoopCount',Inf,'DelayTime',0.3);
    else
        imwrite(A,map,filename,'gif','WriteMode','append','DelayTime',0.3);
    end
end
filename = 'testAnimatedspherical.gif'; % Specify the output file name
%for idx = 1:25
    
%end
newim=uint8(newim);
%imshow();