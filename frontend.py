# -*- coding: utf-8 -*-
"""
Created on Fri May 13 20:52:29 2022

@author: pbori
"""
import tkinter
from tkinter import *
from tkinter import filedialog as fd
import sys
import generalfunctions
import mapfunctions
import Analysis

root = tkinter.Tk()
root.geometry("1200x800") 
root.title("Name") 
root.option_add('*Font', 'Arial 10') 


ObjectVar=tkinter.IntVar()
ObjectVar.set(0)
InputSTR=tkinter.StringVar()
InputSTR.set("No input.")
InputFile=""
CropBool=tkinter.BooleanVar()
ObjectCountVar=tkinter.IntVar()
TotalEnergyVar=tkinter.StringVar()
TotalEnergyVar.set("0")

AlphaVar=tkinter.IntVar()
BetaVar=tkinter.IntVar()
GammaVar=tkinter.IntVar()
MuionVar=tkinter.IntVar()
HEPVar=tkinter.IntVar()
UnknownVar=tkinter.IntVar()

AlphaEnergyVar=tkinter.DoubleVar()
BetaEnergyVar=tkinter.DoubleVar()
GammaEnergyVar=tkinter.DoubleVar()
MuionEnergyVar=tkinter.DoubleVar()
HEPEnergyVar=tkinter.DoubleVar()
UnknownEnergyVar=tkinter.DoubleVar()


PixHistScaleBool=tkinter.BooleanVar()
ObjHistScaleBool=tkinter.BooleanVar()
ObjTypeHistScaleBool=tkinter.BooleanVar()

OverlapSTR=tkinter.StringVar()


SensorSaturationVar=tkinter.DoubleVar()
PixelCountVar=tkinter.IntVar()
InputThreshhold=tkinter.DoubleVar()
ShowTypeVar=tkinter.IntVar()

ObjectEnergyVar=tkinter.IntVar()
ObjectPixelCountVar=tkinter.IntVar()
ObjectSpreadVar=tkinter.IntVar()
ObjectTypeSTR=tkinter.StringVar()
ObjectTypeSTR.set("NULL")
OverlapSTR.set("")
ThreshholdValue=0
InputThreshhold.set(0)

InputData=[]
ObjectsArray=[]
DetectionsList=[] #ObjectN, Pixels, Energy, Type, Spread
def Import():
    InputFile = fd.askopenfilename()
    InputSTR.set(InputFile)
    RefreshObject()
    ConfirmAdressButton=tkinter.Button(TK_Adress, text="Confirm", command=execute, state="normal").grid(row=4, column=2)
def ObjectAdd():
    ObjectVar.set(ObjectVar.get()+1)
    ShowObjectFunction()
    RefreshObject()
def ObjectSub():
    ObjectVar.set(ObjectVar.get()-1)
    ShowObjectFunction()
    RefreshObject()
def SetObject():
    ObjectVar.set(InputObjectEntry.get())
    RefreshObject()
def ShowTypeSelected():
    mapfunctions.ShowTypeFile(InputData, ObjectsArray[0],DetectionsList,ShowTypeVar.get() )
        
def RefreshMeasurements():
    tkinter.Label(TK_Measurements, text=ObjectCountVar.get()).grid(row=1, column=2)
    tkinter.Label(TK_Measurements, text=TotalEnergyVar.get()).grid(row=2, column=2)
    tkinter.Label(TK_Measurements, text=AlphaVar.get()).grid(row=3, column=2)
    tkinter.Label(TK_Measurements, text=BetaVar.get()).grid(row=4, column=2)
    tkinter.Label(TK_Measurements, text=GammaVar.get()).grid(row=5, column=2)
    tkinter.Label(TK_Measurements, text=MuionVar.get()).grid(row=6, column=2)
    tkinter.Label(TK_Measurements, text=HEPVar.get()).grid(row=7, column=2)
    tkinter.Label(TK_Measurements, text=UnknownVar.get()).grid(row=8, column=2)
    tkinter.Label(TK_Measurements, text=str(SensorSaturationVar.get())+" %").grid(row=9, column=2)
    tkinter.Label(TK_Measurements, text=PixelCountVar.get()).grid(row=10, column=2)
    tkinter.Label(TK_Measurements, text=AlphaEnergyVar.get()).grid(row=3, column=4)
    tkinter.Label(TK_Measurements, text=BetaEnergyVar.get()).grid(row=4, column=4)
    tkinter.Label(TK_Measurements, text=GammaEnergyVar.get()).grid(row=5, column=4)
    tkinter.Label(TK_Measurements, text=MuionEnergyVar.get()).grid(row=6, column=4)
    tkinter.Label(TK_Measurements, text=HEPEnergyVar.get()).grid(row=7, column=4)
    tkinter.Label(TK_Measurements, text=UnknownEnergyVar.get()).grid(row=8, column=4)
def RefreshObject():
    tkinter.Label(TK_Object, text=ObjectVar.get()).grid(row=4, column=2)
    tkinter.Label(TK_Object, text=ObjectEnergyVar.get(), padx=5, pady=5).grid(row=6, column=2)
    tkinter.Label(TK_Object, text=ObjectPixelCountVar.get(), padx=5, pady=5).grid(row=7, column=2)
    tkinter.Label(TK_Object, text=ObjectSpreadVar.get(), padx=5, pady=5).grid(row=8, column=2)
    tkinter.Label(TK_Object, text=ObjectTypeSTR.get(), padx=5, pady=5).grid(row=9, column=2)
    tkinter.Label(TK_Object, text=OverlapSTR.get(), padx=5, pady=5).grid(row=10, column=2)

def ParticleTypesMeasure():
    global DetectionsList
    for i in range(len(DetectionsList)):
        if DetectionsList[i][3]==0:
            UnknownVar.set(UnknownVar.get()+1)
        if DetectionsList[i][3]==1:
            AlphaVar.set(AlphaVar.get()+1)
        if DetectionsList[i][3]==2:
            BetaVar.set(BetaVar.get()+1)
        if DetectionsList[i][3]==3:
            GammaVar.set(GammaVar.get()+1)
        if DetectionsList[i][3]==4:
            MuionVar.set(MuionVar.get()+1)
        if DetectionsList[i][3]==5:
            HEPVar.set(HEPVar.get()+1)
def ParticleTypesEnergyMeasure():
    global DetectionsList
    for i in range(len(DetectionsList)):
        if DetectionsList[i][3]==0:
            UnknownEnergyVar.set(UnknownEnergyVar.get()+DetectionsList[i][2])
        if DetectionsList[i][3]==1:
            AlphaEnergyVar.set(AlphaEnergyVar.get()+DetectionsList[i][2])
        if DetectionsList[i][3]==2:
            BetaEnergyVar.set(BetaEnergyVar.get()+DetectionsList[i][2])
        if DetectionsList[i][3]==3:
            GammaEnergyVar.set(GammaEnergyVar.get()+DetectionsList[i][2])
        if DetectionsList[i][3]==4:
            MuionEnergyVar.set(MuionEnergyVar.get()+DetectionsList[i][2])
        if DetectionsList[i][3]==5:
            HEPEnergyVar.set(HEPEnergyVar.get()+DetectionsList[i][2])
        
def ConfirmThreshhold():
    global ThreshholdValue
    ThreshholdValue=float(InputThreshhold.get())
    print(ThreshholdValue)
def execute():
    global ThreshholdValue
    global InputData
    global ObjectsArray
    global DetectionsList
    generalfunctions.test()
    InputData=generalfunctions.LoadFile(InputSTR.get())
    ObjectsArray=generalfunctions.SeparateObjects(InputData,0, ThreshholdValue)
    ExecuteAnalysis()
    DetectionsList=Analysis.TypesAnalysis(InputData, ObjectsArray[0],DetectionsList)
    ParticleTypesMeasure()
    ParticleTypesEnergyMeasure()
    RefreshMeasurements()
    
    
    
    TK_Unlock()

        
def ExecuteAnalysis():
    global DetectionsList
    SensorSaturationVar.set(round((Analysis.Saturation(InputData)),3))
    PixelCountVar.set(Analysis.PixelCount(InputData))
    ObjectCountVar.set(Analysis.ObjectsCount(ObjectsArray[0]))
    TotalEnergyVar.set(round(Analysis.TotalEnergy(InputData),3))
    DetectionsList=Analysis.Parametres(InputData, ObjectsArray[0])
def ShowFile():
    mapfunctions.ShowFile(InputData)
    

def ShowTypeCountFunction():
    mapfunctions.ShowTypeCount(UnknownVar.get(), AlphaVar.get(),BetaVar.get(),GammaVar.get(),MuionVar.get(),HEPVar.get())
    
def ShowEnergyTypeFunction():
    mapfunctions.ShowTypeEnergyCount(DetectionsList)    
    
    
    
def TK_Unlock():
    ShowFileButton=tkinter.Button(TK_InputFilePlot, text="Confirm", command=ShowFile, state="normal").grid(row=1, column=1)
    ShowPixelHist=tkinter.Button(TK_PixelHist, text="Confirm", command=ShowPixelHistFunction, state="normal").grid(row=2, column=1)
    ShowObjectHist=tkinter.Button(TK_ObjectHist, text="Confirm", command=ShowObjectHistFunction, state="normal").grid(row=2, column=1)
    ShowObject=tkinter.Button(TK_Object, text="Confirm",command=ShowObjectFunction, state="normal").grid(row=5, column=2)
    ShowType=tkinter.Button(TK_ShowType, text="Show", state="normal", command=ShowTypeSelected).grid(row=3, column=2)
    ShowTypeCount=tkinter.Button(TK_TypeCount, text="Confirm",command=ShowTypeCountFunction, state="normal").grid(row=1, column=1)
    ShowEnergyType=tkinter.Button(TK_EnergyType, text="Confirm",command=ShowEnergyTypeFunction, state="normal").grid(row=1, column=1)
    ShowTypeHistButton=tkinter.Button(TK_ShowType, text="Show hist", state="normal", command=ShowTypeHistEnergyFunction).grid(row=2, column=3)


def ShowTypeHistEnergyFunction():
    mapfunctions.ObjectTypeHistograme(DetectionsList, 25, ObjTypeHistScaleBool.get(), ShowTypeVar.get())
    
def ShowPixelHistFunction():
    mapfunctions.PixelHistograme(InputData, 100, PixHistScaleBool.get())    
    
    RefreshMeasurements()

def ShowObjectHistFunction():
    
    mapfunctions.ObjectHistograme(generalfunctions.ObjectEnergy(ObjectsArray[0], InputData), 100, ObjHistScaleBool.get())
    RefreshMeasurements()
    
def ShowObjectFunction():    
    global DetectionsList
    mapfunctions.ShowSingleObject(InputData,ObjectsArray[0],ObjectVar.get(),CropBool.get())
    ObjectPixelCountVar.set(DetectionsList[ObjectVar.get()-1][1])
    ObjectEnergyVar.set(DetectionsList[ObjectVar.get()-1][2])
    ObjectTypeSTR.set(generalfunctions.Types(DetectionsList[ObjectVar.get()-1][3]))
    if (Analysis.DetectOverlap(InputData, ObjectsArray[0], ObjectVar.get()))==True:
        OverlapSTR.set("OVERLAP")
    else:
        OverlapSTR.set("               ")
    RefreshObject()
    RefreshMeasurements()
    
TK_Adress=tkinter.LabelFrame(root, text="File adress", padx=5, pady=5)
TK_Adress.grid(row=1, column=1,sticky="w")


    


LoadFileButton=tkinter.Button(TK_Adress, text="Load Input file", command=lambda: Import(), state="normal").grid(row=3, column=1)

tkinter.Label(TK_Adress, text="Path to input file:").grid(row=2, column=1)

tkinter.Label(TK_Adress, textvariable=InputSTR).grid(row=2, column=2)

ConfirmAdressButton=tkinter.Button(TK_Adress, text="Confirm", command=execute, state="disabled").grid(row=4, column=2)


TK_Config=tkinter.LabelFrame(root, text="Config", padx=5, pady=5)
TK_Config.grid(row=1, column=1, sticky="e")

tkinter.Label(TK_Config, text="Threshhold energy:", padx=5, pady=5).grid(row=1, column=1)
InputThreshhold=tkinter.Entry(TK_Config, width=6)
InputThreshhold.grid(row=1, column=2)
Threshholdconfigr=tkinter.Button(TK_Config, command=ConfirmThreshhold, text="Confirm", padx=5, pady=5).grid(row=1, column=3)




TK_Plots=tkinter.LabelFrame(root, text="Ploting",padx=5, pady=5)
TK_Plots.grid(row=2, column=1)

TK_InputFilePlot=tkinter.LabelFrame(TK_Plots, text="Show Input file", padx=5, pady=5)
TK_InputFilePlot.grid(row=1, column=1)
ShowFileButton=tkinter.Button(TK_InputFilePlot, text="Confirm", command=ShowFile, state="disabled").grid(row=1, column=1)

TK_PixelHist=tkinter.LabelFrame(TK_Plots, text="Show Pixel Histograme", padx=5, pady=5)
TK_PixelHist.grid(row=1, column=2)
tkinter.Checkbutton(TK_PixelHist, text="Log Scale", variable=PixHistScaleBool, padx=5, pady=5).grid(row=1, column=1)
ShowPixelHist=tkinter.Button(TK_PixelHist, text="Confirm", command=ShowPixelHistFunction, state="disabled").grid(row=2, column=1)

TK_ObjectHist=tkinter.LabelFrame(TK_Plots, text="Show Object Histograme", padx=5, pady=5)
TK_ObjectHist.grid(row=1, column=3)
tkinter.Checkbutton(TK_ObjectHist, text="Log Scale", variable=ObjHistScaleBool, padx=5, pady=5).grid(row=1, column=1)
ShowObjectHist=tkinter.Button(TK_ObjectHist, text="Confirm", command=ShowObjectHistFunction, state="disabled").grid(row=2, column=1)


TK_Object=tkinter.LabelFrame(TK_Plots, text="Show Object", padx=5, pady=5)
TK_Object.grid(row=1, column=4)
InputObjectEntry=tkinter.Entry(TK_Object, width=6)
InputObjectEntry.grid(row=1, column=1)
SetObjectEntry=tkinter.Button(TK_Object, text="Set", command=SetObject).grid(row=1, column=2)
tkinter.Label(TK_Object, text="Object number", padx=5, pady=5).grid(row=3, column=2)
ObjectAdd=tkinter.Button(TK_Object, text=">", state="normal", command=ObjectAdd).grid(row=4, column=3)
tkinter.Label(TK_Object, text=ObjectVar.get()).grid(row=4, column=2)
tkinter.Checkbutton(TK_Object, text="crop", variable=CropBool, padx=5, pady=5).grid(row=3, column=1)
ObjectSub=tkinter.Button(TK_Object, text="<", state="normal", command=ObjectSub).grid(row=4, column=1)
ShowObject=tkinter.Button(TK_Object, text="Confirm",command=ShowObjectFunction, state="disabled").grid(row=5, column=2)


tkinter.Label(TK_Object, text="Object Energy:", padx=5, pady=5).grid(row=6, column=1)
tkinter.Label(TK_Object, text="Object Pixels:", padx=5, pady=5).grid(row=7, column=1)
tkinter.Label(TK_Object, text="Object Spread:", padx=5, pady=5).grid(row=8, column=1)
tkinter.Label(TK_Object, text="Object type:", padx=5, pady=5).grid(row=9, column=1)

tkinter.Label(TK_Object, text=ObjectEnergyVar.get(), padx=5, pady=5).grid(row=6, column=2)
tkinter.Label(TK_Object, text=ObjectPixelCountVar.get(), padx=5, pady=5).grid(row=7, column=2)
tkinter.Label(TK_Object, text=ObjectSpreadVar.get(), padx=5, pady=5).grid(row=8, column=2)
tkinter.Label(TK_Object, text=ObjectTypeSTR.get(), padx=5, pady=5).grid(row=9, column=2)
tkinter.Label(TK_Object, text=OverlapSTR.get(), padx=5, pady=5).grid(row=10, column=2)


TK_ShowType=tkinter.LabelFrame(TK_Plots, text="Show particle type", padx=5, pady=5)
TK_ShowType.grid(row=1, column=5)
Radiobutton(TK_ShowType, text="  Alpha  ", variable=ShowTypeVar, value=1,).grid(row=1, column=1)
Radiobutton(TK_ShowType, text="  Beta  ", variable=ShowTypeVar, value=2,).grid(row=2, column=1)
Radiobutton(TK_ShowType, text="  Gamma  ", variable=ShowTypeVar, value=3,).grid(row=3, column=1)
Radiobutton(TK_ShowType, text="  Muion  ", variable=ShowTypeVar, value=4,).grid(row=4, column=1)
Radiobutton(TK_ShowType, text="  HEP  ", variable=ShowTypeVar, value=5,).grid(row=5, column=1)
Radiobutton(TK_ShowType, text="  Unknown  ", variable=ShowTypeVar, value=0).grid(row=6, column=1)
ShowType=tkinter.Button(TK_ShowType, text="Show", state="disabled", command=ShowTypeSelected).grid(row=3, column=2)
ShowTypeHistButton=tkinter.Button(TK_ShowType, text="Show hist", state="disabled", command=ShowTypeHistEnergyFunction).grid(row=2, column=3)
tkinter.Checkbutton(TK_ShowType, text="Log Scale", variable=ObjTypeHistScaleBool, padx=5, pady=5).grid(row=1, column=3)

TK_TypeCount=tkinter.LabelFrame(TK_Plots, text="Show type distribution", padx=5, pady=5)
TK_TypeCount.grid(row=1, column=6)
ShowTypeCount=tkinter.Button(TK_TypeCount, text="Confirm",command=ShowTypeCountFunction, state="disabled").grid(row=1, column=1)

TK_EnergyType=tkinter.LabelFrame(TK_Plots, text="Show Energy per type", padx=5, pady=5)
TK_EnergyType.grid(row=1, column=7)
ShowEnergyType=tkinter.Button(TK_EnergyType, text="Confirm",command=ShowEnergyTypeFunction, state="disabled").grid(row=1, column=1)

TK_Measurements=tkinter.LabelFrame(root, text="Measurements", padx=5, pady=5)
TK_Measurements.grid(row=3, column=1, sticky="w")
tkinter.Label(TK_Measurements, text="Number of objects:").grid(row=1, column=1)
tkinter.Label(TK_Measurements, text="Total Energy:").grid(row=2, column=1)
tkinter.Label(TK_Measurements, text="Alpha count:").grid(row=3, column=1)
tkinter.Label(TK_Measurements, text="Beta count:").grid(row=4, column=1)
tkinter.Label(TK_Measurements, text="Gamma count:").grid(row=5, column=1)
tkinter.Label(TK_Measurements, text="Muion count:").grid(row=6, column=1)
tkinter.Label(TK_Measurements, text="HEP count:").grid(row=7, column=1)
tkinter.Label(TK_Measurements, text="Unknown objects:").grid(row=8, column=1)
tkinter.Label(TK_Measurements, text="Detector saturation:").grid(row=9, column=1)
tkinter.Label(TK_Measurements, text="Detected pixels count:").grid(row=10, column=1)



tkinter.Label(TK_Measurements, text=ObjectCountVar.get()).grid(row=1, column=2)
tkinter.Label(TK_Measurements, text=TotalEnergyVar.get()).grid(row=2, column=2)
tkinter.Label(TK_Measurements, text=AlphaVar.get()).grid(row=3, column=2)
tkinter.Label(TK_Measurements, text=BetaVar.get()).grid(row=4, column=2)
tkinter.Label(TK_Measurements, text=GammaVar.get()).grid(row=5, column=2)
tkinter.Label(TK_Measurements, text=MuionVar.get()).grid(row=6, column=2)
tkinter.Label(TK_Measurements, text=HEPVar.get()).grid(row=7, column=2)
tkinter.Label(TK_Measurements, text=UnknownVar.get()).grid(row=8, column=2)
tkinter.Label(TK_Measurements, text=str(SensorSaturationVar.get())+" %").grid(row=9, column=2)
tkinter.Label(TK_Measurements, text=PixelCountVar.get()).grid(row=10, column=2)

tkinter.Label(TK_Measurements, text="Total Alpha Energy:").grid(row=3, column=3)
tkinter.Label(TK_Measurements, text="Total Beta Energy:").grid(row=4, column=3)
tkinter.Label(TK_Measurements, text="Total Gamma Energy:").grid(row=5, column=3)
tkinter.Label(TK_Measurements, text="Total Muion Energy:").grid(row=6, column=3)
tkinter.Label(TK_Measurements, text="Total HEP Energy:").grid(row=7, column=3)
tkinter.Label(TK_Measurements, text="Total Unknown Energy:").grid(row=8, column=3)



tkinter.Label(TK_Measurements, text=AlphaEnergyVar.get()).grid(row=3, column=4)
tkinter.Label(TK_Measurements, text=BetaEnergyVar.get()).grid(row=4, column=4)
tkinter.Label(TK_Measurements, text=GammaEnergyVar.get()).grid(row=5, column=4)
tkinter.Label(TK_Measurements, text=MuionEnergyVar.get()).grid(row=6, column=4)
tkinter.Label(TK_Measurements, text=HEPEnergyVar.get()).grid(row=7, column=4)
tkinter.Label(TK_Measurements, text=UnknownEnergyVar.get()).grid(row=8, column=4)


tkinter.Label(TK_Measurements, text="KeV").grid(row=3, column=5)
tkinter.Label(TK_Measurements, text="KeV").grid(row=4, column=5)
tkinter.Label(TK_Measurements, text="KeV").grid(row=5, column=5)
tkinter.Label(TK_Measurements, text="KeV").grid(row=6, column=5)
tkinter.Label(TK_Measurements, text="KeV").grid(row=7, column=5)
tkinter.Label(TK_Measurements, text="KeV").grid(row=8, column=5)




root.mainloop()