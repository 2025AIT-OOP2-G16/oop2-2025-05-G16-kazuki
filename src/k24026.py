import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

# lecture05_01.pyを変更してGoogleの検索画面の白色部分を
# Macのカメラキャプチャ画像に置き換えるクラス

def k24026():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    
    print("📸 カメラ起動中。'q' キーで撮影終了")
    # カメラ映像からリアルタイムに加工して、画像を表示
    app.run()
    app.write_img('images/camera_capture.png')  # 保存
    
    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') 

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                google_img[y, x] = capture_img[y % c_hight, x % c_width]
    # 書き込み処理
    cv2.imwrite('output_images/lecture05_01_k24026.png', google_img)