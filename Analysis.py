# -*- coding: utf-8 -*-
"""
Created on Sun May 15 01:24:24 2022

@author: pbori
"""
import scipy
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage import data, img_as_float
import mapfunctions
import numpy as np
C=256
R=256
def Saturation(InputFile):
    global SensorSaturationVar
    Zeros=0
    for i in range (R):
        for j in range(C):
            if InputFile[i][j]==0:
                Zeros=Zeros+1
    return (100*(1-Zeros/(R*C)))
def PixelCount(InputFile):
    Pixels=0
    for i in range(R):
        for j in range(C):
            if InputFile[i][j]!=0:
                Pixels=Pixels+1
    return(Pixels)
def ObjectsCount(ObjectArray):
    return np.amax(ObjectArray)
def TotalEnergy(InputFile):
    Energy=0
    for i in range(R):
        for j in range(C):
            Energy=Energy+InputFile[i][j]
    return (Energy)
def Parametres(InputFile, ObjectArray):
    DetectionList1=[]
    MAXV=np.amax(ObjectArray)
    for k in range (MAXV):
        DetectionList1.append([k+1, 0, 0, 0,0])
        
    for i in range(R):
        for j in range(C):
            for k in range (MAXV):
                if ((k+1)==ObjectArray[i][j]):
                    DetectionList1[k][1]=DetectionList1[k][1]+1
                    DetectionList1[k][2]=DetectionList1[k][2]+InputFile[i][j]
    return DetectionList1
def TypesAnalysis(InputFile, ObjectArray, DetectionList):
    for i in range (np.amax(ObjectArray)):
        if DetectionList[i][1]<5:
            DetectionList[i][3]=3
        if DetectionList[i][1]>=5:
            if DetectionList[i][2]<=1000:
                DetectionList[i][3]=2  
        if DetectionList[i][2]>1000:
            Alpha=1
            if Alpha==1:
                DetectionList[i][3]=1
            if Alpha==0:
                DetectionList[i][3]=5
    return DetectionList
def DetectOverlap(DataArray, ObjectArray, ObjectN):
    SuppMatrix=[]
    for i in range(R):
        temp11=[]
        for j in range (C):
            temp11.append(0)
        SuppMatrix.append(temp11)
    for i in range (R):
        for j in range (C):
            if ObjectArray[i][j]==ObjectN:
                SuppMatrix[i][j]=DataArray[i][j]
    Peaks=peak_local_max(np.array(SuppMatrix), min_distance=3,threshold_rel=0.45)
    if (len(Peaks)>1):
        return (True)
    if (len(Peaks)<2):
        return (False)


    
    