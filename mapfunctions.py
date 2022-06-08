# -*- coding: utf-8 -*-
"""
Created on Sat May 14 21:01:38 2022

@author: pbori
"""
R=256
C=256
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

def ShowFile(DataArray):
    plt.pcolormesh(DataArray, rasterized=True, vmin=0, vmax=np.amax(DataArray))
    plt.colorbar()
    plt.axis()
    plt.ylabel("Energy [KeV]", labelpad=-375)
    plt.show()
    return
def PixelHistograme(Input, Bins, ScaleType):
    D_pixely=np.ravel(np.array(Input))
    D_pixely = [i for i in D_pixely if i != 0]
    maxim_pixel=np.amax(Input)
    plt.hist(D_pixely,density=True, bins=Bins)
    plt.xlabel("Energy [KeV]")
    if (ScaleType==True):
        plt.xscale("log")
    plt.ylabel("Quantity")
    plt.grid(b=True, which="both", axis="both")
    plt.show()
def ObjectHistograme(Input, Bins, ScaleType):
    D_pixely=np.ravel(np.array(Input))
    D_pixely = [i for i in D_pixely if i != 0]
    maxim_pixel=np.amax(Input)
    plt.hist(D_pixely,density=True, bins=Bins)
    plt.xlabel("Energy [KeV]")
    plt.ylabel("Quantity")
    if (ScaleType==True):
        plt.xscale("Log")
    plt.grid(b=True, which="both", axis="both")
    plt.show()
    
    
def ObjectTypeHistograme(Input, Bins, ScaleType, ObjectType):
    SPMatrix=[]
    for i in range (len(Input)):
        if Input[i][3]==ObjectType:
            SPMatrix.append(Input[i][2])
    maxim_type=np.amax(SPMatrix)
    plt.hist(SPMatrix, density=True, bins=Bins)
    plt.xlabel("Energy [KeV]")
    plt.ylabel("Quantity")
    if (ScaleType==True):
        plt.xscale("Log")
    plt.grid(b=True, which="both",axis="both")
    plt.show()
        
    
    
def Crop(Input):
    Rmin=R+1
    Cmin=C+1
    Rmax=0
    Cmax=0
    Output=[]
    for i in range (R):
        for j in range (C):
            if Input[i][j]!=0:
                if i<Rmin:
                    Rmin=i
                if j<Cmin:
                    Cmin=j
                if i>Rmax:
                    Rmax=i
                if j>Cmax:
                    Cmax=j
    Rdif=Rmax-Rmin+1
    Cdif=Cmax-Cmin+1
    for i in range (Rdif+2):
        temp5=[]
        for j in range (Cdif+2):
            temp5.append(0)
        Output.append(temp5)
    for i in range (Rdif):
        for j in range (Cdif):
            x=i+Rmin
            y=j+Cmin
            Output[i+1][j+1]=Input[x][y]
    return(Output)
def ShowSingleObject(DataArray, ObjectArray, ObjectN, Cropping):
    SupportMatrix=[]
    for i in range(R):
        temp8=[]
        for j in range (C):
            temp8.append(0)
        SupportMatrix.append(temp8)
    for i in range (R):
        for j in range (C):
            if ObjectArray[i][j]==ObjectN:
                SupportMatrix[i][j]=DataArray[i][j]
    if (Cropping==False):
        plt.pcolormesh(SupportMatrix, rasterized=True, vmin=0, vmax=np.amax(SupportMatrix))
    elif (Cropping==True):
        plt.pcolormesh(Crop(SupportMatrix), rasterized=True, vmin=0, vmax=np.amax(Crop(SupportMatrix)))
    plt.colorbar()
    plt.ylabel("Energy [KeV]", labelpad=-375)
    plt.show()
    return
def ShowTypeFile(DataArray, ObjectArray, DetectionList, Type):
    SupportMatrix2=[]
    for i in range (R):
        temp9=[]
        for j in range(C):
            temp9.append(0)
        SupportMatrix2.append(temp9)
    for k in range(len(DetectionList)):
        for i in range(R):
            for j in range(C):
                if ObjectArray[i][j]==DetectionList[k][0]:
                    if DetectionList[k][3]==Type:
                        SupportMatrix2[i][j]=DataArray[i][j]
    plt.pcolormesh(SupportMatrix2, rasterized=True, vmin=0, vmax=np.amax(SupportMatrix2))
    plt.colorbar()
    plt.ylabel("Energy [KeV]", labelpad=-375)
    plt.show()
def ShowTypeCount(UnknownCount, AlphaCount, BetaCount, GammaCount, MuionCount, HEPCount):
    ArrayCounts={"Unknown":UnknownCount, "Alpha":AlphaCount,"Beta":BetaCount,"Gamma":GammaCount,"Muion":MuionCount,"HEP":HEPCount}
    Keys0=list(ArrayCounts.keys())
    Values0=list(ArrayCounts.values())
    plt.bar(Keys0,Values0)
    print(ArrayCounts)
    plt.ylabel("Count [N]")
    plt.grid(b=True, which="both", axis="y")
    plt.show()
    
def ShowTypeEnergyCount(ObjectListArray):
    ArraySupportEnergy=[]
    for i in range(6):
        ArraySupportEnergy.append(0)
    for i in range (len(ObjectListArray)):
        for j in range (6):
            if ObjectListArray[i][3]==j:
                ArraySupportEnergy[j]=ObjectListArray[i][2]+ArraySupportEnergy[j]
        
        
    ArrayEnergyCounts={"Unknown":ArraySupportEnergy[0], "Alpha":ArraySupportEnergy[1],"Beta":ArraySupportEnergy[2],"Gamma":ArraySupportEnergy[3],"Muion":ArraySupportEnergy[4],"HEP":ArraySupportEnergy[5]}
    
    Keys1=list(ArrayEnergyCounts.keys())
    Values1=list(ArrayEnergyCounts.values())
    plt.bar(Keys1,Values1)
    plt.ylabel("Energy [KeV]")
    plt.grid(b=True, which="both", axis="y")
    
    plt.show()