import cv2
import numpy as np

# get orginal image
orig = cv2.imread('test.png')
assert (orig is not None)

# show original 
#cv.ShowImage("orig", orig)

# blur a bit to remove higher frequency variation
blur = cv2.GaussianBlur(orig, (5,5), 0)
#blur = cv2.medianBlur(orig, 3)

cv2.imwrite('blur.png', blur)

# normalise RGB
b,g,r = cv2.split(blur)

#total = np.zeros((orig.height, orig.width, 3), np.uint8)
total = cv2.add(r,b);
total = cv2.add(total, g);

cv2.divide(r,total,r,255.0)
cv2.divide(g,total,g,255.0)
cv2.divide(b,total,b,255.0)

norm = cv2.merge((b,g,r))

cv2.imwrite('norm.png', norm)

# posterize simply with mean shift filtering
post = cv2.pyrMeanShiftFiltering(norm,20,30)

cv2.imwrite('post.png', post)

#pokemon go colors: light blue is 191H, 65S, 100B
# dark blue is 198, 100, 100
# sometimes B can be 97 or so
# red is 347h 100s 100b
# so maybe H from 175 to 212...
# photoshop uses 0-360H, 0-100S/B

hsv = cv2.cvtColor(post, cv2.COLOR_BGR2HSV)
lower_blue = np.array([175/2,50,50])
upper_blue = np.array([212/2,255,255])
masked = cv2.inRange(hsv, lower_blue, upper_blue)
cv2.imwrite("mask.png", masked)

bwimg = cv2.cvtColor(post,cv2.COLOR_BGR2GRAY)
cv2.imwrite('bw.png', bwimg)

#circles = cv2.HoughCircles(bwimg,cv2.HOUGH_GRADIENT,1.5,minDist=100,
#                            param1=50,param2=30,minRadius=5,maxRadius=0)

circles = cv2.HoughCircles(bwimg,cv2.HOUGH_GRADIENT,1.5,minDist=100, maxRadius=2000, param1=10, param2=100)
                            

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(post,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(post,(i[0],i[1]),2,(0,0,255),3)
cv2.imwrite('circles.png', post)
