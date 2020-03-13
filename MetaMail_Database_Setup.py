import time
import subprocess
import platform
osident=platform.system()
try:
   import mysql.connector
except:
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
    print("Connection Error! Maybe the Server is down! Try Again Later!")
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
print("Please Wait Setup is Running.....")
c.execute("CREATE DATABASE metamailuser;")
dbc.commit()
c.execute("USE metamailuser;")
c.execute("CREATE TABLE user(ID VARCHAR(255) PRIMARY KEY, Password LONGTEXT, ForgotQues LONGTEXT, ForgotPass LONGTEXT);")
dbc.commit()

print("")
print("Setup Finished Sucessfully!")
print("Exiting......")
print("")
time.sleep(5)
