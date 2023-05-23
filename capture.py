import cv2 as cv 
import time

SAVE_PATH = r"./"
DELAY_TIME = 0.5



if __name__ == '__main__':
    cap = cv.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        
        cv.imshow("video", frame)

        img_name = str(time.time()) + ".jpg"
        cv.imwrite(img_name, frame)

        if cv.waitKey(1) == ord('q'):
            break
        
    cap.release()
    cv.destroyAllWindows()