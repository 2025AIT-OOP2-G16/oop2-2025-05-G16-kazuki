import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    # capture_img : cv2.Mat = "implement me"

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):

            #切り返しをしたい
            #Mod演算を使う？
            b1, g1, r1 = google_img[y, x]
            b2, g2, r2 = capture_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b1, g1, r1) == (255, 255, 255):
                pass
                google_img[y, x] = (b2, g2, r2)

    app.write_img('output_images/lecture05_01_K24113.png')

