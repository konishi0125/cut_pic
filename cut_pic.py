import os
import cv2
import numpy as np


def onMouse( event, x, y, flag, params ):
    global x_, y_, start_x, start_y, end_x, end_y, click_flag

    wname, img = params

    if event == cv2.EVENT_LBUTTONDOWN:
        if(click_flag == "first"):
            x_ = x
            y_ = y
            start_x = x
            start_y = y
            click_flag = "second"
        
        elif(click_flag == "second"):
            end_x = x
            end_y = y
            click_flag = "first"

    if event == cv2.EVENT_MOUSEMOVE:
        if(click_flag == "first"):
            img2 = np.copy( img )
            h, w = img2.shape[0], img2.shape[1]
            cv2.line( img2, ( x, 0 ), ( x, y+w ), ( 255, 0, 0 ) )
            cv2.line( img2, ( 0, y ), ( x+h, y ), ( 255, 0, 0 ) )
            cv2.imshow( wname, img2 )
        elif(click_flag == "second"):
            img2 = np.copy( img )
            h, w = img2.shape[0], img2.shape[1]
            cv2.line( img2, ( x_, y_ ), ( x, y_ ), ( 255, 0, 0 ) )
            cv2.line( img2, ( x_, y_ ), ( x_, y ), ( 255, 0, 0 ) )
            cv2.line( img2, ( x, y ), ( x, y_ ), ( 255, 0, 0 ) )
            cv2.line( img2, ( x, y ), ( x_, y ), ( 255, 0, 0 ) )
            cv2.imshow( wname, img2 )

    #if event == cv2.EVENT_LBUTTONDOWN:
    #    print ( x, y )

def resize_pic(img, max_lng):
    orgHeight, orgWidth = img.shape[:2]
    rate = max_lng/max([orgHeight, orgWidth])
    rsz_img = cv2.resize(img, None, fx=rate, fy=rate)

    return rsz_img


ok_list = []
ng_list = []  

path = ""
f_list = os.listdir(f'{path}/pic/')

f_num = 1
for f in f_list:
    wname = "hoge"
    cv2.namedWindow( wname )
    img = cv2.imread(f'{path}/pic/{f}')
    img = resize_pic(img, 512)

    x_ = 0
    y_ = 0
    click_flag = "first"
    cv2.setMouseCallback( wname, onMouse, [ wname, img ] )
    cv2.imshow( wname, img )

    # exit when ESC-key is pressed
    while cv2.waitKey( 0 ) != 10:
        pass

    if(x_ != 0 or y_ != 0):
        ok_path = f'{path}/ok/{f_num}.jpg'
        cv2.imwrite(ok_path, img)
        ok_list.append(f"{ok_path} 0 {start_x} {start_y} {end_x} {end_y}")
        f_num += 1

    cv2.destroyAllWindows()

out_list = '\n'.join(ok_list)
with open(f'{path}/ok/poslist.txt', 'wt') as f:
    f.write(out_list)