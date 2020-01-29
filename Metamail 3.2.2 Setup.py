import time
import mysql.connector
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
print("Welcome to MetaMail 3.2.2 Setup!")
print("Welcome to MetaMail 3.2.2, Best Off-Grid, Light-Weight and Secure E-mail Service with SHA-256 Encryptions")
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
