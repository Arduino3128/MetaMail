from datetime import datetime
import time
import os
import  hashlib

clear=lambda:os.system("cls")
import getpass 
import mysql.connector
select=0
   
select=input("Enter 1 for LAN(localhost) or 2 for WAN(Internet) or Press Just 'Enter' to Customize Connection ")
if select=="1":
    userinput=input("Enter Username(Contact Admin For Username) ")
    passwdinput=input("Enter Password(Contact Admin For Password) ")
    portinput=input("Enter Port No. of the Server(Contact Admin For Port No.) ")
    hostinput="localhost"
elif select=="2":
    userinput=input("Enter Username(Contact Admin For Username) ")
    passwdinput=input("Enter Password(Contact Admin For Password) ")
    portinput=input("Enter Port No. of the Server(Contact Admin For Port No.) ")
    hostinput="o.tcp.ngrok.io"

else:
    userinput=input("Enter Username(Contact Admin For Username) ")
    passwdinput=input("Enter Password(Contact Admin For Password) ")
    portinput=input("Enter Port No. of the Server(Contact Admin For Port No.) ")
    hostinput=input("Enter host IP ")
    
dbc = mysql.connector.connect(
  host=hostinput,
  user=userinput,
  passwd=passwdinput,
  database="User",
  port=portinput
  )
c = dbc.cursor()
clear()
'''x=input("Enter your Username")
#y=int(input("Enter Addr no"))
z=input("Enter Your password")'''

"""print('''
                  _                          _  _   ____      ___  
     /\/\    ___ | |_   __ _   /\/\    __ _ (_)| | |___ \    /_  | 
    /    \  / _ \| __| / _` | /    \  / _` || || |   __) |     | | 
   / /\/\ \|  __/| |_ | (_| |/ /\/\ \| (_| || || |  / __/     _| |
   \/    \/ \___| \__| \__,_|\/    \/ \__,_||_||_| |_____|(_)|____|
'''
)"""


"""print('''

 

     e    e                  d8                                     ,e, 888       _-~88e        /~~88b       /~~88b 
    d8b  d8b      e88~~8e  _d88__   /~~~8e  888-~88e-~88e   /~~~8e   "  888          888b      |   888      |   888 
   d888bdY88b    d888  88b  888         88b 888  888  888       88b 888 888        __888"      `  d88P      `  d88P 
  / Y88Y Y888b   8888__888  888    e88~-888 888  888  888  e88~-888 888 888          888e        d88P         d88P  
 /   YY   Y888b  Y888    ,  888   C888  888 888  888  888 C888  888 888 888          888P d88b  d88P   d88b  d88P   
/          Y888b  "88___/   "88_/  "88_-888 888  888  888  "88_-888 888 888       ~-_88"  Y88P d88P___ Y88P d88P___ 
                                                                                                                    

''')"""
print('''

 ,ggg, ,ggg,_,ggg,                              ,ggg, ,ggg,_,ggg,                                ad888888b,       ad888888b,       ad888888b, 
dP""Y8dP""Y88P""Y8b             I8             dP""Y8dP""Y88P""Y8b                    ,dPYb,    d8"     "88      d8"     "88      d8"     "88 
Yb, `88'  `88'  `88             I8             Yb, `88'  `88'  `88                    IP'`Yb            a88               88               88 
 `"  88    88    88          88888888           `"  88    88    88               gg   I8  8I           ,88P              d8P              d8P 
     88    88    88             I8                  88    88    88               ""   I8  8'         aad8"              a8P              a8P  
     88    88    88   ,ggg,     I8      ,gggg,gg    88    88    88    ,gggg,gg   gg   I8 dP          ""Y8,            ,d8P             ,d8P   
     88    88    88  i8" "8i    I8     dP"  "Y8I    88    88    88   dP"  "Y8I   88   I8dP             `88b         ,d8P'            ,d8P'    
     88    88    88  I8, ,8I   ,I8,   i8'    ,8I    88    88    88  i8'    ,8I   88   I8P               "88       ,d8P'            ,d8P'      
     88    88    Y8, `YbadP'  ,d88b, ,d8,   ,d8b,   88    88    Y8,,d8,   ,d8b,_,88,_,d8b,_     Y8,     a88  d8b a88"         d8b a88"        
     88    88    `Y8888P"Y88888P""Y88P"Y8888P"`Y8   88    88    `Y8P"Y8888P"`Y88P""Y88P'"Y88     "Y888888P'  Y8P 88888888888  Y8P 88888888888 
                                                                                                                                              
''')
print(" ")
print(" ")
print("Welcome to MetaMail 3.2.2, Best Off-Grid, Light-Weight and Secure E-mail Service with SHA-256 Encryptions")
def meta():
    def cforpass():
        foruser=input("Enter Your Username:")
        c.execute("Select * from user")
        for row in c.fetchall():
              print("Question: ", row[2])
        forpass=input("Enter Answer of the Question: ")
        def encrypt_string(forpass):
            sha_signature2 = \
                hashlib.sha256(forpass.encode()).hexdigest()
            return sha_signature2
        sha_signature2 = encrypt_string(forpass)
        nforpass="'%s'"%sha_signature2
        c.execute("select * from user")
        for row in c.fetchall():
              if nforpass==row[3]:
                    newpass=getpass.getpass("Enter New Password: ")
                    cnewpass=getpass.getpass("Re-enter the New Pasword: ")
                    def encrypt_string(newpass):
                        sha_signature = \
                            hashlib.sha256(newpass.encode()).hexdigest()
                        return sha_signature
                    sha_signature = encrypt_string(newpass)
                    if newpass==cnewpass:
                          c.execute('UPDATE user SET  Password="%s" where ID="%s"' %(sha_signature, foruser) )
                          print("You Have Sucessfullly Changed Your Password!")
                          tandd=datetime.today()
                          tandd=tandd.strftime("%c")
                          c.execute("insert into %s values('Password Changed','You have changed Your Password', 'Metamail Support', '%s')"%(foruser, tandd))
                    else:
                          print("Incorrect Password!")
                          time.sleep(1)
                          meta()
              else:
                    print("Incorrect Answer!")
                    time.sleep(1)
                    meta()
        
    def suser():
        print("Username not available! Try using a different One!")
        meta()
    def error():
        print("Unknown Action!")
        meta()
    def logout():
        print("Thank You for using MetaMail 3.2.2")
        print("Logging out......")
        print("Sucessfully Logged out")
        clear()
        o=input("Enter 1 to Login with Different Account and Press Enter to Exit ")
        if o=="1":
            meta()
        else:exit()

    def cacc():#------------------ERROR HERE NO SELECTION.
        print("Create Your account")
        #nuser=""
        #npass=""
        #cpass=""
        nuser=input("Enter Your Username ")
        npass=getpass.getpass("Enter your password ")
        def encrypt_string(npass):
            sha_signature = \
                hashlib.sha256(npass.encode()).hexdigest()
            return sha_signature
        sha_signature = encrypt_string(npass)
        nuser2="('%s',)" %nuser
        c.execute("Show tables")
        forques=input("Enter Your Question: ")
        forpass=input("Enter the answer to the Question: ")
        def encrypt_string(forpass):
            sha_signature2 = \
                hashlib.sha256(forpass.encode()).hexdigest()
            return sha_signature2
        sha_signature2 = encrypt_string(forpass)
        table=c.fetchall()
        #print(table)
        #if nuser2 in table:suser()
        #else: pass

        cnpass=getpass.getpass("Re-enter the Password ")
        if nuser=="" or npass=="":
            error()
        else:pass
        c.execute('select * from user where ID="%s"' % nuser)
        data="error"
        for i in c:
            data=i
        if data !="error":suser()
        else:pass
        
            
        '''i=0
        while i<len(table):
            
            if nuser2==table[i]:suser()
            else:pass
            i+=1'''
        def crmail():
            fuser='f%s'%nuser
            c.execute('insert into user values("%s","%s","%s","%s")', (nuser, sha_signature, forques, sha_signature2))
            c.execute('create table %s(Subject varchar(255), Mail LONGTEXT, SentBy varchar(255), date varchar(255))' %nuser)
            c.execute('create table %s(Friend varchar(100))'%fuser)
            tandd=datetime.today()
            tandd=tandd.strftime("%c")
            c.execute('insert into %s values("Welcome To MetaMail", "Welcome to MetaMail %s", "MetaMail Support","%s")' %(nuser,nuser,tandd))      
            dbc.commit()
        #c.exexute('select * from %s',% nuser)
        #print("Account Created Sucessfully!")
            login()                       
        if npass==cnpass and npass!="":
            #print("Account Created Sucessfully!")
            crmail()
        else:print("Password Didn't Matched!") and cacc()

                

    def login():
        def uerror():#error here!
            print("")
            print("Username not found! Returning to your Mail box")
            print("")
            def ermail():
                mail()
            ermail()
        def cmail():
            clear()
            print("Compose Mail")
            fuser='f%s'%x
            c.execute("select * from %s"%fuser)
            for usr in c.fetchall():
                print(usr)
            cc=input("To: ")
            ncc="'%s'" %cc
            sub=input("Subject: ")
            cont=input("Content: ")
            if cc=="":
                uerror()
            else:pass
            list=(None)
            c.execute("Select ID from user")
            row3=c.fetchall()
            if ncc or cc in row3 :
                    pass
            else:print("Not Found!")
            tandd=datetime.today()
            tandd=tandd.strftime("%c")
            c.execute('insert into %s values("%s","%s","%s","%s")'%(cc, sub, cont,x,tandd))
            print("")
            print("Email Sent")
            print("")
            dbc.commit()
            time.sleep(1)
            mail()
        def frlist():
            print("Welcome to MetaFriends list ")
            g=input("Enter 1 to add a Friend, 2 to Remove a Friend or 3 to return to Mail Box ")
            fuser='f%s'%x
            c.execute("select * from %s"%fuser)
            for usr in c.fetchall():
                print(usr)
            def adfr():
                i=6
                adusr=input("Enter Username of your Friend ")
                c.execute('insert into %s values("%s")'%(fuser,adusr))
                dbc.commit()
                c.execute("select * from %s"%fuser)
                for usr in c.fetchall():
                    print(usr)
                while i==6:
                    frlist()
            def rmfr():
                i=6
                adusr=input("Enter Username of your Friend ")
                c.execute('delete from %s where Friend="%s";'%(fuser,adusr))
                dbc.commit()
                c.execute("select * from %s"%fuser)
                for usr in c.fetchall():
                    print(usr)
                while i==6:
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
                print("Welcome To Your Inbox")
                dbc.reset_session()
                c.execute("Select * from %s " % x)
                for row in c.fetchall():
                    print(" ")
                    print("Subject:",row[0],"|","Content:",row[1],"|","From:",row[2],"|","On:",row[3])
                    print(" ")
                print("Your Friends List")
                
                fuser='f%s'%x

                c.execute("select * from %s"%fuser)
                for usr in c.fetchall():
                    print(usr)
            em()
            lo=input("Enter 1 to Refresh Mail Box, 2 to Create Mail, 3 to Delete Mail, 4 to Edit Friends List and 5 to Logout ")
            if lo=="1":
                while trep>0:
                    mail()
            elif lo=="3":
                delmail()
            elif lo=="5":
                logout()
            elif lo=="2":
                cmail()
            elif lo=="4":
                frlist()
            elif lo=="":mail()
            else:em()
            
        def error404():
            print("")
            print("Error 404! Account not found")
            print("")
            meta()
        def delmail():
            u=""
            #c.execute("select * from %s" % x)
            u=input("Enter the subject of Email you wish to delete ")
            dat=input("Enter the date and time of the Email you wish to delete ")
            if u=="":mail()
            else:pass
            c.execute('delete from %s where Subject="%s" AND date="%s";' %(x,u,dat))
            dbc.commit()
            print("")
            print("Email with subject <%s> has been deleted sucessfully and date <%s>" %(u,dat))
            print("")
            time.sleep(1)
            mail()
        clear()
        x=""
        xnew=""
        z=""
        znew=""
        print("Welcome to MetaMail Login Page")
        x=input("Enter your Username ")
        xnew="'%s'" %x
        #y=int(input("Enter Addr no"))
        z=getpass.getpass("Enter Your Password ")
        def encrypt_string(z):
            sha_signature = \
                hashlib.sha256(z.encode()).hexdigest()
            return sha_signature
        sha_signature = encrypt_string(z)
        znew="'%s'" %sha_signature
        c.execute('SELECT * from user where ID= "%s" ' % xnew)
        for row in c.fetchall():
            if row[1]==znew:
                mail()
            else:error404()
        dbc.commit()
    choice=input("Enter 1 to Login, 2 to Create New Account, 3 to Change Password (Forgot Password) or 4 to Exit ")
    if choice=="1":
        login()
    elif choice=="2":
        cacc()
    elif choice=="":error()
    elif choice=="4":exit()
    elif choice=="3":cforpass()
    else:error()
    #choice=int(input("Enter 1 to login and 2 to create new account"))

'''def acc():
    c.execute("Select * from %s" % x)
    for row in c.fetchall():
        print(row)'''


d=10
while d<20:
    meta()


#Changelog:
    #Added Mail Delete functionality
    #Added Password with SHA-256 Encryption
    #Added Change Password Functionality
    

