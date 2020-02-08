import requests
import re
import os
import time
print("Welcome To MetaMail Updater.")
geturl=input('Enter "Update Server" Address(Visit: www.github.com/Arduino3128/MetaMail/blob/master/"Update Server" Address) ')
res="0"
os.rename("MetaMail.py", "MetaMailPrev.py")
try:
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
time.sleep(5)
exit()
