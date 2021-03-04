try:
    from os import system
    from os import path
    import shutil
    import time
    from datetime import datetime
    import sys
    import os
    import string
except:
    print("Looks like some dependencys are missing!")
    print("Please ry running install.py!")
    time.sleep(15)
    raise EnvironmentError("missing dependencys!")
dir_or_file = "n/a"
debug = "n"
debugtime = "n"
source = "n/a"
diskspeed = 50
try:
    readini()
except:
    time.sleep(0)
def readini():
    config_array_rdy = []
    with open('config.cfg') as my_file:
        config_array = my_file.readlines()
        for x in len(config_array):
            if(config_array[x].startswith("source=")):
                config_array[x].strip("source=")
                config_array_rdy[0] = config_array[x]
            if(config_array[x].startswith("backuptime=")):
                config_array[x].strip("backuptime=")
                config_array_rdy[1] = config_array[x]
            if(config_array[x].startwith("maxbackups=")):
                config_array[x].strip("maxbackups=")
                config_array_rdy[2] = config_array[x]
            if(config_array[x].startwith("diskspeed=")):
                config_array[x].strip("diskspeed=")
                config_array_rdy[3] = config_array[x]
            return(config_array_rdy)
def doespathexist(source):
    if(os.path.isfile) and (os.path.isdir):
        return(True)
    return(False)

    

def getFolderSize(folder,debug):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath, debug)
    return total_size
def gettimedate(debug):
    now = datetime.now()
    dt_string = now.strftime("%d.%m.%Y..%H.%M.%S")
    return dt_string
def copyfile(speed, source, maxbackups, backuptimesec, debug, timedebug):
    counterint = 0
    while(int(counterint) <= int(maxbackups)):
        counterint = int(counterint) + 1
        print('Copy number', counterint, 'started')
        date_time = gettimedate(debug)
        counter = "." + date_time
        destination = source + counter  

        if(debug == "y"):
            print("###############################")
            print("Start Debug 3")
            print(source)
            print(destination)
            print(counter)
            print(counterint)
            print(int(maxbackups))
            print(backuptimesec)
            print(date_time)
            print(debug)
            print("end Debug 3")
            print("###############################")
            time.sleep(5)
        
        if(int(counterint) == int(maxbackups) + 1 and int(maxbackups) != 0 ):
            return 0

        try:
            shutil.copyfile(source, destination)
        except:
            print("Error while copying!")
            print("Do you have rights to copy this folder or is the file opened in any other programm?")
            print("Script will exit now. If you want the program to continue enable debug mode!")
            time.sleep(15)
            raise ValueError("Error while copying file")
        if(debug == "y"):
            print("##################################################")
            print("Debug start")
            print("File Size: ",getFileSize(source,debug))
            print("Wartezeit ohne konvertirung zu int: ",getFileSize(source, debug) /  1000000 / (int(float(speed) * 0.8)))
            print("Wartezeit mit Konvertirung zu int: ",int(getFileSize(source, debug) /  1000000 / (int(float(speed) * 0.8))))
            print("Debug end")
            print("#################################################")
        time.sleep(getFileSize(source, debug) /  1000000 / int(round(float(speed) * 0.8, 0)))
        counter = "." + str(counterint)
        if(timedebug == "y"):
            time.sleep(5)
        else:
            time.sleep(backuptimesec)
    return 0
def min2sec(timemin, debug):
    timesec = int(timemin) * 60
    if(debug == "y"):
        print("###############################")
        print("Start Debug 1")
        print(timemin)
        print(timesec)
        print("end Debug 1")
        print("###############################")
    return timesec
def copydir(speed, source, maxbackus, backuptime, debug, timedebug):
    counterint = 0
    while(int(counterint) <= int(maxbackups)):
        counterint = int(counterint) + 1
        print('Copy Nr.', counterint, 'started')
        date_time = gettimedate(debug)
        counter = "." + date_time
        destination = source + counter  

        if(debug == "y"):
            print("###############################")
            print("Start Debug 3")
            print(source)
            print(destination)
            print(counter)
            print(counterint)
            print(int(maxbackups))
            print(backuptimesec)
            print(date_time)
            print(debug)
            print("end Debug 3")
            print("###############################")
            time.sleep(5)
        
        if(int(counterint) == (int(maxbackups) + 1) and int(maxbackups) != 0 ):

            return 0
        try:
            shutil.copytree(source, destination)
        except:
            print("Error while Copying!")
            print("Do you have Rihts to copy this Folder or is any file opend in another program?")
            print("Program will exit. If you want the program to ignore the error please enable Debug mode!")
            if(debug == "y"):
                time.sleep(0)
            else:
                time.sleep(15)
                raise ValueError("Copy error")
        if(debug == "y"):
            print("##################################################")
            print("Debug start")
            print("Folder Size: ",getFolderSize(source,debug))
            print("Wartezeit ohne konvertirung zu int: ",getFolderSize(source, debug) /  1000000 / (int(float(speed) * 0.8)))
            print("Wartezeit mit Konvertirung zu int: ",int(getFolderSize(source, debug) /  1000000 / (int(float(speed) * 0.8))))
            print("Debug end")
            print("#################################################")
        time.sleep(getFolderSize(source, debug) /  1000000 / int(round(float(speed) * 0.8, 0)))
        counter = "." + str(counterint)
        print('Copy Nr.', counterint, ' finished')
        if(timedebug == "y"):
            time.sleep(5)
        else:
            time.sleep(backuptimesec)
    return 0
def getFileSize(source,debug):
    filesizebites = os.path.getsize(source)
    return filesizebites

try:
    system("cls")
except:
    system("clear")
if(len(sys.argv) >= 2):
    if(str(sys.argv[1]) == "h"):
        print("Hilfeseite für Luki's Autofilebackup")
        print("################################################################################")
        print("Aufbau")
        print("[dir or file] [source] [Interval] [max backups]")
        print("################################################################################")
        print("d            Setzt einen Ordner als Ziel(veraltet, Programm erkennt automatisch ob Ordner oder Datei)")
        print("f            Setzt eine Datei als Ziel(veraltet, Programm erkennt automatisch ob Ordner oder Datei")
        print("source       Setzt die Datei/Den Ordner der zu kopieren ist fest")
        print("Interval     Sagt aus in welchen Intervallen die Backups erstellt werden sollen")
        print("max backups  Setzt die Maximale Anzahl an Backups fest")
        print("Notiz: Bindestrich vor Argument ist optional, wird aber für Powershell benötigt")

        sys.exit(0)
print('Autofilebackup by Luki')
time.sleep(3)
try:
    system("cls")
except:
    system("clear")
if(len(sys.argv) <= 1) and not(doespathexist("config.cfg")):
    diskspeed = 0
    backuptime = 0
    maxbackups = 0
    source = input("Please input dir or file to be copied: ")
    backuptime = input("please input the time between backups in minutes: ")
    maxbackups = input("Please input the number of Backups (0 for infinity): ")
    diskspeed = input("Please input your Disk speed in MB/sec (If you are not sure imput 5): ")
 #   debug = input("Möchten sie das Programm im Debug-Modus ausführen? (y/n) ")
 #   timedebug = input("Möchten sie den Timer überschreiben (für Debug Zwecke) (y/n) ")
    if not (os.path.isdir(source)) and not (os.path.isfile(source)):
        print("Invalid path")
        time.sleep(10)
        raise ValueError('Invalid path')
    if(int(backuptime) == 0):
        print("Time between backups can not bee 0!")
        time.sleep(10)
        raise ValueError("Time between backups can not be 0!")
    if (int(diskspeed) == 0):
        print("Your disc speed can not bee 0!")
        time.sleep(10)
        raise ValueError("Your disc speed can not be 0!")
    if (int(backuptime) >= 5256000):
        print("Die Zeit zwischen Backups ist höher als 10 Jahre!")
        time.sleep(10)
        raise ValueError("In 10 jahren wird dieses Script kein gültiges Python Script mehr sein!")
    if (int(diskspeed) >= 100000):
        print("Bitte keine Laufwerke aus der Zukunft nutzen! (Laufwerksgeschwindgkeit ist höher als 100000")
        time.sleep(10)
        raise ValueError("Bitte keine Laufwerke aus der Zukunft nutzen!")
    if (os.path.isdir(source)):
        print("Additional time for writing of dir:", ((int(getFolderSize(source, debug) /  1000000) / (int(round(float(diskspeed) * 0.8),0)))), "seconds")
    if (os.path.isfile(source)):
         print("Additional time for writing of file:", ((int(getFileSize(source, debug) /  1000000) / (int(round(float(diskspeed) * 0.8),0)))), "seconds")

    debug = "n"
    timedebug = "n"
if(len(sys.argv) >= 2 and len(sys.argv) <= 6 and (sys.argv[1] == "d" or sys.argv[1] == "f")):
    print("Reading start arguments...")
    if(str(sys.argv[1]) == "d"): dir_or_file = "dir"
    if(str(sys.argv[1]) == "f"): dir_or_file = "file"
    source = str(sys.argv[2]) 
    backuptime = str(sys.argv[3])
    maxbackups = str(sys.argv[4])
    debug = str(sys.argv[5])
    timedebug = str(sys.argv[6])
    print("Argument reading finished")
    print("Arguments:")
    if(str(sys.argv[1]) == "d"): 
        print("Copying an dir")
    if(str(sys.argv[1]) == "f"):
        print("Copying an file")
    print("Source: ", source)
    print("A backup will be reated every ", backuptime, "minutes")
    print(maxbackups, " backups will be created")
    if(str(debug) == "y"):
        print("Debug Informatin will be displayed")
    if(str(debug) == "n"):
        print("No debug Information will be displayed")
    if(str(timedebug) == "y"):
        print("timedebug is set to true")
    if(str(timedebug) == "n"):
        print("Time debug is set to false")
if(len(sys.argv) >= 2 and len(sys.argv) <= 6 and (sys.argv[1] == "-d" or sys.argv[1] == "-f")):
    print("Reading launch arguments...")
    str.lstrip(sys.argv[1])
    str.lstrip(sys.argv[2])
    str.lstrip(sys.argv[3])
    str.lstrip(sys.argv[4])
    str.lstrip(sys.argv[5])
    str.lstrip(sys.argv[6])
    if(str(sys.argv[1]) == "d"): dir_or_file = "dir"
    if(str(sys.argv[1]) == "f"): dir_or_file = "file"
    source = str(sys.argv[2]) 
    backuptime = str(sys.argv[3])
    maxbackups = str(sys.argv[4])
    debug = str(sys.argv[5])
    timedebug = str(sys.argv[6])
    print("Finished reading start arguments")
if(len(sys.argv) >= 2 and len(sys.argv) <= 5 and (sys.argv[1] == "d" or sys.argv[1] == "f")):
    print("Lese Startargumente ein...")
    if(str(sys.argv[1]) == "d"): dir_or_file = "dir"
    if(str(sys.argv[1]) == "f"): dir_or_file = "file"
    source = str(sys.argv[2]) 
    backuptime = str(sys.argv[3])
    maxbackups = str(sys.argv[4])
    print("Einlesen der Startargumente beendet")
    debug = "n"
    timedebug = "n"
if(len(sys.argv) >= 2 and len(sys.argv) <= 5 and (sys.argv[1] == "-d" or sys.argv[1] == "-f")):
    print("Lese Startargumente ein...")
    str.lstrip(sys.argv[1])
    str.lstrip(sys.argv[2])
    str.lstrip(sys.argv[3])
    str.lstrip(sys.argv[4])
    if(str(sys.argv[1]) == "d"): dir_or_file = "dir"
    if(str(sys.argv[1]) == "f"): dir_or_file = "file"
    source = str(sys.argv[2]) 
    backuptime = str(sys.argv[3])
    maxbackups = str(sys.argv[4])
    print("Einlesen der Startargumente beendet")
    debug = "n"
    timedebug = "n"   

if(dir_or_file == "n/a"):
    if os.path.isdir(source):  
        dir_or_file = "dir"  
    if os.path.isfile(source):  
        dir_or_file = "file"
if(dir_or_file == "dir"):
    backupsperday = 1440 / int(backuptime)
    sizeperdaybytes = getFolderSize(source, debug) * backupsperday
    sizeperdaymb = sizeperdaybytes / 1000000
    sizeperdaygb = sizeperdaymb / 1000
    if not(int(maxbackups) <= int(round(backupsperday, 0))) or (int(maxbackups) == int(0)):

        if(sizeperdaymb <= 10000):
            print("Space ussage every day:", int(sizeperdaymb), "MB")
        else:
            print("Space ussage every day:",int(sizeperdaygb), "GB")  
    if(int(maxbackups) <= int(round(backupsperday, 0))) and (int(maxbackups) != int(0)):
        sizeoverallmb = getFolderSize(source, debug) / 1000000 * int(maxbackups)
        if(sizeoverallmb <= 10000):
            print("Space ussage over all:", int(sizeoverallmb),"MB")
        else:
            print("Space ussage over all:",int(sizeoverallmb) / 1000 ,"GB")

else:
    backupsperday = 1440 / int(backuptime)
    filesizeperdaybytes = getFileSize(source, debug) * backupsperday
    filesizeperdaymb = filesizeperdaybytes / 1000000
    filesizeperdaygb = filesizeperdaymb / 1000
    if not(int(maxbackups) >= int(backupsperday)) or (int(maxbackups) == 0):

        if(filesizeperdaymb <= 10000):
            print("Space ussage every day:", int(filesizeperdaymb), "MB")
        else:
            print("Space ussage every day",int(filesizeperdaygb), "GB")  
    if(int(maxbackups) <= int(backupsperday)) and (int(maxbackups) != 0):
        filesizeoverallmb = getFileSize(source, debug) / 1000000
        filesizeoverallmb1 = filesizeoverallmb * int(maxbackups)
        if(filesizeoverallmb <= 10000):
            print("Space ussage over all:", int(filesizeoverallmb) ,"MB")
        else:
            print("Space ussage over all:",int(filesizeoverallmb) / 1000,"GB")


backuptimesec = min2sec(backuptime, debug)

if (debug == "y"):
    print("###############################")
    print("Start Debug 2")
    print(source)
    print(backuptime)
    print(maxbackups)
    print(debug)
    print(backuptimesec)
    if(len(sys.argv) >= 2):
        print("Debug: Start Startargumente")
        print(str(sys.argv[0]))
        print(str(sys.argv[1]))
        print(str(sys.argv[2]))
        print(str(sys.argv[3]))
        print(str(sys.argv[4]))
        print(str(sys.argv[5]))
        print(str(sys.argv[6]))
        print("Debug Ende Startargumente")
    print("end Debug 2")
    print("###############################")
    time.sleep(5)

if(dir_or_file == "file"):
    copyfile(diskspeed, source, maxbackups, backuptimesec, debug, timedebug)
if(dir_or_file == "dir"):
    copydir(diskspeed, source, maxbackups, backuptimesec, debug, timedebug)
if(debug == "y"):
    system("pause")
try:
    system("cls")
except:
    system("clear")
sys.exit(0)



