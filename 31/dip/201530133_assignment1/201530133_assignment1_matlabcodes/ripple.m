%% RIPPLE TRANSFORM

%% CODE:
clear all;
im = imread('blur2.jpg');
[x,y,cl]=size(im);
ax = 10;
ay = 5;
tx=120;
ty=150;
for p=1:25
    for i=1:x
        for j=1:y
            a  = i + ax* sin((2*pi*j)/tx);
            b = j + ay*sin((2*pi*i)/ty);
            %newim(round(a)+ax,round(b)+ay) = im(i,j);
            
            w = min(x,round(a)+ax);
            s = min(y,round(b)+ay);
            newim(w,s,1)=im(i,j,1);
            newim(w,s,2)=im(i,j,2);
            newim(w,s,3)=im(i,j,3);
        end
    end
    ax=ax+3;
    ay=ay+4;
    tx=tx+5;
    ty=ty+3;
    filename='ripple1.gif';
    [A,map] = rgb2ind(uint8(newim),256);
    if p == 1
        imwrite(A,map,filename,'gif','LoopCount',Inf,'DelayTime',0.3);
    else
        imwrite(A,map,filename,'gif','WriteMode','append','DelayTime',0.3);
    end
end   
 newim=uint8(newim);
imshow(newim);
