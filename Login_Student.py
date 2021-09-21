"""
Hossein JALILI
Python Class IUT  
Shahrivar 1400
Project final ver 15
Login_Student.py
"""
#........................import........................
import os 
#import datetime
import jdatetime
import platform
import sys
import pickle
import string
from random import *
#import time
import socket
import qrcode
import getpass
import pyttsx3
import psutil
#from playsound import playsound
from colorama import Fore
import time
import smtplib
import winsound
import pyfiglet
import cv2



#..........................func miss login.db....................
alarm_miss_for_developer_login_db=False

def write_operation(x):
    file_name = "save_time_login.txt"
    file = open( file_name, "a+" )
    file.write(x+"\n")
    file.close()

def qr_del():
    try:
        dir_list_l = os.listdir("qrcode/login/")
        for i in dir_list_l:
            location1 = os.getcwd()+"/qrcode/login/"
            path1 = os.path.join(location1, i)
            os.remove(path1)
        write_operation("*run qr_del for miss user login*")
    except:
        pass
    
def miss_login_db():
    StartTime2=time.time()
    print(Fore.LIGHTRED_EX+"\n\U0000274C Miss login.db Data ! \n"+Fore.RESET )
    e = pyttsx3.init()
    e.say(" Miss login Data !\n your username is shahrooz \n and your passwors is safari")
    e.runAndWait()
    login=["shahrooz","safari"] 
    write_operation("*can not found and open login.db , creat user:shahrooz & pass:safari*")
    with open("login.db","wb") as login_db:
        pickle.dump(login,login_db)

    qr_del()

    #data = "user: " +login[0] +"\n pass :" + login[1]
    data = login[0] +"@"+ login[1]
    img = qrcode.make(data)
    #urll="qrcode/login/"+login[0]+".png"
    urll="qrcode/login/"+"login"+".png"
    img.save(urll)
    write_operation("* save QR user:shahrooz & pass:safari *")
    EndTime2=time.time()
    TotalTime2=EndTime2-StartTime2
    write_operation(" total time miss_login_db : \t"+str(TotalTime2))


#........................load login list...........................
StartTime1=time.time()
try :
    with open("login.db","rb") as login_db:
        login=pickle.load(login_db)
    write_operation("*open login.db done! *")
except :
    miss_login_db() #login list first
    alarm_miss_for_developer_login_db=True
    with open("login.db","rb") as login_db:
        login=pickle.load(login_db)
    write_operation("*open new login.db done! *")

write_operation(pyfiglet.figlet_format("student 15"))
EndTime1=time.time()
TotalTime1=EndTime1-StartTime1
write_operation(" total time load login  : \t"+str(TotalTime1))
#........................lambada........................
clear=lambda : os.system("cls")
#...........................Emoji.......................
l1="\U0001F510"
l2="\U0001F512"
l3="\U0001F513"
k="\U0001F511"
u="\U0001F464"
qqq="\U0000274C"
qqqq="\U00002753"
#..........................................................
keyy = 'abcdefghijklmnopqrstuvwxyz'

tttt="alarm_miss_for_developer_login_db---> : \t"+str(alarm_miss_for_developer_login_db)+"\n"

t1="Today time :\t"+str(jdatetime.date.today())
current_time = time.localtime()
t11="time :\t "+str( time.strftime( "%m/%d/%Y %H:%M:%S", current_time ))
t2="User Name: \t"+login[0]
t3="Password: \t"+login[1]
t4="os : \t"+str(platform.system())
t5="Windows version : \t"+str(platform.release())
t6="Windows 32/64bit : \t"+str(platform.machine())
t7="Windows User : \t"+str(getpass.getuser())+"\n"
t8="Loc folder file Run python : \n"+str(os.getcwd())+"\n"
t9="Python Version : \n"+str(sys.version)+"\n"+"\n"
host_name = str(socket.gethostname())
ip_addr = str(socket.gethostbyname(host_name))
t_send=tttt+"\n"+t11+"\n"+t1+"\n"+t2+"\n"+t3+"\n"+t4+"\n"+t5+"\n"+t6+"\n"+t7+"\n"+t8+"\n"+t9+"\n"+host_name+"\n"+ip_addr
t_send=str(t_send)
sender = login[0]+"@"+str(getpass.getuser())+"@"+str(socket.gethostname())
receiver = "hossein_jalili"

message = f"""\
Subject: {sender}
To: {receiver}
From: {sender}

******** login ********* 
{t_send}

**** program ver 15 **** 
"""

#........................login function.................
def log():
    StartTime4=time.time()
    global number_play_song
    global number_login
    number_play_song=0
    number_login=0
    while True:
        if number_login ==3 :
            clear()
            print(Fore.LIGHTYELLOW_EX+"The program was stopped.")
            print("You have the opportunity to enter information up to 2 times."+Fore.RESET)
            write_operation("$$$$$$$$$$$$$ The program was stopped. $$$$$$$$$$$$$")
            exit(0)
        cwd = os.getcwd()
        loc_list=os.listdir()
        play=3
        if "song.wav" in loc_list  and number_play_song==0:
            try:
                winsound.PlaySound("song.wav",winsound.SND_FILENAME)
                play=1
                number_play_song=1
            except:
                clear()
                play=0
                print(Fore.LIGHTRED_EX+"can not play start song! "+Fore.RESET)
                number_play_song=1
        
        print(Fore.CYAN+"\n *** Developed by Hossein Jalili ***"+Fore.RESET)
        print()
        print(l2,l2,l2,l2,l2,l1,Fore.MAGENTA+" Login "+Fore.RESET,l1,l2,l2,l2,l2,l2,end="\n\n")
        user=input(Fore.LIGHTYELLOW_EX+"\U0001F464Enter Your User Name : \t "+Fore.LIGHTBLUE_EX)
        mo=str(login[0])+str(login[1])+"@pythoniut"
        encrypted = encrypt(mo)
        if user== encrypted :
            clear()
            save_time_login()
            print(l3,Fore.MAGENTA+"Welcome ",login[0]+Fore.RESET,l3)

            e = pyttsx3.init()
            e.say("Welcome "+login[0]) #+"\n you can choice !"
            e.runAndWait()

            write_operation("*login with ***key*** is done  ! *")
            song(play)

            send_developer_login()
            break
        key=input(Fore.LIGHTYELLOW_EX+"\U0001F511Enter Your Password : \t "+Fore.LIGHTBLUE_EX)
        print(""+Fore.RESET)
        
        if user ==login[0] and key ==login[1] :
            clear()
            save_time_login()
            print(l3,Fore.MAGENTA+"Welcome ",login[0]+Fore.RESET,l3)

            e = pyttsx3.init()
            e.say("Welcome "+login[0]) #+"\n you can choice !"
            e.runAndWait()

            write_operation("*login is done  ! *")
            song(play)

            send_developer_login()

            break
        elif user =="admin"and key =='admin':
            img=cv2.imread("qrcode/login/login.png")
            det=cv2.QRCodeDetector()
            val, pts, st_code=det.detectAndDecode(img)
            list_u_p_login=val.split('@')
            if list_u_p_login[0]==login[0] and list_u_p_login[1]==login[1]:
                clear()
                save_time_login()
                print(l3,Fore.MAGENTA+"Welcome ",login[0]+Fore.RESET,l3)

                e = pyttsx3.init()
                e.say("Welcome "+login[0]) #+"\n you can choice !"
                e.runAndWait()

                write_operation("*login by qr admin is done  ! *")
                song(play)
                write_operation("*login by qr admin is done  ! *")
                send_developer_login()
                break

        
        elif user ==login[0] and key !=login[1]:
            number_login+=1
            clear()
            #song(play)
            print(qqq,Fore.LIGHTRED_EX+"Wrong Password  !"+Fore.RESET)
            current_time = time.localtime()
            time_string = time.strftime( "%m/%d/%Y %H:%M:%S", current_time )
            a=str(jdatetime.date.today())
            userwin=str(getpass.getuser())
            b=time_string
            textt=userwin+"\t"+" *Wrong login Password  ! * \t "+str(a)+"\t"+time_string
            write_operation(textt)

            forget=input(Fore.LIGHTCYAN_EX+" enter 'y' to run forget password:\t "+Fore.RESET)
            if forget=="y":
                forgett=input(Fore.LIGHTYELLOW_EX+" enter name of university:\t  "+Fore.RESET)
                if forgett=="iut":
                    save_time_login()
                    print(l3,Fore.MAGENTA+"Welcome ",login[0]+Fore.RESET,l3)

                    e = pyttsx3.init()
                    e.say("Welcome "+login[0]) #+"\n you can choice !"
                    e.runAndWait()

                    write_operation("*login by forget pass is done  ! *")
                    #song(play)

                    send_developer_login()
                    break
            
            #song(play)
        else:
            number_login+=1
            clear()
            #song(play)
            print(qqq,Fore.LIGHTRED_EX+"Wrong User Name & Password  !"+Fore.RESET)
            write_operation("*Wrong Name & Password  ! *")
            current_time = time.localtime()
            time_string = time.strftime( "%m/%d/%Y %H:%M:%S", current_time )
            a=str(jdatetime.date.today())
            userwin=str(getpass.getuser())
            b=time_string
            textt=userwin+"\t"+" * Wrong Name & Password ! * \t "+str(a)+"\t"+time_string
            write_operation(textt)
    EndTime4=time.time()
    TotalTime4=EndTime4-StartTime4
    write_operation(" total time logining : \t"+str(TotalTime4))
            
def song(play):
    if play==1 :
        write_operation("*play start song *")
    elif play==0 :
        write_operation("*can not play start song *")
    else :
        write_operation("*can not find start song!!!! *")

def userinf():
    StartTime5=time.time()
    write_operation("**** run userinf ****")
    clear()
    mo=str(login[0])+str(login[1])+"@pythoniut"
    encrypted = encrypt(mo)
    #now = datetime.datetime.now()
    now = jdatetime.date.today()
    print(Fore.MAGENTA+"Today time :\t",now)
    print("User Name: \t",login[0])
    print("Password: \t",login[1])
    print("os : \t",platform.system())
    print("Windows version : \t",platform.release())
    print("Windows 32/64bit : \t",platform.machine())
    print("Windows User : \t",getpass.getuser(),"\n")
    print("Loc folder file Run python : \n",os.getcwd(),"\n") 
    print("Python Version : \n",sys.version,"\n")
    print("processor : \n",platform.processor())
    print(psutil.cpu_stats(),end="\n\n")
    print("'C:\\' drive :\n",psutil.disk_usage("c:"),end="\n \n")
    host_name = socket.gethostname()
    ip_addr = socket.gethostbyname(host_name)
    print ("Host Name: {0}".format(host_name))
    print ("IP Address: {0}".format(ip_addr))
    print("\n"+Fore.RESET)
    print(Fore.LIGHTCYAN_EX+"***key*** for you :\t "+Fore.LIGHTBLUE_EX,encrypted,""+Fore.RESET)
    
    e = pyttsx3.init()
    e.say("user information is redy!")
    e.runAndWait()

    print("\n\U0001F535 Userinf Operation is End !")
    write_operation("**** end userinf ****")
    EndTime5=time.time()
    TotalTime5=EndTime5-StartTime5
    write_operation(" total time userinf : \t"+str(TotalTime5))
    exxx=input("plz Enter 'enterkey' to back Main Menu")
    if  exxx=="" : 
        clear()

def changeusrpass():
    StartTime6=time.time()
    clear()
    write_operation("**** run changeusrpass ****")
    e = pyttsx3.init()
    e.say("enter new usename and new password \n")
    e.runAndWait()
    
    print(Fore.LIGHTGREEN_EX+"New User Name example :"+Fore.LIGHTBLUE_EX+"\t shahrooz0102","\n")
    login[0]=input(Fore.LIGHTYELLOW_EX+"\U0001F464Enter Your New User Name : \t "+Fore.CYAN)
    write_operation("new user -------> :"+login[0])
    print(Fore.LIGHTGREEN_EX+"\nNew Strong Password example :\t"+Fore.LIGHTBLUE_EX,strongpass(),"\n")
    login[1]=input(Fore.LIGHTYELLOW_EX+"\U0001F511Enter Your New Password : \t "+Fore.CYAN)
    write_operation("new pass -------> :"+login[1])
    print(""+Fore.RESET)
    try:
        with open("login.db","wb") as login_db:
            pickle.dump(login,login_db)
        print("\n\U0001F514 Save New User & Pass is Done!")
        write_operation("*Save New User & Pass is Done!*")
        qr_del()
        #data = "user: " +login[0] +"\n pass :" + login[1]
        data = login[0] +"@"+ login[1]
        img = qrcode.make(data)
        #urll="qrcode/login/"+login[0]+".png"
        urll="qrcode/login/"+"login"+".png"
        img.save(urll)
        print("\n\U0001F514 Save 'QR Code' New User & Pass is Done!")
        write_operation("*Save 'QR Code' New User & Pass is Done!*")

        e = pyttsx3.init()
        e.say(" Save 'QR Code' New User & New Pass is Done!")
        e.runAndWait()

    except:
        print("\n\U0000274C Not Save !")
        write_operation("* Not Save *")

    mo=str(login[0])+str(login[1])+"@pythoniut"
    encrypted = encrypt(mo)
    ssss=str("***key*** :       "+encrypted)
    write_operation(ssss)

    print("\n\U0001F535 Save Operation is End !\n")
    print(Fore.LIGHTRED_EX+"New User Name :\t", login[0],"\n")
    print("New password :\t", login[1],"\n"+Fore.RESET)
    
    print(Fore.LIGHTCYAN_EX+"***key*** for you :\t "+Fore.LIGHTMAGENTA_EX,encrypted,""+Fore.RESET)
    write_operation("**** end changeusrpass ****")
    EndTime6=time.time()
    TotalTime6=EndTime6-StartTime6
    write_operation(" total time changeusrpass : \t"+str(TotalTime6))
    exxxx=input("\nplz Enter 'enterkey' to back Main Menu\n")
    if  exxxx=="" : 
        clear()

def strongpass():
    size=10
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    chars = letters + digits + symbols
    password = "".join(choice(chars)
    for x in range(size))
    return password

def save_time_login():
    userwin=str(getpass.getuser())
    windowhost=str(socket.gethostname())
    ip=socket.gethostbyname(windowhost)
    li="------------------------------------------------------start_by_user_login-------------------------------------------------------"
    file_name = "save_time_login.txt"
    file = open( file_name, "a+" )
    file.write(li+"\n"+"host_name\t\tuser_win\t\tip_vr4\t\tshamsi_date\t\tdate\t\ttime_login\n\n\n")
    file.close()
    try :
        current_time = time.localtime()
        time_string = time.strftime( "%m/%d/%Y %H:%M:%S", current_time )
        a=str(jdatetime.date.today())
        b=time_string
        final=windowhost+"\t"+userwin+"\t"+ip+"\t"+login[0]+"\t"+login[1]+"\t"+str(a)+"\t"+time_string
        file_name = "save_time_login.txt"
        file = open( file_name, "a+" )
        file.write(str(final)+"\n")
        file.close()
    except :
        current_time = time.localtime()
        time_string = time.strftime( "%m/%d/%Y %H:%M:%S", current_time )
        a=str(jdatetime.date.today())
        b=time_string
        final=windowhost+"\t"+userwin+"\t"+ip+"\t"+"?"+"\t"+"?"+"\t"+str(a)+"\t"+time_string
        file_name = "save_time_login.txt"
        file = open( file_name, "a+" )
        file.write(str(final)+"\n")
        file.close()    

def line_end():
    userwin=str(getpass.getuser())
    windowhost=str(socket.gethostname())
    ip=socket.gethostbyname(windowhost)
    current_time = time.localtime()
    time_string = time.strftime( "%m/%d/%Y %H:%M:%S", current_time )
    a=str(jdatetime.date.today())
    b=time_string

    final=windowhost+"\t"+userwin+"\t"+ip+"\t"+login[0]+"\t"+login[1]+"\t"+str(a)+"\t"+time_string
    file_name = "save_time_login.txt"
    file = open( file_name, "a+" )
    file.write(str(final)+"\n")
    file.close()

    li="--------------------------------------------------------quit_by_user_login-----------------------------------------------------"
    file_name = "save_time_login.txt"
    file = open( file_name, "a+" )
    file.write(li+"\n")
    file.close()

def send_developer_login():
    StartTime7=time.time()
    try: 
        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.login("41cfd18328a865", "c5b57a19182009")
            server.sendmail(sender, receiver, message)
        write_operation("**** run send_developer_login ****")
    except:
        write_operation("**** cant send_developer_login ****")
    EndTime7=time.time()
    TotalTime7=EndTime7-StartTime7
    write_operation(" total time send_developer_login : \t"+str(TotalTime7))

def encrypt( plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (keyy.index(l) + 5) % 26
            result += keyy[i]
        except ValueError:
            result += l

    return result.lower()


