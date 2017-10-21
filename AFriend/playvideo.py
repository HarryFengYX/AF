import numpy as np
import cv2
def main():
    cap = cv2.VideoCapture('Landscapes - Volume 4K (UHD)-9ZfN87gSjvI.mp4')
    
    while(True):
        ret, frame = cap.read()
        rows,cols,ch = frame.shape
        FX = 1920/cols
        FY = 1080/rows
        res = cv2.resize(frame,None,fx=FX, fy=FY, interpolation = cv2.INTER_CUBIC)
        cv2.imshow('frame',res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()