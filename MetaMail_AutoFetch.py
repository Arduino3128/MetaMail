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
                            ███╗   ███╗███████╗████████╗ █████╗ ███╗   ███╗ █████╗ ██╗██╗         ██████╗    ██████╗ ██╗  ██╗
                            ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗████╗ ████║██╔══██╗██║██║         ╚════██╗   ╚════██╗██║  ██║
                            ██╔████╔██║█████╗     ██║   ███████║██╔████╔██║███████║██║██║          █████╔╝    █████╔╝███████║
                            ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║╚██╔╝██║██╔══██║██║██║          ╚═══██╗   ██╔═══╝ ╚════██║
                            ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██║ ╚═╝ ██║██║  ██║██║███████╗    ██████╔╝██╗███████╗██╗  ██║
                            ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝
                                                    [Script By: Kanad Nemade | Github: Arduino3128]
            \n'''%colour)
    print(" ")
    print(" ")
    print("Welcome to MetaMail 3.2.4, Best Off-Grid, Light-Weight and Secure E-mail Service with SHA-256 Encryptions")
    print("")
    print("")
try:
   import mysql.connector
   import requests
except:
   print("'MySQL Connector or Requests' not found! Starting 'Requests and MySQL Connector' Module installing Procedure!")
   if osident=="Windows":
       piploc=input("Enter the directory path of Python: ")
       subprocess.call("cd %s/Scripts && pip install mysql-connector-python requests"%piploc, shell=True)
       subprocess.call("MetaMail_AutoFetch.py", shell=True)
   elif osident=="Linux" or osident=="Darwin":
       subprocess.call("pip install requests mysql-connector-python", shell=True)
       subprocess.call("python3 MetaMail_AutoFetch.py", shell=True)
   else:
       print("Unknown OS, Try Installing 'mysql-connector-python & requests' manually!")
   exit()
   time.sleep(5)
logo()
print("Welcome to MetaMail AutoFetch Installer")

print("""



""")
print("""End-User License Agreement (EULA) of MetaMail

This End-User License Agreement ("EULA") is a legal agreement between you and MetaMail.Inc

This EULA agreement governs your acquisition and use of our MetaMail software ("Software") directly from MetaMail.Inc or indirectly through a MetaMail.Inc authorized reseller or distributor (a "Reseller").

Please read this EULA agreement odcarefully before completing the installation process and using the MetaMail software. It provides a license to use the MetaMail software and contains warranty information and liability disclaimers.

If you register for a free trial of the MetaMail software, this EULA agreement will also govern that trial. By clicking "accept" or installing and/or using the MetaMail software, you are confirming your acceptance of the Software and agreeing to become bound by the terms of this EULA agreement.

If you are entering into this EULA agreement on behalf of a company or other legal entity, you represent that you have the authority to bind such entity and its affiliates to these terms and conditions. If you do not have such authority or if you do not agree with the terms and conditions of this EULA agreement, do not install or use the Software, and you must not accept this EULA agreement.

This EULA agreement shall apply only to the Software supplied by MetaMail.Inc herewith regardless of whether other software is referred to or described herein. The terms also apply to any MetaMail.Inc updates, supplements, Internet-based services, and support services for the Software, unless other terms accompany those items on delivery. If so, those terms apply. This EULA was created by MetaMail.Inc for MetaMail.
License Grant

MetaMail.Inc hereby grants you a personal, non-transferable, non-exclusive licence to use the MetaMail software on your devices in accordance with the terms of this EULA agreement.

You are permitted to load the MetaMail software (for example a PC, laptop, mobile or tablet) under your control. You are responsible for ensuring your device meets the minimum requirements of the MetaMail software.

You are not permitted to:

    Edit, alter, modify, adapt, translate or otherwise change the whole or any part of the Software nor permit the whole or any part of the Software to be combined with or become incorporated in any other software, nor decompile, disassemble or reverse engineer the Software or attempt to do any such things
    Reproduce, copy, distribute, resell or otherwise use the Software for any commercial purpose
    Allow any third party to use the Software on behalf of or for the benefit of any third party
    Use the Software in any way which breaches any applicable local, national or international law
    Use the Software for any purpose that MetaMail.Inc considers is a breach of this EULA agreement

Intellectual Property and Ownership

MetaMail.Inc shall at all times retain ownership of the Software as originally downloaded by you and all subsequent downloads of the Software by you. The Software (and the copyright, and other intellectual property rights of whatever nature in the Software, including any modifications made thereto) are and shall remain the property of MetaMail.Inc.

MetaMail.Inc reserves the right to grant licences to use the Software to third parties.
Termination

This EULA agreement is effective from the date you first use the Software and shall continue until terminated. You may terminate it at any time upon written notice to MetaMail.Inc.

It will also terminate immediately if you fail to comply with any term of this EULA agreement. Upon such termination, the licenses granted by this EULA agreement will immediately terminate and you agree to stop all access and use of the Software. The provisions that by their nature continue and survive will survive any termination of this EULA agreement.
Governing Law

This EULA agreement, and any dispute arising out of or in connection with this EULA agreement, shall be governed by and construed in accordance with the laws of in.
            """)
print("")
print("")
rt="0"
def End():
    print("All Files Downloaded Sucessfully...")
    print("Please Read 'ReadMe.txt' First")
    print("Exiting....")
    time.sleep(5)
    exit()
Agreement=input("Do You Agree this EULA? Yes/No/y/n: ")
logo()
print("Welcome to MetaMail AutoFetch Installer")
def GetAdv():
    try:
        geturl1="https://raw.githubusercontent.com/Arduino3128/MetaMail/master/MetaMail.py"
        r=requests.get(geturl1, allow_redirects=True)
        open("MetaMail.py",'wb').write(r.content)
        print("MetaMail.py Downloaded Sucessfully.")
    except:
        print("Error! Failed To download MetaMail.py...Exiting..")
        time.sleep(2)
        exit()
    try:
        geturl1="https://github.com/Arduino3128/MetaMail/raw/master/MetaMail.exe"
        print("Downloading Windows version of MetaMail! This Process May Take a while!")
        r=requests.get(geturl1, allow_redirects=True)
        open("MetaMail.exe",'wb').write(r.content)
        print("MetaMail.exe Downloaded Sucessfully.")
    except:
        print("Error! Failed To download MetaMail.exe...Exiting..")
        time.sleep(2)
        exit()    
    try:
        geturl2="https://raw.githubusercontent.com/Arduino3128/MetaMail/master/MetaMail_Updater.py"
        r2=requests.get(geturl2, allow_redirects=True)
        open("MetaMail_Updater.py", "wb").write(r2.content)
        print("MetaMail_Updater.py Downloaded Sucessfully.")
    except:
        print("Error! Failed To download MetaMail Updater.py...Exiting..")
        time.sleep(2)
        exit()        
    try:
        geturl3="https://raw.githubusercontent.com/Arduino3128/MetaMail/master/MetaMail_Database_Setup.py"
        r3=requests.get(geturl3, allow_redirects=True)
        open("MetaMail_Database_Setup.py",'wb').write(r3.content)
        print("MetaMail_Database_Setup.py Downloaded Sucessfully.")
    except:
        print("Error! Failed To download MetaMail Database Setup.py...Exiting..")
        time.sleep(2)
        exit()
    try:
        geturl4="https://raw.githubusercontent.com/Arduino3128/MetaMail/master/ReadMe%20First.txt"
        r4=requests.get(geturl4, allow_redirects=True)
        open("ReadMe.txt",'wb').write(r4.content)
        print("ReadMe.txt Downloaded Sucessfully.")
        rt="1"
    except:
        print("Error! Failed To download ReadMe.txt...Exiting..")
        time.sleep(2)
        exit()
    if rt=="1":
        End()
    elif rt=="0":
        print("Something Went Wrong....")
        print("Delete any file Downloaded and Try Again....")
        print("Exiting...")
        time.sleep(5)
        exit()
def GetBas(cselect):
       if cselect=="1" or cselect=="Windows":
          geturl1="https://github.com/Arduino3128/MetaMail/raw/master/MetaMail.exe"
          err="Error! Failed To download MetaMail.exe...Exiting.."
          succ="MetaMail.exe Downloaded Sucessfully."
          vername="MetaMail.exe"
          print("Downloading Windows version of MetaMail! This Process May Take a while!")
       else:
          geturl1="https://raw.githubusercontent.com/Arduino3128/MetaMail/master/MetaMail.py"
          err="Error! Failed To download MetaMail.py...Exiting.."
          succ="MetaMail.py Downloaded Sucessfully."
          vername="MetaMail.py"
       try:
              r=requests.get(geturl1, allow_redirects=True)
              open(vername,'wb').write(r.content)
              print(succ)
              time.sleep(2)
       except:
              print(err)
              time.sleep(2)
              exit()
       try:
              geturl4="https://raw.githubusercontent.com/Arduino3128/MetaMail/master/ReadMe%20First.txt"
              r4=requests.get(geturl4, allow_redirects=True)
              open("ReadMe.txt",'wb').write(r4.content)
              print("ReadMe.txt Downloaded Sucessfully.")
              time.sleep(2)
              rt="1"
       except:
              print("Error! Failed To download ReadMe.txt...Exiting..")
              time.sleep(2)
              exit()
       if rt=="1":
              End()
       elif rt=="0":
              print("Something Went Wrong....")
              print("Delete any file Downloaded and Try Again....")
              print("Exiting...")
              time.sleep(2)
              exit()
def ModSel():
       mode=input("Enter 1 for Basic Download or 2 for Advance Download(Default:1): ")
       if mode=="2":
           GetAdv()
       else:
           osget=input("Enter 1 for Windows Version and 2 for Cross Platform Compatible Python Version(Default:OS Identification): ")
           if osget=="1":
                   GetBas("1")
           elif osget=='2':
                    GetBas("2")
           else:
               GetBas(osident)
                
if Agreement=="Yes" or Agreement=="yes" or Agreement=="y" or Agreement=="Y":
       ModSel()
else:
    print("Agreement Denied!")
    print("Exiting...")
    time.sleep(3)
    exit()
