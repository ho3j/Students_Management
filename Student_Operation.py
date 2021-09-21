"""
Hossein JALILI
Python Class IUT  
Shahrivar 1400
Project final ver 15
Student_Opration.py
"""
#........................import............................

import pickle
import os 
#import datetime
import jdatetime
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pandas as pd
import qrcode
import pyttsx3

from faker import Faker

import string
from random import *
import pywhatkit
from colorama import Fore
import time


import Login_Student as login
#.......................func miss.............................
def dell_pic():
    dir_list_p = os.listdir("pic/")
    try:
        for i in dir_list_p:
            location_p = os.getcwd()+"/pic/"
            path_p = os.path.join(location_p, i)
            os.remove(path_p)
            login.write_operation("*delete all pic in pic folder*")
    except:
        login.write_operation("*can nort delete all pic in pic folder!!*")
#........................load...........................
StartTime1=time.time()
try :
    with open("active_students.db","rb") as as_db:
        active_students=pickle.load(as_db)
    with open("graduate_students.db","rb") as gs_db:
        graduate_students=pickle.load(gs_db)
    login.write_operation("*found and open student .db*")
except :
    e = pyttsx3.init()
    e.say(" Miss student databases Data !")
    e.runAndWait()
    print(Fore.LIGHTRED_EX+"\n\U0000274C Miss student databases Data ! \n")
    active_students=[]
    graduate_students= []
    dell_pic()
    login.write_operation("*can not found and open student .db , creat empety student .db*")

    with open("active_students.db","wb") as as_db:
        pickle.dump(active_students,as_db)
    with open("graduate_students.db","wb") as gs_db:
        pickle.dump(graduate_students,gs_db)
    print("\n\U0001F514 Empty active_students.db & graduate_students.db is Create Done!"+Fore.RESET)
    login.write_operation("*Empty active_students.db & graduate_students.db is Create Done!*")
    e = pyttsx3.init()
    e.say(" Empty active_students.db & graduate_students.db is Create Done!")
    e.runAndWait()
EndTime1=time.time()
TotalTime1=EndTime1-StartTime1
login.write_operation(" total time load as.db  gs.db  : \t"+str(TotalTime1))

#........................lambada............................

clear=lambda : os.system("cls")

#.......................function............................

def add_student():
    StartTime2=time.time()
    clear()
    login.write_operation("****run add_student****")
    student=dict()

    while True :
        try:
            e = pyttsx3.init()
            e.say("Enter first_name ,and last_name")
            e.runAndWait()
            student["first_name"]=input(Fore.LIGHTYELLOW_EX+"\U0001F4CCEnter First_Name of Student: "+Fore.LIGHTBLUE_EX).title()
            student["last_name"]=input(Fore.LIGHTYELLOW_EX+"\U0001F4CC\U0001F4CCEnter Last_Name of Student: "+Fore.LIGHTBLUE_EX).title()
            if student["first_name"]!=' ' and student["last_name"]!=' ' and student["first_name"]!='' and student["last_name"]!='' :
                break
            else:
                print(Fore.LIGHTRED_EX+"\U0001F514The number of first_name and last_name biger than '1' !"+Fore.RESET)
        except:
            print(Fore.LIGHTRED_EX+"\U0000274CEnter true value !"+Fore.RESET)

    while True :
        try:
            m=[]
            e = pyttsx3.init()
            e.say("Enter birthday")
            e.runAndWait()
            m=input(Fore.LIGHTYELLOW_EX+"\U0001F4C5Enter birthday of Student : yyyy,mm,dd "+Fore.LIGHTBLUE_EX).split(",")
            if (len(m[0])==4 and 0<len(m[1])<3 and 0<len(m[2])<3 and m[0].isdigit() and m[1].isdigit() and m[2].isdigit() ):
                yyyy,mm,dd=int(m[0]),int(m[1]),int(m[2])
                #student["birthday"]= datetime.datetime(yyyy,mm,dd)
                student["birthday"]= jdatetime.date(yyyy,mm,dd)

                break
            else:
                #print("\U0000274CFor Example:\t2020,5,10 !")
                print(Fore.LIGHTRED_EX+"\U0000274CFor Example:\t1400,6,23 !"+Fore.RESET)
        except:
            print(Fore.LIGHTRED_EX+"\U0000274C Month betwwn 1-12 \tDay betwwn 1-31"+Fore.RESET)
    while True :
        try:
            e = pyttsx3.init()
            e.say("code melli")
            e.runAndWait()
            student["code_melli"]=int(input(Fore.LIGHTYELLOW_EX+"\U0001F4A0Enter Numbers of Code_Melli : "+Fore.LIGHTBLUE_EX))
            if (1000000000<=student["code_melli"]<10000000000 ) :
                break
            else:
                print(Fore.LIGHTRED_EX+"\U0001F514Number Shoud be 10 Digits !"+Fore.RESET)
        except :
            print(Fore.LIGHTRED_EX+"\U0000274CEnter Number !"+Fore.RESET)
    while True:
        try:
            e = pyttsx3.init()
            e.say("student code")
            e.runAndWait()
            student["student_code"]=int(input(Fore.LIGHTYELLOW_EX+"\U0001F393Enter Numbers of Student_Code : "+Fore.LIGHTBLUE_EX))
            if str(student["student_code"]).isdigit() :
                break
        except:
            print(Fore.LIGHTRED_EX+"\U0000274CEnter Number !"+Fore.RESET)
    while True:
        try:
            e = pyttsx3.init()
            e.say("Enter courses ,and grades")
            e.runAndWait()
            student["courses"]=input(Fore.LIGHTYELLOW_EX+"\U0001F535Enter List of Courses (between Course insert ','): \n"+Fore.LIGHTBLUE_EX).split(',')
            student["grade"]=input(Fore.LIGHTYELLOW_EX+"\U0001F7E3Enter List of Grade (between Grade insert ','): \n"+Fore.LIGHTBLUE_EX).split(',')
    
            if (len(student["courses"])==len(student["grade"])) and student["courses"]!=[''] and student["grade"]!=[''] and student["courses"]!=[' '] and student["grade"]!=[' '] :
                break
            else:
                print(Fore.LIGHTRED_EX+"\U0001F514The number of lessons and the number of grades must be the same !"+Fore.RESET)
        except:
            print(Fore.LIGHTRED_EX+"\U0000274CEnter true value !"+Fore.RESET)

    student["pic"]="false"
    student["locpic"]="no address"

    e = pyttsx3.init()
    e.say("is informatation of Active Student ?")
    e.runAndWait()
    ss = input(Fore.CYAN+"\U0001F514 \ninformatation of Active Student (yes/no)?"+Fore.RESET).lower()

    if ss == "y":
        active_students.append(student)
        login.write_operation("*new Active Student Informatation save*")
        e = pyttsx3.init()
        e.say(" Student Informatation save ")
        e.runAndWait()
    elif ss=='n':
        graduate_students.append(student)
        login.write_operation("*new graduate Student Informatation save*")
        e = pyttsx3.init()
        e.say(" Student Informatation save ")
        e.runAndWait()
    else:
        print(Fore.LIGHTRED_EX+"\U0000274C Wrong choice !"+Fore.RESET)

    login.write_operation("****end Add Operation****")
    print(Fore.CYAN+"\n\U0001F535 Add Operation is End !"+Fore.RESET)
    EndTime2=time.time()
    TotalTime2=EndTime2-StartTime2
    login.write_operation(" total time add pic  : \t"+str(TotalTime2))
    ex = input("\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        clear()

def delete_student():
    StartTime3=time.time()
    clear()
    login.write_operation("****run delete_student****")
    e = pyttsx3.init()
    e.say("is Delete inf of Active Student ?")
    e.runAndWait()
    ss = input(Fore.CYAN+"\U0001F514 \nDelete inf of Active Student (yes/no)?"+Fore.RESET).lower()
    if ss == "y":
        e = pyttsx3.init()
        e.say("Enter Code Melli")
        e.runAndWait()
        code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to delete Active Student : "+Fore.RESET))
        check=False
        for student in active_students:
            if student["code_melli"]==code_melli :
                file =str(student["code_melli"])+".png"
                active_students.remove(student)
                e = pyttsx3.init()
                e.say(" Student Informatation delete ")
                e.runAndWait()
                
                try:
                    location = os.getcwd()+"/pic"
                    path = os.path.join(location, file)
                    os.remove(path)
                    login.write_operation("*The pic aStudent has been deleted*")
                except:
                    print(Fore.LIGHTRED_EX+"**** miss file **** Student has not pic !!! \n"+Fore.RESET)
                    login.write_operation("*The  aStudent has not pic *")

                print(Fore.LIGHTGREEN_EX+"\U0001F514 The Student has been deleted ! "+Fore.RESET)
                login.write_operation("*The aStudent has been deleted*")
                check=True
        if not check : print(Fore.LIGHTRED_EX+" \U0000274C Not Found !"+Fore.RESET)
    elif ss=='n' :
        e = pyttsx3.init()
        e.say("Enter Code Melli")
        e.runAndWait()
        code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to delete Graduate Student : "+Fore.RESET))
        check=False
        for student in graduate_students:
            if student["code_melli"]==code_melli :
                file =str(student["code_melli"])+".png"
                graduate_students.remove(student)
                e = pyttsx3.init()
                e.say(" Student Informatation delete ")
                e.runAndWait()

                try:
                    location = os.getcwd()+"/pic"
                    path = os.path.join(location, file)
                    os.remove(path)
                    login.write_operation("*The pic gStudent has been deleted*")
                except:
                    print(Fore.LIGHTRED_EX+"**** miss file **** Student has not pic !!! \n"+Fore.RESET)
                    login.write_operation("*The  gStudent has not pic *")

                print(Fore.LIGHTGREEN_EX+"\U0001F514 The Student has been deleted ! "+Fore.RESET)
                login.write_operation("*The gStudent has been deleted*")
                check=True
        if not check : print(Fore.LIGHTRED_EX+"\U0000274C Not Found !"+Fore.RESET)
    else:
        print(Fore.LIGHTRED_EX+"\U0000274C Wrong choice !"+Fore.RESET)
    login.write_operation("****end delete_student****")
    EndTime3=time.time()
    TotalTime3=EndTime3-StartTime3
    login.write_operation(" total time del   : \t"+str(TotalTime3))
    print(Fore.CYAN+"\n\U0001F535 Delete Operation is End !"+Fore.RESET)
   
def list_student():
    StartTime4=time.time()
    #clear()
    login.write_operation("****run list_student****")
    print(Fore.MAGENTA+"First_Name","\tLast_Name","\tBirthDay","\tCode_Melli","\tStudent_Code","\tCourses","\tGrade","\tPic"+Fore.RESET)
    print("\n")
    print(Fore.LIGHTGREEN_EX+"------\U0001F7E9\U0001F7E9\U0001F7E9 Active_Students \U0001F7E9\U0001F7E9\U0001F7E9-----"+Fore.RESET)
    c=0
    for student in active_students:
        
    #    print(f"First_Name : \t{ student['first_name']}")
    #    print(f"Last_Name : \t{ student['last_name']}")
    #    print(f"BirthDay : \t{ student['birthday']}")
    #    print(f"Code_Melli : \t{ student['code_melli']}")
    #    print(f"Student_Code : \t{ student['student_code']}")
    #    print(f"Courses : \t{ student['courses']}")
    #    print(f"Grade : \t{ student['grade']}")
        print(Fore.LIGHTYELLOW_EX+"\U0001F7E9------NO:"+str(c+1)+"-----"+Fore.RESET)
        c+=1
        print(str(student['first_name']),"\t"+str(student['last_name']),"\t"+str(student['birthday']),"\t"+Fore.LIGHTGREEN_EX+str(student['code_melli'])+Fore.RESET,"\t"+str(student['student_code']),"\t"+str(student['courses']),"\t"+str(student['grade']),"\t"+str(student["pic"]))
        print("\n")
    else:
        pass

    print(Fore.LIGHTRED_EX+"------\U0001F7E5\U0001F7E5\U0001F7E5 Graduate_Student \U0001F7E5\U0001F7E5\U0001F7E5-----"+Fore.RESET)
    c1=0
    for student in graduate_students:
        print(Fore.LIGHTYELLOW_EX+"\U0001F7E5------NO:"+str(c1+1)+"-----"+Fore.RESET)
        c1+=1
        print(str(student['first_name']),"\t"+str(student['last_name']),"\t"+str(student['birthday']),"\t"+Fore.LIGHTRED_EX+str(student['code_melli'])+Fore.RESET,"\t"+str(student['student_code']),"\t"+str(student['courses']),"\t"+str(student['grade']),"\t"+str(student["pic"]))
        print("\n")
    else:
        pass

    print(Fore.LIGHTBLUE_EX+"-----\U0001F514 sammary \U0001F514-----")
    print("number of Active_Students is : ",c)
    print("number of Graduate_Gtudents is : ",c1)
    print("Total of Students is : \t",c+c1,"\n")
    print(Fore.CYAN+"\n\U0001F535 List Operation is End !\n"+Fore.RESET)

    e = pyttsx3.init()
    e.say(" Students list is redy!")
    e.runAndWait()
    login.write_operation("****end list_student****")
    EndTime4=time.time()
    TotalTime4=EndTime4-StartTime4
    login.write_operation(" total time list students  : \t"+str(TotalTime4))
    ex = input("\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        clear()

def find_student():
    StartTime5=time.time()
    clear()
    login.write_operation("****run find_student****")
    e = pyttsx3.init()
    e.say("is Find inf of Active Student ?")
    e.runAndWait()
    ss = input(Fore.CYAN+"\U0001F514 \nFind inf of Active Student (yes/no)?"+Fore.RESET).lower()
    if ss == "y":
        e = pyttsx3.init()
        e.say("Enter Code Melli")
        e.runAndWait()
        code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to Find Student : "+Fore.RESET))
        check=False
        for student in active_students:
            if student["code_melli"]==code_melli :
                print(Fore.LIGHTGREEN_EX+"---------\U0001F7E9 info Active_students \U0001F7E9---------"+Fore.LIGHTBLUE_EX)
                print(f"First_Name : \t{ student['first_name']}")
                print(f"Last_Name : \t{ student['last_name']}")
                print(f"BirthDay : \t{ str(student['birthday'])}")
                print(f"Code_Melli : \t{ student['code_melli']}")
                print(f"Student_Code : \t{ student['student_code']}")
                age(student['birthday'])
                # print(f"Courses : \t{ student['courses']}")
                # print(f"Grade : \t{ student['grade']}")
                print()
                to_dictionary(student['courses'],student['grade'])
                print()
                mean_scores(student['grade'])
                print("max score is :\t",max(student['grade']))
                print("min score is :\t",min(student['grade']))
                
                print()
                print("Pic: \t",student["pic"])
                print("Address Pic:\t",student["locpic"])
                e = pyttsx3.init()
                e.say(" Found student")
                e.runAndWait()
                #print(student)
                login.write_operation("* find a_student*")
                print(Fore.LIGHTGREEN_EX+"-------------------\U0001F7E9\U0001F7E9\U0001F7E9-------------------"+Fore.RESET)
                check=True
        if not check : print(Fore.LIGHTRED_EX+"\U0000274C Not Found !"+Fore.RESET)
    elif ss=='n':
        e = pyttsx3.init()
        e.say("Enter Code Melli")
        e.runAndWait()
        code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to Find Student : "+Fore.RESET))
        check=False
        for student in graduate_students:
            if student["code_melli"]==code_melli :
                print(Fore.LIGHTRED_EX+"---------\U0001F7E5 info Graduate_students \U0001F7E5---------"+Fore.LIGHTBLUE_EX)
                print(f"First_Name : \t{ student['first_name']}")
                print(f"Last_Name : \t{ student['last_name']}")
                print(f"BirthDay : \t{ str(student['birthday'])}")
                print(f"Code_Melli : \t{ student['code_melli']}")
                print(f"Student_Code : \t{ student['student_code']}")
                age(student['birthday'])
                # print(f"Courses : \t{ student['courses']}")
                # print(f"Grade : \t{ student['grade']}")
                print()
                to_dictionary(student['courses'],student['grade'])
                print()
                mean_scores(student['grade'])
                print("max score is :\t",max(student['grade']))
                print("min score is :\t",min(student['grade']))
                
                print()
                print("Pic: \t",student["pic"])
                print("Address Pic:\t",student["locpic"])
                e = pyttsx3.init()
                e.say(" Found student")
                e.runAndWait()
                login.write_operation("* find g_student*")
                print(Fore.LIGHTRED_EX+"-------------------\U0001F7E5\U0001F7E5\U0001F7E5--------------------"+Fore.RESET)
                check=True
        if not check : print(Fore.LIGHTRED_EX+"\U0000274C Not Found !"+Fore.RESET)
    else :
        print(Fore.LIGHTRED_EX+"\U0000274C Wrong choice !"+Fore.RESET)
    print(Fore.CYAN+"\n\U0001F535 Found Operation is End !"+Fore.RESET)
    login.write_operation("****end find_student****")
    EndTime5=time.time()
    TotalTime5=EndTime5-StartTime5
    login.write_operation(" total time find  : \t"+str(TotalTime5))
    ex = input("\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        clear()

def edit_student():
    StartTime6=time.time()
    clear()
    login.write_operation("****run edit_student****")
    e = pyttsx3.init()
    e.say("is Edit inf of Active Student ?")
    e.runAndWait()
    ss = input(Fore.CYAN+"\U0001F514 \nEdit inf of Active Student (yes/no)?"+Fore.RESET).lower()
    if ss == "y":
        e = pyttsx3.init()
        e.say("Enter Code Melli")
        e.runAndWait()
        code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to Edit Student : "+Fore.RESET))
        check=False
        for student in active_students:
            if student["code_melli"]==code_melli :
                print(Fore.MAGENTA+"\U0001F7E9 Found !"+Fore.RESET)
                login.write_operation("*Found a_stutent for edit_student*")
                print(Fore.LIGHTGREEN_EX+"---------\U0001F7E9 EDIT info Active_students \U0001F7E9---------"+Fore.RESET)

                while True :
                    try:
                        e = pyttsx3.init()
                        e.say("Enter first_name ,and last_name")
                        e.runAndWait()
                        student["first_name"]=input(Fore.LIGHTYELLOW_EX+"\U0001F4CCEnter First_Name of Student: "+Fore.LIGHTBLUE_EX).title()
                        student["last_name"]=input(Fore.LIGHTYELLOW_EX+"\U0001F4CC\U0001F4CCEnter Last_Name of Student: "+Fore.LIGHTBLUE_EX).title()
                        if student["first_name"]!=' ' and student["last_name"]!=' ' and student["first_name"]!='' and student["last_name"]!='' :
                            break
                        else:
                            print(Fore.LIGHTRED_EX+"\U0001F514The number of first_name and last_name biger than '1' !"+Fore.RESET)
                    except:
                        print(Fore.LIGHTRED_EX+"\U0000274CEnter true value !"+Fore.RESET)

                while True :
                    try:
                        m=[]
                        e = pyttsx3.init()
                        e.say("Enter birthday")
                        e.runAndWait()
                        m=input(Fore.LIGHTYELLOW_EX+"\U0001F4C5Enter birthday of Student : yyyy,mm,dd "+Fore.LIGHTBLUE_EX).split(",")
                        if (len(m[0])==4 and 0<len(m[1])<3 and 0<len(m[2])<3 and m[0].isdigit() and m[1].isdigit() and m[2].isdigit() ):
                            yyyy,mm,dd=int(m[0]),int(m[1]),int(m[2])
                            #student["birthday"]= datetime.datetime(yyyy,mm,dd)
                            student["birthday"]= jdatetime.date(yyyy,mm,dd)

                            break
                        else:
                            print(Fore.LIGHTRED_EX+"\U0000274CFor Example:\t1400,6,23 !"+Fore.RESET)
                    except:
                        print(Fore.LIGHTRED_EX+"\U0000274C Month betwwn 1-12 \tDay betwwn 1-31"+Fore.RESET)
                while True :
                    try:
                        e = pyttsx3.init()
                        e.say("code melli")
                        e.runAndWait()
                        student["code_melli"]=int(input(Fore.LIGHTYELLOW_EX+"\U0001F4A0Enter Numbers of Code_Melli : "+Fore.LIGHTBLUE_EX))
                        if (1000000000<=student["code_melli"]<10000000000 ) :
                            break
                        else:
                            print(Fore.LIGHTRED_EX+"\U0001F514Number Shoud be 10 Digits !"+Fore.RESET)
                    except :
                        print(Fore.LIGHTRED_EX+"\U0000274CEnter Number !"+Fore.RESET)
                while True:
                    try:
                        e = pyttsx3.init()
                        e.say("student code")
                        e.runAndWait()
                        student["student_code"]=int(input(Fore.LIGHTYELLOW_EX+"\U0001F393Enter Numbers of Student_Code : "+Fore.LIGHTBLUE_EX))
                        if str(student["student_code"]).isdigit() :
                            break
                    except:
                        print(Fore.LIGHTRED_EX+"\U0000274CEnter Number !"+Fore.RESET)
                while True:
                    try:
                        e = pyttsx3.init()
                        e.say("Enter courses ,and grades")
                        e.runAndWait()
                        student["courses"]=input(Fore.LIGHTYELLOW_EX+"\U0001F535Enter List of Courses (between Course insert ','): \n"+Fore.LIGHTBLUE_EX).split(',')
                        student["grade"]=input(Fore.LIGHTYELLOW_EX+"\U0001F7E3Enter List of Grade (between Grade insert ','): \n"+Fore.LIGHTBLUE_EX).split(',')
                
                        if (len(student["courses"])==len(student["grade"])) and student["courses"]!=[''] and student["grade"]!=[''] and student["courses"]!=[' '] and student["grade"]!=[' '] :
                            break
                        else:
                            print(Fore.LIGHTRED_EX+"\U0001F514The number of lessons and the number of grades must be the same !"+Fore.RESET)
                    except:
                            print(Fore.LIGHTRED_EX+"\U0000274CEnter true value !"+Fore.RESET)
                print(Fore.LIGHTGREEN_EX+"\U0001F514 Changed !"+Fore.RESET)
                login.write_operation("*Changed a_stutent for edit_student*")
                e = pyttsx3.init()
                e.say(" Changed !")
                e.runAndWait()

                print(Fore.LIGHTRED_EX+"-------------------\U0001F7E9\U0001F7E9\U0001F7E9-------------------"+Fore.RESET)
                check=True
        if not check : print(Fore.LIGHTRED_EX+"\U0000274C Not Found !"+Fore.RESET)
    elif ss=='n':
        e = pyttsx3.init()
        e.say("Enter Code Melli")
        e.runAndWait()
        code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to Edit Student : "+Fore.RESET))
        check=False
        for student in graduate_students:
            if student["code_melli"]==code_melli :
                print(Fore.MAGENTA+"\U0001F7E5 Found !"+Fore.RESET)
                login.write_operation("*Found g_stutent for edit_student*")
                print(Fore.LIGHTRED_EX+"---------\U0001F7E5 EDIT info Graduate_students \U0001F7E5---------"+Fore.RESET)

                while True :
                    try:
                        e = pyttsx3.init()
                        e.say("Enter first_name ,and last_name")
                        e.runAndWait()
                        student["first_name"]=input(Fore.LIGHTYELLOW_EX+"\U0001F4CCEnter First_Name of Student: "+Fore.LIGHTBLUE_EX).title()
                        student["last_name"]=input(Fore.LIGHTYELLOW_EX+"\U0001F4CC\U0001F4CCEnter Last_Name of Student: "+Fore.LIGHTBLUE_EX).title()
                        if student["first_name"]!=' ' and student["last_name"]!=' ' and student["first_name"]!='' and student["last_name"]!='' :
                            break
                        else:
                            print(Fore.LIGHTRED_EX+"\U0001F514The number of first_name and last_name biger than '1' !"+Fore.RESET)
                    except:
                        print(Fore.LIGHTRED_EX+"\U0000274CEnter true value !"+Fore.RESET)

                while True :
                    try:
                        m=[]
                        e = pyttsx3.init()
                        e.say("Enter birthday")
                        e.runAndWait()
                        m=input(Fore.LIGHTYELLOW_EX+"\U0001F4C5Enter birthday of Student : yyyy,mm,dd "+Fore.LIGHTBLUE_EX).split(",")
                        if (len(m[0])==4 and 0<len(m[1])<3 and 0<len(m[2])<3 and m[0].isdigit() and m[1].isdigit() and m[2].isdigit() ):
                            yyyy,mm,dd=int(m[0]),int(m[1]),int(m[2])
                            #student["birthday"]= datetime.datetime(yyyy,mm,dd)
                            student["birthday"]= jdatetime.date(yyyy,mm,dd)
                            break
                        else:
                            print(Fore.LIGHTRED_EX+"\U0000274CFor Example:\t1400,6,23 !"+Fore.RESET)
                    except:
                        print(Fore.LIGHTRED_EX+"\U0000274C Month betwwn 1-12 \tDay betwwn 1-31"+Fore.RESET)
                while True :
                    try:
                        e = pyttsx3.init()
                        e.say("code melli")
                        e.runAndWait()
                        student["code_melli"]=int(input(Fore.LIGHTYELLOW_EX+"\U0001F4A0Enter Numbers of Code_Melli : "+Fore.LIGHTBLUE_EX))
                        if (1000000000<=student["code_melli"]<10000000000 ) :
                            break
                        else:
                            print(Fore.LIGHTRED_EX+"\U0001F514Number Shoud be 10 Digits !"+Fore.RESET)
                    except :
                        print(Fore.LIGHTRED_EX+"\U0000274CEnter Number !"+Fore.RESET)
                while True:
                    try:
                        e = pyttsx3.init()
                        e.say("student code")
                        e.runAndWait()
                        student["student_code"]=int(input(Fore.LIGHTYELLOW_EX+"\U0001F393Enter Numbers of Student_Code : "+Fore.LIGHTBLUE_EX))
                        if str(student["student_code"]).isdigit() :
                            break
                    except:
                        print(Fore.LIGHTRED_EX+"\U0000274CEnter Number !"+Fore.RESET)
                while True:
                    try:
                        e = pyttsx3.init()
                        e.say("Enter courses ,and grades")
                        e.runAndWait()
                        student["courses"]=input("\U0001F535Enter List of Courses (between Course insert ','): \n"+Fore.LIGHTBLUE_EX).split(',')
                        student["grade"]=input("\U0001F7E3Enter List of Grade (between Grade insert ','): \n"+Fore.LIGHTBLUE_EX).split(',')
                
                        if (len(student["courses"])==len(student["grade"])) and student["courses"]!=[''] and student["grade"]!=[''] and student["courses"]!=[' '] and student["grade"]!=[' '] :
                            break
                        else:
                            print(Fore.LIGHTRED_EX+"\U0001F514The number of lessons and the number of grades must be the same !"+Fore.RESET)
                    except:
                        print(Fore.LIGHTRED_EX+"\U0000274CEnter true value !"+Fore.RESET)
                print(Fore.LIGHTGREEN_EX+"\U0001F514 Changed !"+Fore.RESET)
                login.write_operation("*Changed g_stutent for edit_student*")
                e = pyttsx3.init()
                e.say(" Changed !")
                e.runAndWait()
                print(Fore.LIGHTRED_EX+"-------------------\U0001F7E5\U0001F7E5\U0001F7E5--------------------"+Fore.RESET)
                check=True
        if not check : print(Fore.LIGHTRED_EX+"\U0000274C Not Found !"+Fore.RESET)
    else:
        print(Fore.LIGHTRED_EX+"\U0000274C Wrong choice !"+Fore.RESET)
    print(Fore.CYAN+"\n\U0001F535 Edit Operation is End !"+Fore.RESET)
    login.write_operation("****end edit_student****")
    EndTime6=time.time()
    TotalTime6=EndTime6-StartTime6
    login.write_operation(" total time edit : \t"+str(TotalTime6))
    ex = input("\n\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        clear()

def save_student():
    StartTime7=time.time()
    login.write_operation("****run save_student****")
    try:
    
        with open("active_students.db","wb") as as_db:
            pickle.dump(active_students,as_db)
        with open("graduate_students.db","wb") as gs_db:
            pickle.dump(graduate_students,gs_db)
        print(Fore.LIGHTGREEN_EX+"\n\U0001F514 Save is Done!"+Fore.RESET)
        login.write_operation("*Save is Done!*")
        e = pyttsx3.init()
        e.say(" Save is Done!")
        e.runAndWait()
    except:
        print(Fore.LIGHTRED_EX+"\n\U0000274C Not Save !"+Fore.RESET)
        login.write_operation("*Not Save!*")
        e = pyttsx3.init()
        e.say(" Not Save !")
        e.runAndWait()

    print(Fore.CYAN+"\n\U0001F535 Save Operation is End !"+Fore.RESET)
    login.write_operation("****end save_student****")
    EndTime7=time.time()
    TotalTime7=EndTime7-StartTime7
    login.write_operation(" total time save  : \t"+str(TotalTime7))
    ex = input("\n\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        clear()

def move_student():
    StartTime8=time.time()
    clear()
    login.write_operation("****run move_student****")
    try:
        code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to delete Student : "+Fore.RESET))
        check=False
        for student in active_students:
            if student["code_melli"]==code_melli :
                check=True
                temp=student
                active_students.remove(student)
                graduate_students.append(temp)
                print(Fore.LIGHTGREEN_EX+"\U0001F514 Transferred !"+Fore.RESET)
                login.write_operation("*Transferred !*")
                e = pyttsx3.init()
                e.say(" Transferred !")
                e.runAndWait()

        if not check : print(Fore.LIGHTRED_EX+"\U0000274C Not Found !"+Fore.RESET) 
    except:
        print(Fore.LIGHTRED_EX+"\U0000274CFalse value !"+Fore.RESET)

    print(Fore.CYAN+"\n\U0001F535 Move Operation is End !"+Fore.RESET) 
    login.write_operation("****end move_student****") 
    EndTime8=time.time()
    TotalTime8=EndTime8-StartTime8
    login.write_operation(" total time move : \t"+str(TotalTime8))
    ex = input("\n\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        clear()

def mean_scores(i):
    sum=0
    count=0
    for j in i :
        sum+=int(j)
        count+=1
    print("mean scors is :\t",sum/count)

def age(x):
    #now = datetime.datetime.now()
    now = jdatetime.date.today()
    print("age student is : ",now.year-x.year,"(years)")

def plot_student():
    StartTime9=time.time()
    clear()
    login.write_operation("****run plot_student****")
    e = pyttsx3.init()
    e.say("is Plot inf of Active Student ?")
    e.runAndWait()
    ss = input(Fore.CYAN+"\U0001F514 \n Plot inf of Active Student (yes/no)?"+Fore.RESET).lower()
    if ss == "y":
        try:
            e = pyttsx3.init()
            e.say("Enter Code Melli")
            e.runAndWait()
            code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to Plot Student : "+Fore.RESET))
            check=False
            for student in active_students:
                if student["code_melli"]==code_melli :
                    print(Fore.LIGHTGREEN_EX+"---------\U0001F7E9 info Active_students \U0001F7E9---------"+Fore.LIGHTBLUE_EX)
                    print(f"First_Name : \t{ student['first_name']}")
                    print(f"Last_Name : \t{ student['last_name']}")
                    print(f"Student_Code : \t{ student['student_code']}")
                    x= np.array(student['courses'])
                    y = np.array([int(i) for i in student['grade']])
                    plt.title("Grade of Student")
                    plt.xlabel("Courses")
                    plt.ylabel("Grade")
                    plt.bar(x,y ,color = "hotpink")
                    e = pyttsx3.init()
                    e.say(Fore.MAGENTA+" plot is running "+Fore.RESET)
                    login.write_operation("*plot a_s is running *")
                    e.runAndWait()
                    plt.show()
                    print(Fore.LIGHTGREEN_EX+"-------------------\U0001F7E9\U0001F7E9\U0001F7E9-------------------"+Fore.RESET)
                    check=True
            if not check : print(Fore.LIGHTRED_EX+"\U0000274C Not Found !"+Fore.RESET)
        except:
            print(Fore.LIGHTRED_EX+"\U0000274C enter number !"+Fore.RESET)
    else :
        try:
            e = pyttsx3.init()
            e.say("Enter Code Melli")
            e.runAndWait()
            code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to Plot Student : "+Fore.RESET))
            check=False
            for student in graduate_students:
                if student["code_melli"]==code_melli :
                    print(Fore.LIGHTRED_EX+"---------\U0001F7E5 info Graduate_students \U0001F7E5---------"+Fore.LIGHTBLUE_EX)
                    print(f"First_Name : \t{ student['first_name']}")
                    print(f"Last_Name : \t{ student['last_name']}")
                    print(f"Student_Code : \t{ student['student_code']}")
                    x= np.array(student['courses'])
                    y = np.array([int(i) for i in student['grade']])
                    plt.title("Grade of Student")
                    plt.xlabel("Courses")
                    plt.ylabel("Grade")
                    plt.bar(x,y ,color = "hotpink")
                    e = pyttsx3.init()
                    e.say(Fore.MAGENTA+" plot is running "+Fore.RESET)
                    login.write_operation("****plot g_s is running ****")
                    e.runAndWait()
                    plt.show()
                    print(Fore.LIGHTRED_EX+"-------------------\U0001F7E5\U0001F7E5\U0001F7E5--------------------"+Fore.RESET)
                    check=True
            if not check : print(Fore.LIGHTRED_EX+"\U0000274C Not Found !"+Fore.RESET)
        except:
            print(Fore.LIGHTRED_EX+"\U0000274C enter number !"+Fore.RESET)
    login.write_operation("*end plot_student*")
    EndTime9=time.time()
    TotalTime9=EndTime9-StartTime9
    login.write_operation(" total time plot  : \t"+str(TotalTime9))

def add_pic():
    StartTime10=time.time()
    clear()
    login.write_operation("****run add_pic****")
    e = pyttsx3.init()
    e.say("is Find inf of Active Student ?")
    e.runAndWait()
    ss = input(Fore.CYAN+"\U0001F514 \nFind inf of Active Student (yes/no)?"+Fore.RESET).lower()
    if ss == "y":
        e = pyttsx3.init()
        e.say("Enter Code Melli")
        e.runAndWait()
        code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to Find Student : "+Fore.RESET))
        check=False
        for student in active_students:
            if student["code_melli"]==code_melli :
                while True:
                    w=input(Fore.LIGHTBLUE_EX+"Enter address new '.jpg' pic \n for example: \t hasan.jpg \n")
                    img = cv2.imread(w,-1)
                    print(Fore.MAGENTA+"pre view pic\n for continue close pic window\n"+Fore.RESET)
                    e = pyttsx3.init()
                    e.say(" pre view pic\n for continue close pic window\n ")
                    login.write_operation("*pre view pic a_s*")
                    e.runAndWait()
                    # cv2.imshow(str(student["code_melli"]),img)
                    # cv2.waitKey(0) ,0xFF
                    # cv2.destroyAllWindows()

                    
                    # Get user supplied values
                    imagePath = w
                    cascPath = "tools/haarcascade_frontalface_default.xml"

                    # Create the haar cascade
                    faceCascade = cv2.CascadeClassifier(cascPath)

                    # Read the image
                    image = cv2.imread(imagePath)
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                    # Detect faces in the image
                    faces = faceCascade.detectMultiScale(
                        gray,
                        scaleFactor=1.1,
                        minNeighbors=20,
                        minSize=(30, 30))
                    print(""+Fore.LIGHTYELLOW_EX)
                    print("Found {0} faces!".format(len(faces)))
                    print(""+Fore.RESET)

                    # Draw a rectangle around the faces
                    for (x, y, w, h) in faces:
                        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

                    cv2.imshow("Faces found", image)
                    cv2.waitKey(0)

                    
                    if (len(faces))==1 :
                        break
                    else:
                        print(Fore.LIGHTRED_EX+"enter url better pic !!"+Fore.RESET)


                k = input(Fore.LIGHTYELLOW_EX+"enter 's' for save & 'n' for new load"+Fore.RESET)
                if k == 's':
                    name="pic/"+str(student["code_melli"])+".png"
                    student["locpic"]=name
                    cv2.imwrite(name,img)
                    student["pic"]="true"
                    clear()
                    print(Fore.LIGHTGREEN_EX+"Save Done !"+Fore.RESET)
                    login.write_operation("*Save Done pic a_s*")
                else:
                    clear()
                    print(Fore.LIGHTRED_EX+"Not save !"+Fore.RESET)
                    login.write_operation("*Not save pic a_s*")
                    
                print(Fore.LIGHTGREEN_EX+"-------------------\U0001F7E9\U0001F7E9\U0001F7E9-------------------"+Fore.RESET)
                check=True
        if not check : print(Fore.LIGHTRED_EX+"\U0000274C Not Found !"+Fore.RESET)
    elif ss=='n':
        e = pyttsx3.init()
        e.say("Enter Code Melli")
        e.runAndWait()
        code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to Find Student : "+Fore.RESET))
        check=False
        for student in graduate_students:
            if student["code_melli"]==code_melli :
                while True:
                    w=input(Fore.LIGHTBLUE_EX+"Enter address new '.jpg' pic \n for example: \t hasan.jpg \n")
                    img = cv2.imread(w,-1)
                    print(Fore.MAGENTA+"pre view pic\n for continue close pic window\n"+Fore.RESET)
                    e = pyttsx3.init()
                    e.say(" pre view pic\n for continue close pic window\n ")
                    login.write_operation("*pre view pic a_s*")
                    e.runAndWait()
                    # cv2.imshow(str(student["code_melli"]),img)
                    # cv2.waitKey(0) ,0xFF
                    # cv2.destroyAllWindows()

                    
                    # Get user supplied values
                    imagePath = w
                    cascPath = "tools/haarcascade_frontalface_default.xml"

                    # Create the haar cascade
                    faceCascade = cv2.CascadeClassifier(cascPath)

                    # Read the image
                    image = cv2.imread(imagePath)
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                    # Detect faces in the image
                    faces = faceCascade.detectMultiScale(
                        gray,
                        scaleFactor=1.1,
                        minNeighbors=20,
                        minSize=(30, 30))
                    print(""+Fore.LIGHTYELLOW_EX)
                    print("Found {0} faces!".format(len(faces)))
                    print(""+Fore.RESET)
                    # Draw a rectangle around the faces
                    for (x, y, w, h) in faces:
                        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

                    cv2.imshow("Faces found", image)
                    cv2.waitKey(0)

                    
                    if (len(faces))==1 :
                        break
                    else:
                        print(Fore.LIGHTRED_EX+"enter url better pic !!"+Fore.RESET)


                k = input(Fore.LIGHTYELLOW_EX+"enter 's' for save & 'n' for new load"+Fore.RESET)
                if k == 's':
                    name="pic/"+str(student["code_melli"])+".png"
                    student["locpic"]=name
                    cv2.imwrite(name,img)
                    student["pic"]="true"
                    clear()
                    print(Fore.LIGHTGREEN_EX+"Save Done !"+Fore.RESET)
                    login.write_operation("*Save Done pic g_s*")
                else:
                    clear()
                    print(Fore.LIGHTRED_EX+"Not save !"+Fore.RESET)
                    login.write_operation("*Not save pic g_s*")
            
                print(Fore.LIGHTRED_EX+"-------------------\U0001F7E5\U0001F7E5\U0001F7E5--------------------"+Fore.RESET)
                check=True
        if not check : print(Fore.LIGHTRED_EX+"\U0000274C Not Found !"+Fore.RESET)
    else :
        print(Fore.LIGHTRED_EX+"\U0000274C Wrong choice !"+Fore.RESET)
    print(Fore.CYAN+"\n\U0001F535 Add pic Operation is End !"+Fore.RESET)
    login.write_operation("****end add_pic****")
    EndTime10=time.time()
    TotalTime10=EndTime10-StartTime10
    login.write_operation(" total time add pic  : \t"+str(TotalTime10))
    ex = input("\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        clear()

def all_pic():
    StartTime11=time.time()
    pica=0
    picg=0
    login.write_operation("****run all_pic****")
    print(Fore.MAGENTA+"code_melli"+"\t"+"pic"+"\t"+"locpic\n"+Fore.RESET)
    print(Fore.LIGHTGREEN_EX+"------\U0001F7E9\U0001F7E9\U0001F7E9 Pic Active_Students \U0001F7E9\U0001F7E9\U0001F7E9-----"+Fore.RESET)
    c=0
    for student in active_students:
        print(Fore.LIGHTYELLOW_EX+"\U0001F7E9------NO:"+str(c+1)+"-----"+Fore.LIGHTBLUE_EX)
        c+=1
        print(str(student["code_melli"])+"\t",str(student["pic"])+"\t",str(student["locpic"]))

        if(student["pic"]=='true'): pica+=1
            
        print("\n")
    else:
        pass

    print(Fore.LIGHTRED_EX+"------\U0001F7E5\U0001F7E5\U0001F7E5 Pic Graduate_Student \U0001F7E5\U0001F7E5\U0001F7E5-----"+Fore.RESET)
    c1=0
    for student in graduate_students:
        print(Fore.LIGHTYELLOW_EX+"\U0001F7E5------NO:"+str(c1+1)+"-----"+Fore.LIGHTBLUE_EX)
        c1+=1
        print(str(student["code_melli"])+"\t",str(student["pic"])+"\t",str(student["locpic"])) 
        if(student["pic"]=='true'): picg+=1       
        print("\n")
    else:
        pass

    print(Fore.LIGHTYELLOW_EX+"-----\U0001F514 sammary \U0001F514-----")
    print("all number of Active_Students is : ",c)
    print("pic number of Active_Students is : ",pica,"\n")
    print("all number of Graduate_Gtudents is : ",c1)
    print("pic number of Graduate_Gtudents is : ",picg,"\n")
    print("Total of Students is : \t",c+c1)
    print("Total of Students pics is : \t",pica+picg,"\n"+Fore.RESET)

    e = pyttsx3.init()
    e.say(Fore.CYAN+" Lists Pics Operation is running! "+Fore.RESET)
    e.runAndWait()
    print("\n\U0001F535 List Pics Operation is End !\n")
    login.write_operation("****end all_pic****")
    EndTime11=time.time()
    TotalTime11=EndTime11-StartTime11
    login.write_operation(" total time all pic  : \t"+str(TotalTime11))
    ex = input("\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        clear()

def show_pic():
    StartTime12=time.time()
    clear()
    login.write_operation("****run show_pic****")
    e = pyttsx3.init()
    e.say("is Find inf of Active Student ?")
    e.runAndWait()
    ss = input(Fore.CYAN+"\U0001F514 \nFind inf of Active Student (yes/no)?"+Fore.RESET).lower()
    if ss == "y":
        e = pyttsx3.init()
        e.say("Enter Code Melli")
        e.runAndWait()
        code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to Find Student : "+Fore.RESET))
        check=False
        for student in active_students:
            if student["code_melli"]==code_melli and student["pic"]=='true':

                print(Fore.LIGHTGREEN_EX+"---------\U0001F7E9 info Active_students \U0001F7E9---------"+Fore.LIGHTBLUE_EX)
                print("Address Pic:\t",student["locpic"])
                w=student["locpic"]
                img = cv2.imread(w,-1)
                print(Fore.MAGENTA+"view pic\n for continue close pic window\n")
                e = pyttsx3.init()
                e.say(" pre view pic\n for continue close pic window\n ")
                login.write_operation("*pre view pic a_s *")
                e.runAndWait()
                cv2.imshow(str(student["code_melli"]),img)
                cv2.waitKey(0) ,0xFF
                cv2.destroyAllWindows()
                
                print(Fore.LIGHTGREEN_EX+"-------------------\U0001F7E9\U0001F7E9\U0001F7E9-------------------"+Fore.RESET)
                check=True
        if not check : print(Fore.LIGHTRED_EX+"\U0000274C Not Found !"+Fore.RESET)
    elif ss=='n':
        e = pyttsx3.init()
        e.say("Enter Code Melli")
        e.runAndWait()
        code_melli=int(input(Fore.LIGHTYELLOW_EX+"Enter Code_Melli to Find Student : "+Fore.RESET))
        check=False
        for student in graduate_students:
            if student["code_melli"]==code_melli and student["pic"]=='true':

                print(Fore.LIGHTRED_EX+"---------\U0001F7E5 info Graduate_students \U0001F7E5---------"+Fore.LIGHTBLUE_EX)
                print("Address Pic:\t",student["locpic"])
                w=student["locpic"]
                img = cv2.imread(w,-1)
                print(Fore.MAGENTA+"view pic\n for continue close pic window\n")
                e = pyttsx3.init()
                e.say(" pre view pic\n for continue close pic window\n ")
                login.write_operation("*pre view pic g_s *")
                e.runAndWait()
                cv2.imshow(str(student["code_melli"]),img)
                cv2.waitKey(0) ,0xFF
                cv2.destroyAllWindows()

                print(Fore.LIGHTRED_EX+"-------------------\U0001F7E5\U0001F7E5\U0001F7E5--------------------"+Fore.RESET)
                check=True
        if not check : print(Fore.LIGHTRED_EX+"\U0000274C Not Found !"+Fore.RESET)
    else :
        print(Fore.LIGHTRED_EX+"\U0000274C Wrong choice !"+Fore.RESET)
    print(Fore.CYAN+"\n\U0001F535 Show pic Operation is End !"+Fore.RESET)
    login.write_operation("****end show_pic****")
    EndTime12=time.time()
    TotalTime12=EndTime12-StartTime12
    login.write_operation(" total time show pic  : \t"+str(TotalTime12))
    ex = input("\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        clear()

def to_dictionary(keys, values):
    print("List of Course with Grade:",end="")
    df = pd.DataFrame(values, index= keys, columns=[' '])
    print(df)
    
def output_qr():
    StartTime13=time.time()
    clear()
    login.write_operation("****run output_qr ****")
    e = pyttsx3.init()
    e.say("are you delete all QR then new output ?")
    e.runAndWait()
    qr=input(Fore.LIGHTYELLOW_EX+"are you delete all QR then new output 'y' to yes :\n "+Fore.RESET)
    if qr=='y':
        dir_list_a = os.listdir("qrcode/stu/a/")
        dir_list_g = os.listdir("qrcode/stu/g/")
        try:
            for i in dir_list_a:
                location1 = os.getcwd()+"/qrcode/stu/a/"
                path1 = os.path.join(location1, i)
                os.remove(path1)

            for g in dir_list_g:
                location2 = os.getcwd()+"/qrcode/stu/g/"
                path2 = os.path.join(location2, g)
                os.remove(path2)
            e = pyttsx3.init()
            e.say(" old QR codes is deleted! ")
            login.write_operation("*old QR codes is deleted! *")
            e.runAndWait()
        except:
            pass
    
    try:
        for student in active_students:
            name=str(student["code_melli"])
            urll="qrcode/stu/a/"+name+".png"
            data = str(student)
            img = qrcode.make(data)
            img.save(urll)
        for student in graduate_students:
            name=str(student["code_melli"])
            urll="qrcode/stu/g/"+name+".png"
            data = str(student)
            img = qrcode.make(data)
            img.save(urll)
        print(Fore.LIGHTGREEN_EX+"QR Code of all student is save as png file \n"+Fore.RESET)
        login.write_operation("*QR Code of all student is save as png file *")
        e = pyttsx3.init()
        e.say(" QR Code of all student is save as png file \n")
        e.runAndWait()
    except:
        print(Fore.LIGHTRED_EX+"QR Code can not save!!! \n"+Fore.RESET)
    print(Fore.CYAN+"\n\U0001F535 QR output Operation is End !\n"+Fore.RESET)
    login.write_operation("****end output_qr ****")
    EndTime13=time.time()
    TotalTime13=EndTime13-StartTime13
    login.write_operation(" total time output qr  : \t"+str(TotalTime13))
    ex = input("\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        clear()

def create_email():
        StartTime14=time.time()
        clear()
        login.write_operation("****run create_email ****")
        print(Fore.LIGHTBLUE_EX+"**** list email student ****"+Fore.RESET)
        emm=[]
        emm2=[]
        emaillist=[]
        
        print(Fore.LIGHTYELLOW_EX+"**** active student ****")
        for student in active_students:
            iut=dict()
            email_a=str(student["first_name"])+"_"+str(student["last_name"])+"_"+str(student["code_melli"])[0:5]+"@iut.com"
            email_a=email_a.lower()
            iut["code_melli"]=student["code_melli"]
            iut["first_name"]=student["first_name"]
            iut["last_name"]=student["last_name"]
            iut["email"]=email_a
            emm.append(iut)
            print(Fore.LIGHTGREEN_EX+str(iut["code_melli"]),"   --->   ",iut["email"])

        print(Fore.LIGHTYELLOW_EX+"**** graduate student ****")
        for student in graduate_students:
            iut=dict()
            email_g=str(student["first_name"])+"_"+str(student["last_name"])+"_"+str(student["code_melli"])[0:5]+"@iut.com"
            email_g=email_g.lower()
            iut["code_melli"]=student["code_melli"]
            iut["first_name"]=student["first_name"]
            iut["last_name"]=student["last_name"]
            iut["email"]=email_g
            emm2.append(iut)
            print(Fore.LIGHTRED_EX+str(iut["code_melli"]),"   --->   ",iut["email"])

        emaillist=[emm,emm2]
        print("\n")

        # print(emm,end="\n\n\n")
        # print(emm2,end="\n\n\n")
        # print(emaillist,end="\n\n\n")
        savee=input(Fore.LIGHTBLUE_EX+"are you save email.db ?'y'=yes ")
        if savee=='y':
            with open("email.db","wb") as em_db:
                pickle.dump(emaillist,em_db)
            clear()
            print(Fore.LIGHTGREEN_EX+"\n\U0001F514  'iut' email is save Done!")
            login.write_operation("*'iut' email is save Done!*")
        
        print("\n\U0001F514  'iut' email is Create Done!")
        e = pyttsx3.init()
        e.say(Fore.LIGHTBLUE_EX+" 'iut' email is Create Done!")
        e.runAndWait()

        print(Fore.CYAN+"\n\U0001F535 'iut' email Operation is End !\n"+Fore.RESET)
        login.write_operation("****end create_email ****")
        EndTime14=time.time()
        TotalTime14=EndTime14-StartTime14
        login.write_operation(" total time email.db  : \t"+str(TotalTime14))
        ex = input("\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
        if not ex =="" : 
            clear()

def add_stu_random():
    StartTime15=time.time()
    clear()
    login.write_operation("****run add_stu_random ****")
    while True:
        try:
            num_=int(input(Fore.LIGHTYELLOW_EX+"how many student add?\n"+Fore.RESET))
            break
        except:
            clear()
            print(Fore.LIGHTRED_EX+"enter number!!!\n"+Fore.RESET)

    for n in range(1,num_+1):
        print(Fore.LIGHTMAGENTA_EX+"\nNO : "+Fore.RESET,n)
        fake = Faker()
        student=dict()
        
        name_family=fake.name()
        name_family = name_family.split(' ')  
        student["first_name"]=name_family[0].title()
        student["last_name"]=name_family[1].title()
                
        m=[]
        list=[]
        fdate=fake.date()
        m=fdate.split('-')
        yyyy,mm,dd=int(m[0]),int(m[1]),int(m[2])
        student["birthday"]= jdatetime.date.fromgregorian(day=dd,month=mm,year=yyyy)
        

        digits = string.digits
        password = "".join(choice(digits)  #codemeli
        for x in range(10))
        student["code_melli"]=int(password)
            

        ssn=fake.ssn()
        ssn=ssn.split('-')
        ssn=''.join(ssn)       
        student["student_code"]=int(ssn)
            

        lst_course_random=[]
        for i in range(3):
            course=letters = string.ascii_letters
            course_ = "".join(choice(course)  
            for x in range(4))
            lst_course_random.append(course_)
        student["courses"]=lst_course_random

        lst_grade_random=[]
        for j in range(3):
            grade= string.digits
            grade_= "".join(choice(grade)  
            for x in range(2))
            grade_=int((int(grade_)*20 )/100)
            lst_grade_random.append(grade_)                
        student["grade"]=lst_grade_random
        
                

        student["pic"]="false"
        student["locpic"]="no address"

        e = pyttsx3.init()
        e.say("is informatation of Active Student ?")
        e.runAndWait()
        ss = input(Fore.LIGHTYELLOW_EX+"\U0001F514 \ninformatation of Active Student (yes/no)?"+Fore.RESET).lower()
        if ss == "y":
            active_students.append(student)
            login.write_operation("*Random a_Student Informatation save *")
            e = pyttsx3.init()
            e.say("Random Student Informatation save ")
            e.runAndWait()
            print(Fore.LIGHTGREEN_EX+"Random a_Student Informatation save \n"+Fore.RESET)
        elif ss=='n':
            graduate_students.append(student)
            login.write_operation("*Random g_Student Informatation save *")
            e = pyttsx3.init()
            e.say("Random Student Informatation save ")
            e.runAndWait()
            print(Fore.LIGHTRED_EX+"Random a_Student Informatation save \n"+Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX+"\U0000274C Wrong choice ! \nOne of your choices was lost due to a mistake.\n"+Fore.RESET)

    print(Fore.CYAN+"\n\U0001F535 Random Add Operation is End !"+Fore.RESET)
    login.write_operation("****end add_stu_random ****")
    EndTime15=time.time()
    TotalTime15=EndTime15-StartTime15
    login.write_operation(" total time add_stu_random  : \t"+str(TotalTime15))
    ex = input("\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        clear()

def handwriting():
    StartTime16=time.time()
    clear()
    login.write_operation("****run handwriting ****")
    e = pyttsx3.init()
    e.say("handwriting is running maybe a few sec long!!!")
    e.runAndWait()
    print(Fore.LIGHTYELLOW_EX+"handwriting is running maybe a few sec long!!! :\n ")
    e = pyttsx3.init()
    e.say("are you delete all handwriting then new output?")
    e.runAndWait()
    hr=input(Fore.LIGHTBLUE_EX+"are you delete all handwriting then new output 'y' to yes :\n ")
    if hr=='y':
        dir_list_a = os.listdir("handwriting/")
        try:
            for i in dir_list_a:
                location1 = os.getcwd()+"/handwriting/"
                path1 = os.path.join(location1, i)
                os.remove(path1)
            e = pyttsx3.init()
            e.say(" old handwriting codes is deleted! ")
            e.runAndWait()
            login.write_operation("*old handwriting codes is deleted! *")
        except:
            pass
    
    try:
        for student in active_students:
            name=str(student["code_melli"])
            loc=os.getcwd()+"/handwriting/"+name+".png"
            st7="In the Name Of God"+"\n"+"Active_student\n"
            st8="Today Date :\t"+str(jdatetime.date.today())+"\n"
            st="Code Melli :\t"+str(student["code_melli"])+"\n"
            st1="First Name :\t"+str(student["first_name"])+"\n"
            st2="Last Name :\t"+str(student["last_name"])+"\n"
            st3="BirthDay :\t"+str(student["birthday"])+"\n"
            st4="Student Sode :\t"+str(student["student_code"])+"\n"
            st5="courses :\t"+str(student["courses"])+"\n"
            st6="grade :\t"+str(student["grade"])+"\n"
            st9="\n\n*****Director of Artificial Intelligence Group :\tHossein Jalili***** "
            st_final=st7+st8+st+st1+st2+st3+st4+st5+st6+st9
            pywhatkit.text_to_handwriting(string=st_final,save_to=loc)
            print(Fore.LIGHTGREEN_EX+"handwriting",student["code_melli"],"\tis Done!")
 

        for student in graduate_students:
            name=str(student["code_melli"])
            loc=os.getcwd()+"/handwriting/"+name+".png"
            st7="In the Name Of God"+"\n"+"Graduate_student\n"
            st8="Today Date :\t"+str(jdatetime.date.today())+"\n"
            st="Code Melli :\t"+str(student["code_melli"])+"\n"
            st1="First Name :\t"+str(student["first_name"])+"\n"
            st2="Last Name :\t"+str(student["last_name"])+"\n"
            st3="BirthDay :\t"+str(student["birthday"])+"\n"
            st4="Student Sode :\t"+str(student["student_code"])+"\n"
            st5="courses :\t"+str(student["courses"])+"\n"
            st6="grade :\t"+str(student["grade"])+"\n"
            st9="\n\n*****Director of Artificial Intelligence Group :\tHossein Jalili***** "
            st_final=st7+st8+st+st1+st2+st3+st4+st5+st6+st9
            pywhatkit.text_to_handwriting(string=st_final,save_to=loc)
            print(Fore.LIGHTRED_EX+"handwriting",student["code_melli"],"\tis Done!")
            

        print(Fore.LIGHTGREEN_EX+"handwriting Code of all student is save as png file \n")
        login.write_operation("*handwriting Code of all student is save as png file *")
        e = pyttsx3.init()
        e.say(" handwriting Code of all student is save as png file ")
        e.runAndWait()
    except:
        print(Fore.LIGHTRED_EX+"handwriting Code can not save!!! \n")
    print(Fore.CYAN+"\n\U0001F535 handwriting output Operation is End !\n"+Fore.RESET)
    login.write_operation("****end handwriting ****")
    EndTime16=time.time()
    TotalTime16=EndTime16-StartTime16
    login.write_operation(" total time handwriting : \t"+str(TotalTime16))
    ex = input("\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        clear()

def sort_by_last_name():
	ls = list()
	for sname,details in D.items():
		tup = (sname[1],sname[0])
		ls.append(tup)
	ls = sorted(ls)
	for i in ls:
		print(Fore.LIGHTBLUE_EX+"",i[1],"   ",i[0],""+Fore.RESET)

def search_by_lastname(fname):
	ls = list()
	for sname,details in D.items():
		tup=(sname,details)
		ls.append(tup)
	for i in ls:
		if i[0][1] == fname:
			print(Fore.LIGHTYELLOW_EX+"FirstName:\t"+Fore.LIGHTBLUE_EX,i[0][0],Fore.LIGHTYELLOW_EX+"\nLastName:\t"+Fore.LIGHTBLUE_EX,i[0][1],Fore.LIGHTYELLOW_EX+"\nCodeMelli:\t"+Fore.LIGHTBLUE_EX,i[1][0],Fore.LIGHTYELLOW_EX+"\nMean:\t"+Fore.LIGHTBLUE_EX,i[1][1],Fore.RESET+"")
	
def search_by_firstname(fname):
	ls = list()
	for sname,details in D.items():
		tup=(sname,details)
		ls.append(tup)
	for i in ls:
		if i[0][0] == fname:
			print(Fore.LIGHTYELLOW_EX+"FirstName:\t"+Fore.LIGHTBLUE_EX,i[0][0],Fore.LIGHTYELLOW_EX+"\nLastName:\t"+Fore.LIGHTBLUE_EX,i[0][1],Fore.LIGHTYELLOW_EX+"\nCodeMelli:\t"+Fore.LIGHTBLUE_EX,i[1][0],Fore.LIGHTYELLOW_EX+"\nMean:\t"+Fore.LIGHTBLUE_EX,i[1][1],Fore.RESET+"")

def avdance_ss():
    global D
    D = dict()
    
    login.write_operation("****run avdance_ss ****")
    #clear() 
    d1="\U0001F534"
    d2="\U0001F7E0"
    d3="\U0001F7E1"
    d4="\U0001F7E2"
    r ="\U0001F7E5"
    oo ="\U0001F7E7"
    yy ="\U0001F7E8"
    g ="\U0001F7E9"
    p ="\U0001F7EA"
    b ="\U0001F7EB"
    bl="\U00002B1B"
    w ="\U00002B1C"
    qq ="\U0001F4A0"
    e = pyttsx3.init()
    e.say("Which list do you want to search and sort ??")
    e.runAndWait()
    print(Fore.LIGHTGREEN_EX+"\nenter a   --> for active_students")
    print(Fore.LIGHTRED_EX+"enter g   --> for graduate_students\n")
    search_list=input(Fore.LIGHTYELLOW_EX+'\nWhich list (a & g) do you want to search??'+Fore.RESET).lower()
    clear()
    if search_list=='a':
        for students in active_students:
            x=students['first_name']
            y=students['last_name']
            z=students['code_melli']
            sum=0
            count=0
            for j in students['grade'] :
                sum+=int(j)
                count+=1
            m=sum/count
            D[x, y] = (z, m)
            #print(x,y,z,m,"\n")
        while True:
            print(""+Fore.LIGHTCYAN_EX)
            print("         Sort & Adnance Search           ")
            print(qq,r,oo,yy,g,p,b,bl,w,r,oo,yy,g,qq)
            print(d1," 'a' for Sorting using last name   ",d1)
            print(d2," 'b' for Search by using last name ",d2) 
            print(d3," 'c' for Search by using first name",d3) 
            print(d4," 'd' back to main menu             ",d4) 
            print(qq,r,oo,yy,g,p,b,bl,w,r,oo,yy,g,qq,"\n\n"+Fore.RESET)
            e = pyttsx3.init()
            e.say("Enter the operation ??")
            e.runAndWait()
            choice = input(Fore.LIGHTYELLOW_EX+'Enter the operation :'+Fore.RESET)
                
            if choice == 'a':
                StartTime17=time.time()
                clear()
                print(Fore.LIGHTCYAN_EX+"****Sorting using last name****\n")
                sort_by_last_name()
                login.write_operation("*Sorting using last name in active student*")
                e = pyttsx3.init()
                e.say("Sort is done!")
                e.runAndWait()
                EndTime17=time.time()
                TotalTime17=EndTime17-StartTime17
                login.write_operation(" total time Sorting  : \t"+str(TotalTime17))
                q=input(Fore.LIGHTYELLOW_EX+"\n\nenter'b' to back serach and sort menu \n enter 'q' to back main menu "+Fore.RESET)
                if q=='b':
                    clear()
                    exit
                if q=='q':
                    clear()
                    break
            elif choice == 'b':
                StartTime18=time.time()
                clear()
                print(Fore.LIGHTCYAN_EX+"****Search by using last name****\n")
                last = input(Fore.LIGHTYELLOW_EX+'Enter Lastname name of student: '+Fore.RESET).title()
                clear()
                print("\n")
                print(Fore.LIGHTGREEN_EX+"---------------active student-----------------"+Fore.RESET)
                search_by_lastname(last)
                login.write_operation("*Search by using last name in active student*")
                print(Fore.LIGHTGREEN_EX+"-----------------------------------------------"+Fore.RESET)
                e = pyttsx3.init()
                e.say("Search is done!")
                e.runAndWait()
                EndTime18=time.time()
                TotalTime18=EndTime18-StartTime18
                login.write_operation(" total time Search lastname  : \t"+str(TotalTime18))
                q=input(Fore.LIGHTYELLOW_EX+"\n\nenter'b' to back serach and sort menu \n enter 'q' to back main menu "+Fore.RESET)
                if q=='b':
                    clear()
                    exit
                if q=='q':
                    clear()
                    break
                
            elif choice == 'c':
                StartTime19=time.time()
                clear()
                print(Fore.LIGHTCYAN_EX+"****Search by using first name****\n")
                first = input(Fore.LIGHTYELLOW_EX+'Enter Firstname name of student: '+Fore.RESET).title()
                clear()
                print("\n")
                print(Fore.LIGHTGREEN_EX+"---------------active student-------------------"+Fore.RESET)
                search_by_firstname(first)
                login.write_operation("*Search by using first name in active student*")
                print(Fore.LIGHTGREEN_EX+"------------------------------------------------"+Fore.RESET)
                e = pyttsx3.init()
                e.say("Search is done!")
                e.runAndWait()
                EndTime19=time.time()
                TotalTime19=EndTime19-StartTime19
                login.write_operation(" total time Search firstname  : \t"+str(TotalTime19))
                q=input(Fore.LIGHTYELLOW_EX+"\n\nenter'b' to back serach and sort menu \n enter 'q' to back main menu "+Fore.RESET)
                if q=='b':
                    clear()
                    exit
                if q=='q':
                    clear()
                    break
            elif choice == 'd':
                    clear()
                    break
            else:
                clear()
                print(Fore.LIGHTRED_EX+'\n\nwrong choise!!!\n'+Fore.RESET)
                
            

    elif search_list=='g':
        for students in graduate_students:
            x=students['first_name']
            y=students['last_name']
            z=students['code_melli']
            sum=0
            count=0
            for j in students['grade'] :
                sum+=int(j)
                count+=1
            m=sum/count
            D[x, y] = (z, m)
            #print(x,y,z,m,"\n")
        while True:
            print(""+Fore.LIGHTCYAN_EX)
            print("         Sort & Adnance Search           ")
            print(qq,r,oo,yy,g,p,b,bl,w,r,oo,yy,g,qq)
            print(d1," 'a' for Sorting using last name   ",d1)
            print(d2," 'b' for Search by using last name ",d2) 
            print(d3," 'c' for Search by using first name",d3) 
            print(d4," 'd' back to main menu             ",d4) 
            print(qq,r,oo,yy,g,p,b,bl,w,r,oo,yy,g,qq,"\n\n"+Fore.RESET)
            e = pyttsx3.init()
            e.say("Enter the operation ??")
            e.runAndWait()
            choice = input(Fore.LIGHTYELLOW_EX+'Enter the operation :'+Fore.RESET)
                
            if choice == 'a':
                StartTime20=time.time()
                clear()
                print(Fore.LIGHTCYAN_EX+"****Sorting using last name****\n")
                sort_by_last_name()
                e = pyttsx3.init()
                e.say("Sort is done!")
                e.runAndWait()
                login.write_operation("*Sorting using last name in graduate student *")
                EndTime20=time.time()
                TotalTime20=EndTime20-StartTime20
                login.write_operation(" total time Sorting  : \t"+str(TotalTime20))
                q=input(Fore.LIGHTYELLOW_EX+"\n\nenter'b' to back serach and sort menu \n enter 'q' to back main menu "+Fore.RESET)
                if q=='b':
                    clear()
                    exit
                if q=='q':
                    clear()
                    break
            elif choice == 'b':
                StartTime21=time.time()
                clear()
                print(Fore.LIGHTCYAN_EX+"****Search by using last name****\n")
                last = input(Fore.LIGHTYELLOW_EX+'Enter Lastname name of student: '+Fore.RESET).title()
                clear()
                print("\n")
                print(Fore.LIGHTRED_EX+"---------------graduate student-----------------"+Fore.RESET)
                search_by_lastname(last)
                login.write_operation("*Search by using last name in graduate student*")
                print(Fore.LIGHTRED_EX+"------------------------------------------------"+Fore.RESET)
                e = pyttsx3.init()
                e.say("Search is done!")
                e.runAndWait()
                EndTime21=time.time()
                TotalTime21=EndTime21-StartTime21
                login.write_operation(" total time Search lastname  : \t"+str(TotalTime21))
                q=input(Fore.LIGHTYELLOW_EX+"\n\nenter'b' to back serach and sort menu \n enter 'q' to back main menu "+Fore.RESET)
                if q=='b':
                    clear()
                    exit
                if q=='q':
                    clear()
                    break
                
            elif choice == 'c':
                StartTime22=time.time()
                clear()
                print(Fore.LIGHTCYAN_EX+"****Search by using first name****\n")
                first = input(Fore.LIGHTYELLOW_EX+'Enter Firstname name of student: '+Fore.RESET).title()
                clear()
                print("\n")
                print(Fore.LIGHTRED_EX+"---------------graduate student-----------------"+Fore.RESET)
                search_by_firstname(first)
                login.write_operation("*Search by using first name in graduate student*")
                print(Fore.LIGHTRED_EX+"------------------------------------------------"+Fore.RESET)
                e = pyttsx3.init()
                e.say("Search is done!")
                e.runAndWait()
                EndTime22=time.time()
                TotalTime22=EndTime22-StartTime22
                login.write_operation(" total time Search firstname  : \t"+str(TotalTime22))
                q=input(Fore.LIGHTYELLOW_EX+"\n\nenter'b' to back serach and sort menu \n enter 'q' to back main menu "+Fore.RESET)
                if q=='b':
                    clear()
                    exit
                if q=='q':
                    clear()
                    break
            elif choice == 'd':
                    clear()
                    break
            else:
                clear()
                print(Fore.LIGHTRED_EX+'\n\nwrong choise!!!\n'+Fore.RESET)
                
            
    else:
        print(Fore.LIGHTRED_EX+"enter 'a' or 'g' only!!!\n"+Fore.RESET)
        avdance_ss()
    login.write_operation("**** end avdance_ss ****")

