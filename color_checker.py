import cv2
import numpy as np
import os

def colourMatrix(filename):
    original = cv2.imread(filename)
    imageFrame = cv2.imread(filename)

    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    #Red color boundries and mask
    red_lower1 = np.array([0, 50, 20], np.uint8)
    red_upper1 = np.array([10, 255, 255], np.uint8)
    red_lower2 = np.array([170, 50, 20], np.uint8)
    red_upper2 = np.array([180, 255, 255], np.uint8)
    red_mask1 = cv2.inRange(hsvFrame, red_lower1, red_upper1)
    red_mask2 = cv2.inRange(hsvFrame, red_lower2, red_upper2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    #Green color boundries and mask
    green_lower = np.array([38, 50, 20], np.uint8)
    green_upper = np.array([70, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    #Blue color boundries and mask
    blue_lower = np.array([98, 50, 20], np.uint8)
    blue_upper = np.array([125, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    #Yellow color boundries and mask
    yellow_lower = np.array([20, 50, 20], np.uint8)
    yellow_upper = np.array([35, 255, 255], np.uint8)
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

    #White color boundries and mask
    white_lower = np.array([0, 0, 239], np.uint8)
    white_upper = np.array([178, 52, 255], np.uint8)
    white_mask = cv2.inRange(hsvFrame, white_lower, white_upper)

    squares = []

    #Finding red coloured squares
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 1200):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            square = ['r',x,y]
            squares.append(square)
            #cv2.putText(imageFrame, "Red", (x/2, y/2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)    


    #Finding green coloured squares
    contours, hierarchy = cv2.findContours(green_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]
        
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 900):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),  (x + w, y + h),(0, 255, 0), 2)
            square = ['g',x,y]
            squares.append(square)
            #cv2.putText(imageFrame, "Green Colour", (x, y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))


    #Finding blue coloured squares
    contours, hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h),(255,0,0), 2)
            square = ['b',x,y]
            squares.append(square)
            #cv2.putText(imageFrame, "Blue Colour", (x, y),cv2.FONT_HERSHEY_SIMPLEX,1.0, (255, 0, 0))

    #Finding yellow coloured squares
    contours, hierarchy = cv2.findContours(yellow_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h),(0,255,255), 2)
            square = ['y',x,y]
            squares.append(square)
            #cv2.putText(imageFrame, "Yellow Colour", (x, y),cv2.FONT_HERSHEY_SIMPLEX,1.0, (255, 0, 0))

    #Finding white coloured squares
    contours, hierarchy = cv2.findContours(white_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(10000 > area > 3000):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h),(139,0,139), 2)
            square = ['w',x,y]
            squares.append(square)
            #cv2.putText(imageFrame, "White Colour", (x, y),cv2.FONT_HERSHEY_SIMPLEX,1.0, (255, 0, 0))

    i = 0
    A=[]
    while(i<4):
        c,x,y = 'x',square[1],square[2]
        for square in squares:
            if(square[1] > x and square[2] < y):
                c,x,y = square[0],square[1],square[2]
        A.append([c,x,y])
        i += 1

    print(filename + " " + str(A))

    return imageFrame

    #cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    #cv2.imshow('Original Image', original)

    #cv2.imshow('rtes', white_mask)

    #cv2.waitKey()


testImages = 'images2/'
results = 'results/'
for image in os.listdir(testImages):
    if image.endswith(".png"):  
        result = colourMatrix(testImages + image)
        cv2.imwrite(os.path.join(results , image), result)