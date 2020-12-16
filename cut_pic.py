import os
import cv2
import numpy as np


#切り出す座標を決定する
def decide_coordinate( event, x, y, flag, params ):
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


#切り出しのため画像のリサイズ
def resize_pic(img, max_lng):
    orgHeight, orgWidth = img.shape[:2]
    rate = max_lng/max([orgHeight, orgWidth])
    rsz_img = cv2.resize(img, None, fx=rate, fy=rate)

    return rsz_img, rate


ok_list = []
ng_list = []

f_list = os.listdir(f"./input_pic/")

for f in f_list:
    wname = "hoge"
    cv2.namedWindow( wname )
    img = cv2.imread(f"./input_pic/{f}")
    #描画のため長辺512ピクセルに変換
    img, rate = resize_pic(img, 512)

    x_ = 0
    y_ = 0
    click_flag = "first"
    cv2.setMouseCallback( wname, decide_coordinate, [ wname, img ] )
    cv2.imshow( wname, img )
    cv2.waitKey( 0 )

    if(x_ != 0 or y_ != 0):
        ok_list.append(f"{f},{int(start_x/rate)},{int(start_y/rate)},{int(end_x/rate)},{int(end_y/rate)}")
    else:
        ng_list.append(f)

    cv2.destroyAllWindows()

out_ok_list = "\n".join(ok_list)
with open(f"./result/ok.csv", "wt") as f:
    f.write(out_ok_list)
out_ng_list = "\n".join(ng_list)
with open(f"./result/ng.csv", "wt") as f:
    f.write(out_ng_list)