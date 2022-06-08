# -*- coding: utf-8 -*-
"""
Created on Sat May 14 20:46:50 2022

@author: pbori
"""
R=256
C=256
def test():
    print("test")
def LoadFile(Path):
    DataArray=[]
    SourceFile=open(Path, "r")
    for line in SourceFile:
            DataArray.append([float(x) for x in line.split()])
    SourceFile.close()
    print("File", Path, " loaded.")
    return DataArray
def SeparateObjects(InputData, ObjectCount, threshhold):
    Support=[]
    Output=[]
    ObjectsArray=[]
    for i in range(R):
        for j in range(C):
            if InputData[i][j]<threshhold:
                InputData[i][j]=0
    for i in range(R+2):
        temp1=[]
        for j in range (C+2):
            temp1.append(0)
        Support.append(temp1)

    for i in range(R+2):
        temp2=[]
        for j in range (C+2):
            temp2.append(0)
        Output.append(temp2)
    for i in range(R):
        for j in range(C):
            if InputData[i][j]!=0:
                Support[i+1][j+1]=1
    for i in range(R):
        temp3=[]
        for j in range(C):
            temp3.append(0)
        ObjectsArray.append(temp3)
            
    detection=1
    ObjectN=1
    Hit=ObjectCount+1
    test=0
    while detection!=0:
        detection=0
        Found=0
        for i in range (R):
            for j in range(C):                
                x=i+1
                y=j+1
            
                if Found==0:
                    if Support[x][y]==1:
                        Support[x][y]=2
                        detection=1
                        Found=1


                    
                    
        while ObjectN!=0:
            ObjectN=0
            for i in range (R):
                for j in range(C):
                    x=i+1
                    y=j+1
                    if Support[x][y]==2:
                
                        if Support[x-1][y-1]==1:
                            Support[x-1][y-1]=2
                            ObjectN=1
                        
                        if Support[x-1][y]==1:
                            Support[x-1][y]=2
                            ObjectN=1
                        
                        if Support[x-1][y+1]==1:
                            Support[x-1][y+1]=2
                            ObjectN=1
                        
                        if Support[x][y-1]==1:
                            Support[x][y-1]=2
                            ObjectN=1
                        
                        if Support[x][y+1]==1:
                            Support[x][y+1]=2
                            ObjectN=1
                        
                        if Support[x+1][y-1]==1:
                            Support[x+1][y-1]=2
                            ObjectN=1
                        
                        if Support[x+1][y]==1:
                            Support[x+1][y]=2
                            ObjectN=1
                        
                        if Support[x+1][y+1]==1:
                            Support[x+1][y+1]=2
                            ObjectN=1
            if ObjectN==0:
                for i in range(R):
                    for j in range(C):
                        x=i+1
                        y=j+1                    
                        if Support[x][y]==2:
                            test=1
                            Support[x][y]=0
                            Output[x][y]=Hit
                        if test==0:
                            test=1
                        
                            ObjectN=1
                                
        for i in range(R):
            for j in range(C):
                if ObjectN==0:
                    x=i+1
                    y=j+1
                    if Support[x][y]!=0:
                        detection=1
                        ObjectN=1
                        Hit=Hit+1
    for i in range(R):
        for j in range(C):
            ObjectsArray[i][j]=Output[i+1][j+1]
    print("Vytvorena vystupni matice.")
    
    return ObjectsArray, Hit
def ObjectEnergy(Input, DataArray):
    tempM=0
    Output_Object_List=[]
    for j in range (R):
        for k in range(C):
            if Input[j][k]>tempM:
                tempM=Input[j][k]
    for i in range (tempM):
        Output_Object_List.append(0)
        
    for i in range (tempM):
        tempI=0
        for j in range (R):
            for k in range(C):
                if Input[j][k]==i and Input[j][k]!=0:
                    tempI=tempI+DataArray[j][k]
        Output_Object_List[i]=tempI
    return Output_Object_List
def Types(TypeInt):
    TypeStr=""
    if TypeInt==0:
        TypeStr="Unknown"
    if TypeInt==1:
        TypeStr="Alpha"
    if TypeInt==2:
        TypeStr="Beta"
    if TypeInt==3:
        TypeStr="Gamma"
    if TypeInt==4:
        TypeStr="Muion"
    if TypeInt==5:
        TypeStr="HEP"
    return(TypeStr)

def Reboot(Confirm):
    if Confirm==True:
        os.execl(sys.executable, sys.executable, *sys.argv)
