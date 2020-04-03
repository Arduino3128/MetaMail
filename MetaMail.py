#Version 3.2.3.6
import random
Ver=r"b'#Version 3.2.3.6\n'"
def logo():
    clear()
    colour=random.randint(31,37)
    print('''\033[1;%s;40m


                 ███╗   ███╗███████╗████████╗ █████╗ ███╗   ███╗ █████╗ ██╗██╗         ██████╗    ██████╗    ██████╗ 
                 ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗████╗ ████║██╔══██╗██║██║         ╚════██╗   ╚════██╗   ╚════██╗
                 ██╔████╔██║█████╗     ██║   ███████║██╔████╔██║███████║██║██║          █████╔╝    █████╔╝    █████╔╝
                 ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║╚██╔╝██║██╔══██║██║██║          ╚═══██╗   ██╔═══╝     ╚═══██╗
                 ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██║ ╚═╝ ██║██║  ██║██║███████╗    ██████╔╝██╗███████╗██╗██████╔╝
                 ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝ ╚═╝╚══════╝╚═╝╚═════╝
                                        [Script By: Kanad Nemade | Github: Arduino3128]
        \n'''%colour)
    print(" ")
    print(" ")
    print("Welcome to MetaMail 3.2.3, Best Off-Grid, Light-Weight and Secure E-mail Service with SHA-256 Encryptions")
    print("")
    print("")
from datetime import datetime
import time
import os
import platform
import hashlib
import re
import subprocess
getdir=os.getcwd()
r1="None"
osident=platform.system()
if "Windows" in osident:
    clear=lambda:os.system("cls")
elif "Linux" in osident:
    clear=lambda:os.system("clear")
elif "Darwin" in osident:
    clear=lambda:os.system("clear")
else:
    print("Unknown O.S. Using Default 'Windows Configuration'")
import getpass
try:
   import mysql.connector
   import requests
except:
   print("'MySQL Connector or Requests' not found! Starting 'Requests and MySQL Connector' Module installing Procedure!")
   if osident=="Windows":
       piploc=input("Enter the directory path of Python: ")
       subprocess.call("cd %s/Scripts && pip install mysql-connector-python requests"%piploc, shell=True)
       subprocess.call("MetaMail.py", shell=True)
   elif osident=="Linux" or osident=="Darwin":
       subprocess.call("pip3 install requests mysql-connector-python", shell=True)
       subprocess.call("python3 MetaMail.py", shell=True)
   else:
       print("Unknown OS, Try Installing 'mysql-connector-python & requests' manually!")
   exit()
   time.sleep(5)
#####################
s1=""
s2=""
try:
    geturls="https://raw.githubusercontent.com/Arduino3128/MetaMail/master/Server.txt"
    urls=geturls
    s1=requests.get(urls, allow_redirects=True)
    s1=str(s1.content)
    checkup2="Sucess"
except:
   print("An Error occured while checking for Server Uplink...Check your Internet Connection!")
   checkup2="Error"
s2=s1.replace("b'",'')
s2=s2.replace("'","")
s3=s2.split(r"\n")
####################
try:
    geturl1="https://raw.githubusercontent.com/Arduino3128/MetaMail/master/Version.txt"
    url=geturl1
    r1=requests.get(url, allow_redirects=True)
    r1=str(r1.content)
    checkup="Sucess"
except:
   print("An Error occured while checking for Updates....Check your Internet Connection!")
   print("Nothing Updated!")
   checkup="Error"
   time.sleep(3)
   clear()
####################
def update():
    logo()
    if r1>Ver:
       print("New Update Available!")
       print("Please Consider Updating MetaMail")
       conf=input("Do you want to Update MetaMail Now? Yes/Y/N/No: ")
       confu=conf.lower()
       def GetUp():
           try:
               geturl1="https://raw.githubusercontent.com/Arduino3128/MetaMail/master/MetaMail.py"
               r=requests.get(geturl1, allow_redirects=True)
               open("MetaMail.py",'wb').write(r.content)
               print("MetaMail.py Downloaded Sucessfully.")
               print("Updating....")
               print("MetaMail Updated Sucessfully!")
               time.sleep(2)
               if osident=="Darwin" or osident=="Linux":
                   subprocess.call("python3 MetaMail.py", shell=True)
               else:
                   subprocess.call("MetaMail.py", shell=True)
               exit(None)
           except:
               print("Failed To Update! You are using Older Version!")
       if confu=="y" or confu=="yes":
           GetUp()
       time.sleep(4)
       clear()
    else:
       print("You're running Latest Version!")
       time.sleep(1)
       clear()
if checkup=="Sucess":
    update()
else:
    print("You are maybe using older version!")
    time.sleep(2)
select=0
logo()   
select=input("Enter 1 for LAN(localhost) or 2 for WAN(Internet) or Press Just 'Enter' to Customize Connection: ")
if select=="1":
    userinput=input("Enter Username(Contact Admin For Username): ")
    passwdinput=input("Enter Password(Contact Admin For Password): ")
    portinput=input("Enter Port No. of the Server(Contact Admin For Port No.): ")
    hostinput="localhost"
    dbinput=input("Enter Database Name of the Server(Contact Admin For Database name): ")
elif select=="2":
    userinput=s3[2]
    passwdinput=s3[1]
    portinput=s3[3]
    hostinput=s3[0]
    dbinput=s3[4]

else:
    userinput=input("Enter Username(Contact Admin For Username): ")
    passwdinput=input("Enter Password(Contact Admin For Password): ")
    portinput=input("Enter Port No. of the Server(Contact Admin For Port No.): ")
    hostinput=input("Enter host IP: ")
    dbinput=input("Enter Database Name of the Server(Contact Admin For Database name): ")
def connerr():
    logo()
    print("Server Unreachable! Maybe the Server is down! Try Again Later!")
    time.sleep(4)
    exit()
try:
    dbc = mysql.connector.connect(
    host=hostinput,
    user=userinput,
    passwd=passwdinput,
    database=dbinput,
    port=portinput,
    auth_plugin='caching_sha2_password')
except:
    connerr()
c = dbc.cursor()
clear()
def meta():
    logo()
    def cforpass():
        dbc.reset_session()
        logo()
        print("Reset Password")
        foruser=input("Enter your Username: ")
        foruserlow=str.lower(foruser)
        foruser2="'%s'"%foruser
        foruserl=foruser2.lower()
        c.execute("Select ID from user")
        for j in c.fetchall():
            if foruserl in j:
               break
        else:
            print("Username not Found!")
            time.sleep(5)
            meta()
            clear()
        c.execute('Select * from user where ID="%s"'%foruserl)
        for row in c.fetchall():
              print("Question:",row[2])
        forpass=getpass.getpass("Enter Answer: ")
        def encrypt_string(forpass):
            sha_signature2 = \
                hashlib.sha256(forpass.encode()).hexdigest()
            return sha_signature2
        sha_signature2 = encrypt_string(forpass)
        nforpass="'%s'"%sha_signature2
        c.execute('select * from user where ID="%s"'%foruserl)
        for row in c.fetchall():
              if nforpass==row[3]:
                    newpass=getpass.getpass("Enter New Password: ")
                    cnewpass=getpass.getpass("Re-enter the New Pasword: ")
                    def encrypt_string(newpass):
                        sha_signature = \
                            hashlib.sha256(newpass.encode()).hexdigest()
                        return sha_signature
                    sha_signature = encrypt_string(newpass)
                    nforpass3="'%s'"%sha_signature
                    if newpass==cnewpass:
                          c.execute('UPDATE user SET  Password="%s" where ID="%s"' %(nforpass3, foruserl))
                          dbc.commit()
                          tandd=datetime.today()
                          tandd=tandd.strftime("%c")
                          c.execute("insert into %s values('Password Changed','You have changed your Password. If you did not update your account password, please report the issue immediately to \"MetaMailSupport\"', 'MetamailSupport', '%s')"%(foruserlow, tandd))
                          dbc.commit()
                          print("You Have Sucessfullly Changed your Password!")
                          time.sleep(2)
                          meta()
                    else:
                          print("Password didn't Match!")
                          time.sleep(1)
                          meta()
              else:
                    print("Incorrect Answer!")
                    time.sleep(1)
                    meta()
        
    def suser():
        print("Username not available! Try using a different One!")
        time.sleep(2)
        meta()
    def error():
        print("Unknown Action!")
        time.sleep(1)
        meta()
    def logout():
        print("Thank You for using MetaMail 3.2.3")
        print("Logging out......")
        time.sleep(1)
        dbc.reset_session()
        print("You have Sucessfully Logged out")
        time.sleep(2)
        clear()
        logo()
        o=input("Enter 1 to Return to Main Page or Press Enter to Exit: ")
        if o=="1":
            meta()
        else:exit()
    def invalidchar():
        print("Invalid Charcters Used!")
        time.sleep(2)
        meta()
    def cacc():
        dbc.reset_session()
        logo()
        print("Create your account")
        nuser=""
        npass=""
        cpass=""
        nuser=input("Enter your Username: ")
        check=nuser.isalnum()
        if check==False:
            invalidchar()
        nuserl=str.lower(nuser)
        nuser3="'%s'" %nuser
        nuser3l=str.lower(nuser3)
        if nuser=="":
            print("This Field can't be left empty!")
            time.sleep(2)
            meta()
        c.execute('select ID from user')
        for i in c.fetchall():
             if nuser3l in i:
               suser()
        npass=getpass.getpass("Enter your Password: ")
        if npass=="":
            print("This Field can't be left empty!")
            time.sleep(2)
            meta()
        def encrypt_string(npass):
            sha_signature = \
                hashlib.sha256(npass.encode()).hexdigest()
            return sha_signature
        sha_signature = encrypt_string(npass)
        cnpass=getpass.getpass("Re-enter the Password: ")
        if npass!=cnpass or npass=="":
            print("Password Didn't Match!")
            cacc()  
        forques=input("Enter your Question(This Question will be asked while resetting your password!): ")
        if forques=="":
            print("This Field can't be left empty!")
            time.sleep(2)
            meta()
        forques=forques.replace("'", "\\'")
        forques=forques.replace('"', '\\"')
        forpass=getpass.getpass("Enter the answer: ")
        if forpass=="":
            print("This Field can't be left empty!")
            time.sleep(2)
            meta()
        def encrypt_string(forpass):
            sha_signature2 = \
                hashlib.sha256(forpass.encode()).hexdigest()
            return sha_signature2
        sha_signature2 = encrypt_string(forpass)
        
        def crmail():
            fuser='f%s'%nuserl
            try:
                c.execute('insert into user values("%s","%s","%s","%s")', (nuserl, sha_signature, forques, sha_signature2))
                c.execute('create table %s(Subject varchar(255), Mail LONGTEXT, SentBy varchar(255), date varchar(255), Attachment LONGBLOB, AttachFormat varchar(255))' %nuserl)
                c.execute('create table %s(Friend varchar(100))'%fuser)
            except:
                print("Unknown Error! Maybe another user exists with same username!")
                suser()
            tandd=datetime.today()
            tandd=tandd.strftime("%c")
            c.execute('insert into %s values("Welcome To MetaMail", "Welcome to MetaMail %s", "MetaMailSupport","%s","","")' %(nuserl,nuser,tandd))      
            dbc.commit()
            print("Account Created Sucessfully!")
            time.sleep(5)
            login()                       
        if npass==cnpass and npass!="":
            crmail()
        else:print("Password Didn't Match!") and cacc()

                

    def login():
        logo()
        def mdirect():
            print("Unknown Error! Returning To Mail Box!")
            time.sleep(2)
            mail()
            
        def uerror():
            print("")
            print("Username not found! Returning to your Mail box")
            time.sleep(2)
            print("")
            def ermail():
                mail()
            ermail()
        def cmail():
            clear()
            logo()
            print("Compose Mail")
            xl=str.lower(x)
            fuser='f%s'%xl
            c.execute("select * from %s"%fuser)
            for usr in c.fetchall():
                print(usr)
            cc=input("To: ")
            ncc="'%s'" %cc
            nccl=str.lower(ncc)
            ccl=str.lower(cc)
            if cc=="":
                mdirect()
            else:pass
            p="0"
            c.execute("select ID from user")
            for i in c.fetchall():
                if nccl in i:
                    p="1"
                    pass
            if p=="1":
                pass
            else:
                print("Username Not Found!")
                time.sleep(2)
                cmail()
            sub=input("Subject: ")
            sub=sub.replace("'", "\\'")
            sub=sub.replace('"', '\\"')
            cont=input("Content: ")
            cont=cont.replace("'", "\\'")
            cont=cont.replace('"', '\\"')
            attachmnt=input("Attachment? Yes/No: ")
            attachmnt=attachmnt.lower()
            file=""
            filename="None"
            try:
                def fileconv(filename):
                    with open(filename, 'rb') as f:
                        fileblob = f.read()
                    return fileblob
                    print("File Uploaded Sucessfully!")
                if attachmnt=="yes" or attachmnt=="y":
                    filename=input("Enter Filename: ")
                    file_stats = os.stat(filename)
                    file_stats=(file_stats.st_size/1024/1024)
                    if file_stats>1.0:
                        print("You cannot upload a file with size Greater Than 1 MB!")
                        time.sleep(4)
                        mail()
                    else:
                        file=fileconv(filename)
            except:
                    print("Probably File doesn't Exist!")
                    time.sleep(2)
                    cmail()
            tandd=datetime.today()
            tandd=tandd.strftime("%c")
            sql_query="""insert into """+ccl+""" (Subject,Mail,SentBy,date,Attachment,AttachFormat) values(%s,%s,%s,%s,%s,%s)"""
            data_store=(sub,cont,xl,tandd,file,filename)
            result=c.execute(sql_query,data_store)
            dbc.commit()
            print("")
            print("Email Sent")
            print("")
            time.sleep(1)
            mail()
        def frlist():
            logo()
            print("Welcome to MetaFriends list")
            xl=str.lower(x)
            fuser='f%s'%xl
            usr=None
            c.execute("select * from %s"%fuser)
            for usr in c.fetchall():
                print(usr)           
            g=input("Enter 1 to add a Friend, 2 to Remove a Friend or 3 to return to Mail Box: ")
            
            def adfr():
                clear()
                logo()
                ic=6
                t="0"
                adusr=""
                adusr=input("Enter Username of your Friend: ")
                adusr=adusr.replace("'", "\\'")
                adusr=adusr.replace('"', '\\"')
                adusr2="'%s'" %adusr
                adusr2l=str.lower(adusr2)
                if adusr=="":
                    frlist()
                else:pass
                c.execute("select * from user")
                for i in c.fetchall():
                    if i[0]==adusr2l:
                        t="1"
                if t=="1":
                    c.execute('insert into %s values("%s")'%(fuser,adusr))
                    dbc.commit()
                else:
                    print("Username Not Found!")
                    adfr()
                c.execute("select * from %s"%fuser)
                usr=None
                for usr in c.fetchall():
                    print(usr)
                while ic==6:
                    frlist()
            def rmfr():
                logo()
                ic=6
                adusr=""
                adusr=input("Enter Username of your Friend: ")
                adusr=adusr.replace("'", "\\'")
                adusr=adusr.replace('"', '\\"')
                adusrl=str.lower(adusr)
                if adusr=="":
                    frlist()
                else:pass
                c.execute('delete from %s where Friend="%s";'%(fuser,adusrl))
                dbc.commit()
                while ic==6:
                    frlist()
                
                                                   
            if g=="1":
                adfr()
            elif g=="2":
                rmfr()
            elif g=="3":
                mail()
            else:frlist()
            
        def mail():
            trep=1
            def em():
                clear()
                logo()
                global xl
                print("Inbox")
                xl=str.lower(x)
                dbc.reset_session()
                c.execute("Select Subject,Mail,SentBy,date from %s " % xl)
                for row in c.fetchall():
                    controw=row[1]
                    if len(controw)>50:
                        controw=controw[0:50]+"...."
                    print(" ")
                    print("Subject:",row[0],"|","Content:",controw,"|","From:",row[2],"|","On:",row[3])
                    print(" ")
                print("Your Friends List")
                
                fuser='f%s'%xl

                c.execute("select * from %s"%fuser)
                for usr in c.fetchall():
                    print(usr)
            em()
            lo=input("Enter 1 to Refresh Mail Box, 2 to Read Mail, 3 to Compose Mail, 4 to Delete Mail, 5 to Edit Friends List or 6 to Logout: ")
            def rmail():
                logo()
                print("Read Mail")
                def retmailconf():
                    retconf=input("Return to Inbox? Yes/No: ")
                    retconf=retconf.lower()
                    if retconf=="yes" or retconf=="y":
                        mail()
                    else:
                        retmailconf()
                c.execute('select Subject,Mail,SentBy,Attachment,AttachFormat from %s where date="%s" and Subject="%s"'%(xl,rdate,rsubj))
                for dat in c.fetchall():
                    subjectdat=dat[0]
                    maildata=dat[1]
                    sentbydata=dat[2]
                    attachment=dat[3]
                    filename=dat[4]
                try:
                    print("Subject: ",subjectdat)
                    print("Content: ",maildata)
                    print("Sent by: ",sentbydata)
                except:
                    print("Mail not found with <%s> subject and <%s> date! Maybe there is an extra 'Space' in between!"%(rsubj,rdate))
                    time.sleep(5)
                    mail()
                if filename!="None":
                    conf=input("Do you want to download the Attachment? Yes/No: ")
                    conf=conf.lower()
                    if conf=="yes" or conf=="y":
                        try:
                            def convblob(attachment):
                                with open(filename,"wb") as f:
                                    f.write(attachment)
                            convblob(attachment)
                            print("Attachment Downloaded Sucessfully in the MetaMail folder")
                            time.sleep(1)
                            downloaded=1
                        except:
                            print("Unknown Error Occured! Error While Downloading the attachment!")
                            retmailconf()
                            downloaded=2
                        if downloaded==1:
                            retmailconf()
                    else:
                        retmailconf()
                else:
                    print("No Attachment Found!")
                    retmailconf()
            if lo=="1":
                while trep>0:
                    mail()
            elif lo=="4":
                delmail()
            elif lo=="6":
                logout()
            elif lo=="2":
                rsubj=input("Enter the Subject of the Mail: ")
                rdate=input("Enter the Date and Time of the Mail: ")
                if rdate=="":
                    print("Unknown date!")
                    time.sleep(2)
                    mail()
                else:
                    rmail()
            elif lo=="3":
                cmail()
            elif lo=="5":
                frlist()
            elif lo=="":mail()
            else:em()
            
        def error404():
            print("")
            print("Error 404! Account not found")
            time.sleep(2)
            print("")
            meta()
        def delmail():
            xl=str.lower(x)
            u="!@#$%^&*()'"
            u=input("Enter the subject of Email you wish to delete: ")
            u=u.replace("'", "\\'")
            u=u.replace('"', '\\"')
            dat=input("Enter the date and time of the Email you wish to delete: ")
            if u=="!@#$%^&*()'":mail()
            else:pass
            c.execute('delete from %s where Subject="%s" AND date="%s";' %(xl,u,dat))
            dbc.commit()
            print("")
            print("Email with subject <%s> and date <%s> has been deleted sucessfully " %(u,dat))
            print("")
            time.sleep(1)
            mail()
        clear()
        x=""
        xnew=""
        z=""
        znew=""
        logo()
        print("Welcome to MetaMail Login Page")
        x=input("Enter your Username: ")
        if x=="":
            print("This field can't be left Empty!")
            time.sleep(2)
            meta()
        x=x.replace("'", "\\'")
        x=x.replace('"', '\\"')
        xnew="'%s'" %x
        xnewl=str.lower(xnew)
        z=getpass.getpass("Enter your Password: ")
        def encrypt_string(z):
            sha_signature = \
                hashlib.sha256(z.encode()).hexdigest()
            return sha_signature
        sha_signature = encrypt_string(z)
        znew="'%s'" %sha_signature
        c.execute('SELECT * from user where ID= "%s" ' %xnewl)
        if c.fetchall()==[]:
        	error404()
        c.execute('SELECT * from user where ID= "%s" ' %xnewl)
        for row in c.fetchall():
            if row[1]==znew:
                mail()
            else:
                error404()
        dbc.commit()
    choice=input("Enter 1 to Login, 2 to Create New Account, 3 to Change Password (Forgot Password) or 4 to Exit: ")
    if choice=="1":
        login()
    elif choice=="2":
        cacc()
    elif choice=="":error()
    elif choice=="4":exit()
    elif choice=="3":cforpass()
    else:error()


d=10
while d<20:
    meta()


#Changelog:
    #Added Mail Delete functionality
    #Added Password with SHA-256 Encryption
    #Added Change Password Functionality
    #Fixed Same Username Conflict Bug
    #Fixed Random Username Create Mail Bug
    #Fixed Random Username Friend List Bug
    #Fixed General Issue Bugs
    #Fixed Major Issues
    #Added Logo Def.
    #Bug Fix: FriendList Bug Fixed
    #Added Multi OS Clear Functionality
    #Added IN-BUILT Update Feature
    #Fixed Major Bug in Database Text saving(<">and<'>)
    #Added 24x7 Running Server
    #Fixed variable Issue
    #Added support for auth_plugin='caching_sha2_password'
    #Connection Error Notif Added
    #Fixed Major "Change Password" Bug
    #Server Uplink
    #Added File Attachment Option
    #Fixed Variable Issue
    #Fixed Inbuilt Updater
