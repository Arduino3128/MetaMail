#Version 3.2.2
import requests
import re
import os
import time
def VerUp():
    print("Version Upto Date! Not Upgrading....")
    metaVersion.close()
    metamail.close()
    os.remove("MetaVersion.txt")
    os.rename("MetaMailPrev.py", "MetaMail.py")
    time.sleep(3)
    exit()
print("Welcome To MetaMail Updater.")
print("MetaMail_Updater is no longer supported by MetaMailSupport!")
try:
    os.rename("MetaMail.py", "MetaMailPrev.py")
    metamail=open("MetaMailPrev.py", "r")
    d=str(metamail.readline())
except:
    print("Error 404! File Not Found.")
    time.sleep(2)
    exit()
try:
    geturl1="https://raw.githubusercontent.com/Arduino3128/MetaMail/master/Version.txt"
    url=geturl1
    r1=requests.get(url, allow_redirects=True)
    open("MetaVersion.txt", "wb").write(r1.content)
except:
    print("Failed To Download.....Exiting...")
    os.rename("MetaMail.py", "MetaMailPrev.py")  
    res="Failed"
    time.sleep(5)
    exit()
try:
    metaVersion=open("MetaVersion.txt" , "r")
    c=str(metaVersion.readline())
except:
    print("MetaVersion.txt Not Found!")
if d<c:
    print("")
    print("Update Found! From %s >>>>>>>>> to %s"%(d,c))
    time.sleep(2)
    pass
else:VerUp()
        
geturl="https://raw.githubusercontent.com/Arduino3128/MetaMail/master/MetaMail.py"
res="0"
#os.rename("MetaMail.py", "MetaMailPrev.py")
try:
    metamail.close()
    url=geturl
    r=requests.get(url, allow_redirects=True)
    if url.find("/"):
        print(url.rsplit('/', 1)[1])
    open('MetaMail.py', "wb").write(r.content)
    print("Downloaded File Sucessfully..")
    res="Sucess"
     
except:
    print("Failed To Download.....")
    os.rename("MetaMail.py", "MetaMailPrev.py")  
    res="Failed"
try:
    try:
        metamail.close()
        if res=="Sucess":
            os.remove("MetaMailPrev.py")
            print("Sucessfully Updated MetaMail....")
        elif re=="Failed":
            print("Since Download Failed, Reverting All the changes.")

    except:
        print("Failed to Install.. Maybe Previous Version of 'MetaMail' does not exists..")
        os.rename("MetaMailPrev.py", "MetaMail.py")
        
except:
    print("Since File download Failed No changes have been made.....")
print("Exiting")
metamail.close()
metaVersion.close()
os.remove("MetaVersion.txt")
time.sleep(5)
exit()
