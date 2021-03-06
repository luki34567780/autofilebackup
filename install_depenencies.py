import sys
import os
import time
import urllib.request

url = 'https://bootstrap.pypa.io/get-pip.py'

if(len(sys.argv) == 2):
    debug = sys.argv[1]
else:
    debug = "n"
librarys = ("pytest-shutil", "mcrcon")
urllib.request.urlretrieve(url,r'get-pip.py')
time.sleep(5)
os.system("python get-pip.py")
time.sleep(5)
if(debug == "y"):
    print("##################################################")
    print("Start Debug")
    print(os.name)
    for x in range(len(librarys)):
        print("Library: ", librarys[x])
    print("End Debug")
    print("##################################################")
if(os.name == "nt"):
    print("Installing to nt system")
    print("Installing dependencies")
    for x in range(len(librarys)):
        os.system("python3 -m pip install " + librarys[x])
    print("Installed dependencies")
    sys.exit(0)
if(os.name == "posix"):
    print("Installinx to posix system")
    print("Installing dependencies")
    for x in range(len(librarys)):
        os.system("python3 -m pip install " + librarys[x])
    print("Installed dependencies")
if(os.name == "unix"):
    print("Installinx to unix system")
    print("Installing dependencies")
    for x in range(len(librarys)):
        os.system("python3 -m pip install " + librarys[x])
    print("Installed dependencies")
if(os.name != "nt") and (os.name != "posix") and (os.name != "unix"):
    install_anyway = input("Do you want to try installing anyway? (Y/n): ")
    if (install_anyway == "n"):
        print("Please install all dependencies manually.")
        print("List of needed dependencies:")
        for x in range(len(librarys)):
            print(librarys[x])
    else:
        print("Trying installing to ", os.name, "...")
        print("Installing dependencies")
        for x in range(len(librarys)):
            os.system("python3 -m pip install " + librarys[x])
        print("Installed dependencies")
    sys.exit(1)
sys.exit(0)