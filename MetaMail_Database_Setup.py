import time
import os
import random
import subprocess
import platform
osident=platform.system()
if "Windows" in osident:
    clear=lambda:os.system("cls")
elif "Linux" in osident:
    clear=lambda:os.system("clear")
elif "Darwin" in osident:
    clear=lambda:os.system("clear")
else:
    print("Unknown O.S. Using Default 'Windows Configuration'")
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
try:
   import mysql.connector
except:
   logo()
   print("MySQL Connector not found! Starting 'mysql-connector-python' Module installing Procedure!")
   if osident=="Windows":
       piploc=input("Enter the directory path of Python: ")
       subprocess.call("cd %s/Scripts && pip install mysql-connector-python "%piploc, shell=True)
       subprocess.call("MetaMail_Database_setup.py", shell=True)
   elif osident=="Linux" or osident=="Darwin":
       subprocess.call("pip install mysql-connector-python", shell=True)
       subprocess.call("python3 MetaMail_Database_setup.py", shell=True)
   else:
       print("Unknown OS, Try Installing 'mysql-connector-python' manually!")
   exit()
   time.sleep(5)
logo()
print(" ")
print("Welcome to MetaMail Database Setup!")
print("")
time.sleep(2)
userinput=input("Enter Username(Contact Admin For Username) ")
passwdinput=input("Enter Password(Contact Admin For Password) ")
portinput=input("Enter Port No. of the Server(Contact Admin For Port No.) ")
hostinput=input("Enter host IP ")
   
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
    port=portinput,
    auth_plugin='caching_sha2_password')
except:
    connerr()
c = dbc.cursor()
logo()
dbinput=input("Enter Database Name/ID: ")
print("Please Wait Setup is Running.....")
c.execute("CREATE DATABASE %s;"%dbinput")
dbc.commit()
c.execute("USE %s;"%dbinput)
c.execute("CREATE TABLE user(ID VARCHAR(255) PRIMARY KEY, Password LONGTEXT, ForgotQues LONGBLOB, ForgotPass LONGTEXT);")
dbc.commit()
c.execute('insert into user values("user","None","Not Applicable","None")')
dbc.commit()
print("")
print("Setup Finished Sucessfully!")
print("Exiting......")
print("")
time.sleep(5)
