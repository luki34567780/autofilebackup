import sys
import os
if(len(sys.argv) == 2):
    debug = sys.argv[1]
else:
    debug = "n"
librarys = ("pytest-shutil", "mcrcon")
if(debug == "y"):
    print("##################################################")
    print("Start Debug")
    print(os.name)
    for x in range(len(librarys)):
        print("Library: ", librarys[x])
    print("End Debug")
    print("##################################################")
if(os.name == "nt"):
    print("Installing dependencies")
    for x in range(len(librarys)):
        os.system("python3 -m pip install " + librarys[x])
    print("Installed dependencies")
    sys.exit(0)
if(os.name != "nt"):
    print("This script runs oly for Windows right now, sorry!")
    print("Please install all dependencies manually.")
    print("List of needed dependencies:")
    for x in range(len(librarys)):
        print(librarys[x])
    
    sys.exit(1)
sys.exit(0)