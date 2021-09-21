"""
Hossein JALILI
Python Class IUT  
Shahrivar 1400
Project final ver 15
Sample_data.py
"""
import requests
import os
import pyfiglet
import time



def write_operation(x):
    file_name = "save_time_login.txt"
    file = open( file_name, "a+" )
    file.write(x+"\n")
    file.close()
    
def download_db():
    try:
        url1 = "https://s19.picofile.com/d/8440985000/2b17cd5f-932a-4728-a50f-64e779f65d97/login.db"
        data1 = requests.get(url1).content
        with open("login.db","wb") as login:
            login.write(data1)
        write_operation("@@@ Download 'login.db' is done! @@@")
        print("@@@ Download 'login.db' is done! @@@")
    except:
        write_operation("@@@ cant Download 'login.db' !!!! @@@")
        print("@@@ cant Download 'login.db' !!!! @@@")

    try:
        url2 = "https://s19.picofile.com/d/8440985042/effd180e-641f-423b-8f7f-b5f22c1122d3/active_students.db"
        data2 = requests.get(url2).content
        with open("active_students.db","wb") as active_students:
            active_students.write(data2)
        write_operation("@@@ Download 'active_students.db' is done! @@@")
        print("@@@ Download 'active_students.db' is done! @@@")
    except:
        write_operation("@@@ cant Download 'active_students.db' !!!! @@@")
        print("@@@ cant Download 'active_students.db' !!!! @@@")

    try:
        url3 = "https://s18.picofile.com/d/8440985068/1e63265c-6806-43f5-8c6a-9704b1007b13/graduate_students.db"
        data3 = requests.get(url3).content
        with open("graduate_students.db","wb") as graduate_student:
            graduate_student.write(data3)
        write_operation("@@@ Download 'graduate_students.db' is done! @@@")
        print("@@@ Download 'graduate_students.db' is done! @@@")
    except:
        write_operation("@@@ cant Download 'graduate_students.db' !!!! @@@")
        print("@@@ cant Download 'graduate_students.db' !!!! @@@")

    try:
        url4 = "https://s19.picofile.com/d/8440984450/00c42194-dd1d-492c-b852-d91757b21c92/email.db"
        data4 = requests.get(url4).content
        with open("email.db","wb") as email:
            email.write(data4)
        write_operation("@@@ Download 'email.db' is done! @@@")
        print("@@@ Download 'email.db' is done! @@@")
    except:
        write_operation("@@@ cant Download 'email.db' !!!! @@@")
        print("@@@ cant Download 'email.db' !!!! @@@")

def download_song_welcom():
    try:
        url5 = "https://s19.picofile.com/d/8440985618/1e1d8a17-200e-40d5-8f67-904d4e355f4e/song.wav"
        data5 = requests.get(url5).content
        with open("song.wav","wb") as song:
            song.write(data5)
        write_operation("@@@ Download 'song.wav' is done! @@@")
        print("@@@ Download 'song.wav' is done! @@@")
    except:
        write_operation("@@@ cant Download 'song.wav' !!!! @@@")
        print("@@@ cant Download 'song.wav' !!!! @@@")

def downlod_pic():
    write_operation("@@@ Download 'pic' is start! @@@")
    print("@@@ Download 'pic' is start! @@@")
    try:
        url6 = "https://s18.picofile.com/file/8440987700/1150232676.png"
        data6 = requests.get(url6).content
        with open(os.getcwd()+"/pic/"+"1150232676.png","wb") as song:
            song.write(data6)
        write_operation("@@@ Download '1150232676.png' is done! @@@")
        print("@@@ Download '1150232676.png' is done! @@@")
    except:
        write_operation("@@@ cant Download '1150232676.png' !!!! @@@")
        print("@@@ cant Download '1150232676.png' !!!! @@@")
    
    try:
        url7 = "https://s19.picofile.com/file/8440987726/1234567890.png"
        data7 = requests.get(url7).content
        with open(os.getcwd()+"/pic/"+"1234567890.png","wb") as song:
            song.write(data7)
        write_operation("@@@ Download '1234567890.png' is done! @@@")
        print("@@@ Download '1234567890.png' is done! @@@")
    except:
        write_operation("@@@ cant Download '1234567890.png' !!!! @@@")
        print("@@@ cant Download '1234567890.png' !!!! @@@")
    
    try:
        url8 = "https://s18.picofile.com/file/8440987742/1245678910.png"
        data8 = requests.get(url8).content
        with open(os.getcwd()+"/pic/"+"1245678910.png","wb") as song:
            song.write(data8)
        write_operation("@@@ Download '1245678910.png' is done! @@@")
        print("@@@ Download '1245678910.png' is done! @@@")
    except:
        write_operation("@@@ cant Download '1245678910.png' !!!! @@@")
        print("@@@ cant Download '1245678910.png' !!!! @@@")
    
    try:
        url9 = "https://s19.picofile.com/file/8440987768/7862107800.png"
        data9 = requests.get(url9).content
        with open(os.getcwd()+"/pic/"+"7862107800.png","wb") as song:
            song.write(data9)
        write_operation("@@@ Download '7862107800.png' is done! @@@")
        print("@@@ Download '7862107800.png' is done! @@@")
    except:
        write_operation("@@@ cant Download '7862107800.png' !!!! @@@")
        print("@@@ cant Download '7862107800.png' !!!! @@@")
    write_operation("@@@ Download 'pic' is end! @@@")
    print("@@@ Download 'pic' is end! @@@")

def downlod_handwriting():
    write_operation("@@@ Download 'handwriting' is start! @@@")
    print("@@@ Download 'handwriting' is start! @@@")
    try:
        url6 = "https://s18.picofile.com/file/8440988276/1150232676.png"
        data6 = requests.get(url6).content
        with open(os.getcwd()+"/handwriting/"+"1150232676.png","wb") as song:
            song.write(data6)
        write_operation("@@@ Download '1150232676.png' is done! @@@")
        print("@@@ Download '1150232676.png' is done! @@@")
    except:
        write_operation("@@@ cant Download '1150232676.png' !!!! @@@")
        print("@@@ cant Download '1150232676.png' !!!! @@@")
    
    try:
        url7 = "https://s18.picofile.com/file/8440988284/1234567890.png"
        data7 = requests.get(url7).content
        with open(os.getcwd()+"/handwriting/"+"1234567890.png","wb") as song:
            song.write(data7)
        write_operation("@@@ Download '1234567890.png' is done! @@@")
        print("@@@ Download '1234567890.png' is done! @@@")
    except:
        write_operation("@@@ cant Download '1234567890.png' !!!! @@@")
        print("@@@ cant Download '1234567890.png' !!!! @@@")
    
    try:
        url8 = "https://s18.picofile.com/file/8440988292/1245678910.png"
        data8 = requests.get(url8).content
        with open(os.getcwd()+"/handwriting/"+"1245678910.png","wb") as song:
            song.write(data8)
        write_operation("@@@ Download '1245678910.png' is done! @@@")
        print("@@@ Download '1245678910.png' is done! @@@")
    except:
        write_operation("@@@ cant Download '1245678910.png' !!!! @@@")
        print("@@@ cant Download '1245678910.png' !!!! @@@")
    
    try:
        url9 = "https://s19.picofile.com/file/8440988318/7862107800.png"
        data9 = requests.get(url9).content
        with open(os.getcwd()+"/handwriting/"+"7862107800.png","wb") as song:
            song.write(data9)
        write_operation("@@@ Download '7862107800.png' is done! @@@")
        print("@@@ Download '7862107800.png' is done! @@@")
    except:
        write_operation("@@@ cant Download '7862107800.png' !!!! @@@")
        print("@@@ cant Download '7862107800.png' !!!! @@@")
    write_operation("@@@ Download 'handwriting' is end! @@@")
    print("@@@ Download 'handwriting' is end! @@@")

def download_qrcode():
    write_operation("@@@ Download 'qrcode' is start! @@@")
    print("@@@ Download 'qrcode' is start! @@@")

    try:
        url0 = "https://s18.picofile.com/file/8441039084/login.png"
        data0 = requests.get(url0).content
        with open(os.getcwd()+"/qrcode/login/"+"login.png","wb") as song:
            song.write(data0)
        write_operation("@@@ Download 'shahrooz.png' is done! @@@")
        print("@@@ Download 'shahrooz.png' is done! @@@")
    except:
        write_operation("@@@ cant Download 'shahrooz.png' !!!! @@@")
        print("@@@ cant Download 'shahrooz.png' !!!! @@@")

    try:
        url6 = "https://s19.picofile.com/file/8440988800/1150232676.png"
        data6 = requests.get(url6).content
        with open(os.getcwd()+"/qrcode/stu/a/"+"1150232676.png","wb") as song:
            song.write(data6)
        write_operation("@@@ Download '1150232676.png' is done! @@@")
        print("@@@ Download '1150232676.png' is done! @@@")
    except:
        write_operation("@@@ cant Download '1150232676.png' !!!! @@@")
        print("@@@ cant Download '1150232676.png' !!!! @@@")
    
    try:
        url7 = "https://s19.picofile.com/file/8440988834/1234567890.png"
        data7 = requests.get(url7).content
        with open(os.getcwd()+"/qrcode/stu/g/"+"1234567890.png","wb") as song:
            song.write(data7)
        write_operation("@@@ Download '1234567890.png' is done! @@@")
        print("@@@ Download '1234567890.png' is done! @@@")
    except:
        write_operation("@@@ cant Download '1234567890.png' !!!! @@@")
        print("@@@ cant Download '1234567890.png' !!!! @@@")
    
    try:
        url8 = "https://s18.picofile.com/file/8440988818/1245678910.png"
        data8 = requests.get(url8).content
        with open(os.getcwd()+"/qrcode/stu/a/"+"1245678910.png","wb") as song:
            song.write(data8)
        write_operation("@@@ Download '1245678910.png' is done! @@@")
        print("@@@ Download '1245678910.png' is done! @@@")
    except:
        write_operation("@@@ cant Download '1245678910.png' !!!! @@@")
        print("@@@ cant Download '1245678910.png' !!!! @@@")
    
    try:
        url9 = "https://s18.picofile.com/file/8440988826/7862107800.png"
        data9 = requests.get(url9).content
        with open(os.getcwd()+"/qrcode/stu/a/"+"7862107800.png","wb") as song:
            song.write(data9)
        write_operation("@@@ Download '7862107800.png' is done! @@@")
        print("@@@ Download '7862107800.png' is done! @@@")
    except:
        write_operation("@@@ cant Download '7862107800.png' !!!! @@@")
        print("@@@ cant Download '7862107800.png' !!!! @@@")

    write_operation("@@@ Download 'qrcode' is end! @@@")
    print("@@@ Download 'qrcode' is end! @@@")

def download_tools_item():
    write_operation("@@@ Download 'tools_item' is start! @@@")
    print("@@@ Download 'tools_item' is start! @@@")

    try:
        url0 = "https://s19.picofile.com/d/8441047700/75dfbadd-a295-4e41-a9ed-513191e16fc4/haarcascade_frontalface_default.xml"
        data0 = requests.get(url0).content
        with open(os.getcwd()+"/tools/"+"haarcascade_frontalface_default.xml","wb") as s:
            s.write(data0)
        write_operation("@@@ Download 'haarcascade_frontalface_default.xml' is done! @@@")
        print("@@@ Download 'haarcascade_frontalface_default.xml' is done! @@@")
    except:
        write_operation("@@@ cant Download 'haarcascade_frontalface_default.xml' !!!! @@@")
        print("@@@ cant Download 'haarcascade_frontalface_default.xml' !!!! @@@")
    
    write_operation("@@@ Download 'tools_item' is end! @@@")
    print("@@@ Download 'tools_item' is end! @@@")

def miss_folder():
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

def load_sample():
    write_operation("##### 'Sample_data.py' is rinning... #####")
    print("##### 'Sample_data.py' is rinning... #####")

    write_operation("@@@ 'Create sample folders' is rinning... @@@")
    print("@@@ 'Create sample folders' is rinning... @@@")

    StartTime2=time.time()
    miss_folder()
    EndTime2=time.time()
    TotalTime2=EndTime2-StartTime2
    write_operation(" total time create folder : \t"+str(TotalTime2))

    write_operation("@@@ 'Create sample folders' is end. @@@")
    print("@@@ 'Create sample folders' is end @@@")

    write_operation("@@@ 'Download files' is rinning... @@@")
    print("@@@ 'Download files' is rinning... @@@")

    StartTime3=time.time()
    download_db()
    download_song_welcom()
    downlod_pic()
    download_qrcode()
    downlod_handwriting()
    download_tools_item()
    EndTime3=time.time()
    TotalTime3=EndTime3-StartTime3
    write_operation(" total time download : \t"+str(TotalTime3))

    write_operation("@@@ 'Download files' is end @@@")
    print("@@@ 'Download files' is end @@@")

    write_operation("##### 'Sample_data.py' is end #####")
    print("##### 'Sample_data.py' is end #####")

StartTime1=time.time()
write_operation(pyfiglet.figlet_format("sample"))
load_sample()
EndTime1=time.time()
TotalTime1=EndTime1-StartTime1
write_operation(" total time sample : \t"+str(TotalTime1))