# drawing colors with object color detection
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3,640) # width id number is 3
cap.set(4,480) # height id number is 4
cap.set(10,100) # brightness id number is 100

myColors = [[0,0,0,163,103,63],[149,25,68,179,183,201],[98,205,0,136,255,255]]
myColorValues = [[0,0,0],[229,204,255],[255,128,0]] #BGR format
myPoints = [] #x,y,colorID


def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        #cv2.imshow(str(color[1]), mask)
        x,y = getContours(mask)
        cv2.circle(imgResults, (x, y), 10, myColorValues[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200:
            #cv2.drawContours(imgResults, cnt, -1, (255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
            x , y , w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResults, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResults = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for newPoint in newPoints:
            myPoints.append(newPoint)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    cv2.imshow("Result", imgResults)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break