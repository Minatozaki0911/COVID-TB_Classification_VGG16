import os
import cv2
import numpy as np
import pandas as pd
import pathlib
import argparse


home = pathlib.Path.home()
global width, height

def CLIinit():
    global args
    ap = argparse.ArgumentParser(description="Python script for resizing image from datasets")
    ap.add_argument("-i","--input", required=True, help="path to directory contains inputs image")
    ap.add_argument("-o","--output", required=True, help="path to directory to store outputs image")
    ap.add_argument("-s","--scale", type=int, default=50, help="scale factor (percentage)")
    args = vars(ap.parse_args())
    print(args)

def fileRead(directory):
    path = os.path.join(home,directory)
    files = os.listdir(path)
    return files

def fileWrite(directory, imageName, inputImg):
    path = os.path.join(home, directory)
    try:
        os.makedirs(path, exist_ok = False)
    except FileExistsError:
        pass

    size = str(inputImg.shape[1]) + 'x' + str(inputImg.shape[0])
    resizedImgName = (str(imageName)[:-4] + "_" + size) + ".png" 
    pwd = os.getcwd()
    os.chdir(path)
    cv2.imwrite(resizedImgName, inputImg)
    os.chdir(pwd)
    cv2.waitKey(1)

def imageResize(img, scale):
    grayImg = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    width = grayImg.shape[1]
    height = grayImg.shape[0]
    widthScaled = int(width * scale/100)
    heightScaled = int(height * scale/100)
    resizedImg = cv2.resize(grayImg, (widthScaled, heightScaled), interpolation = cv2.INTER_AREA)
    return resizedImg, (width, height)


if __name__ =="__main__":
    
    CLIinit()
    directory = args["input"]
    dest = args["output"]
    scale = args["scale"]

    path = os.path.join(home, directory)

    dataset = {'Name':[], 'Dimension':[]}
    allFiles = sorted(os.listdir(path), key=lambda a: int(''.join(s for s in a if s.isdigit())))
    print(allFiles)
    for image in allFiles: 
        if image[-4:] in ['.jpg', 'png']: 

            resizedImg, dimension  = imageResize(os.path.join(path, image), scale)
            fileWrite(dest, image, resizedImg)
            print("imwrite"+image)

            dataset['Name'].append(image)
            dataset['Dimension'].append(dimension)
    

    excelFileName = str(path).split("/")[-2] + "_DatasetInfo.xlsx"
    excelWriter = pd.ExcelWriter(excelFileName, engine='xlsxwriter')
    dataframe = pd.DataFrame.from_dict(dataset)
    dataframe.to_excel(excelWriter, index = False)
    excelWriter.save()
    print("Excel File Saved at current directory")

    print("Operation Completed")
