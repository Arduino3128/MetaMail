import time
import mysql.connector
print(" ")
print("Welcome to MetaMail Database Setup!")
print("")
time.sleep(2)
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
  port=portinput
  )
c = dbc.cursor()
print("Please Wait Setup is Running.....")
c.execute("CREATE DATABASE User;")
dbc.commit()
c.execute("USE User;")
c.execute("CREATE TABLE User(ID VARCHAR(255) PRIMARY KEY, Password LONGTEXT, ForgotQues LONGTEXT, ForgotPass LONGTEXT);")
dbc.commit()

print("")
print("Setup Finished Sucessfully!")
print("Exiting......")
print("")
time.sleep(5)
