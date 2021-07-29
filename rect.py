import cv2
from PIL import Image
import PIL.ImageOps
import numpy as np
cap= cv2.VideoCapture(0)
while(True):
    try:
        rect,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #qprint(gray.shape)
        height,width=gray.shape
        upper_left=(int(width/2-56),int(height/2-56))

        bottom_right=(int(width/2+56),int(height/2+56))
        cv2.rectangle(gray,upper_left,bottom_right,(0,255,0),3)
        roi=gray[upper_left[1]:bottom_right[1],upper_left[0]:bottom_right[0]]
        #print(roi)
        image_pil=Image.fromarray(roi)

        im_btw=image_pil.convert("L")

        im_btw_resized= im_btw.resize((28.28),Image.ANTIALIAS)
        
        print(im_btw_resized)
        
        im_btw_resized_inverted=PIL.ImageOps.invert(im_btw_resized)
        print(im_btw_resized_inverted)
        pixel_filter=20
        maxpixel_filter=mp.percentile(im_btw_resized_inverted,pixel_filter)
        print(image_pil)

        cv2.imshow("Digit",gray)
        
        if(cv2.waitKey(1)==ord("q")):
            break

    except:
        pass
        
cap.release()        
cv2.destroyAllWindows()


        
