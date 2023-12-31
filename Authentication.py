import  cv2
import numpy
import numpy as np
from pyzbar.pyzbar import decode
# img=cv2.imread('2.png')
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
with open('mtDatafile.text') as f:
    myDataList=f.read().splitlines()


while True:
    success,img=cap.read()
    for barcode in decode(img):
        mydata=barcode.data.decode('utf-8')
        print((mydata))
        if mydata in myDataList:
            myOutput='authorized'
            myColor=(0,0,255)
        else:
            myOutput='unauthorized'
            myColor = (0, 255, 255)
        pts=numpy.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2=barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)
    cv2.imshow('Result',img)
    cv2.waitKey(1)
