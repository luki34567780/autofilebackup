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
    print("Abhängigkeiten werden installiert...")
    for x in range(len(librarys)):
        os.system("python3 -m pip install " + librarys[x])
    print("Abhängigkeiten wurden installiert.")
    sys.exit(0)
if(os.name != "nt"):
    print("Dieses Script kann aktuell nur unter Windows genutzt werden")
    print("Bitte installieren sie die Abhängigkeiten manuell")
    print("Liste der benötigten Abhängigkeiten:")
    for x in range(len(librarys)):
        print(librarys[x])
    
    sys.exit(1)
sys.exit(0)