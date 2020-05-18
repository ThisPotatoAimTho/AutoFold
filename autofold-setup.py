import configparser
import os
import sys

config = configparser.ConfigParser()

print("AutoFold setup")
fahPath = input("Enter in path of FAHClient.exe or type in \"default\" if you dont know : ")

if fahPath == "default":
    config['FAH'] = {'Path': "C:\Program Files (x86)\FAHClient\FAHClient.exe"}
else:
    config['FAH'] = {'Path' : fahPath}

waitTime = input("Enter in wait time interval for checking for programs in seconds (recommend 10-30) : ")

config['autofold'] = {'waitTime' : int(waitTime)}
with open('config.ini', 'w') as configFile:
    config.write(configFile)

print("Type in add and then program name with exe to add to program list. eg \"add RobloxPlayerBeta.exe\". Type in \"del\" to delete entire list. Type in \"exit\" to exit setup.")

while True:
    cmd = input("> ")
    if cmd.split()[0] == "add":
        with open("filelist.txt", "a") as filehandle:
            filehandle.write("%s\n" % cmd.split()[1])
    elif cmd.split()[0] == "del":
        confirm = input("Are you sure you want to delete the entire list? ")
        if confirm == "yes" or confirm == "Yes" or confirm == "y" or confirm == "Y":
            os.remove("filelist.txt")
    elif cmd.split()[0] == "exit":
        sys.exit()
    elif cmd.split()[0] == "help":
        print("Type in add and then program name with exe to add to program list. eg \"add RobloxPlayerBeta.exe\". Type in \"del\" to delete entire list. Type in \"exit\" to exit setup.")
    else:
        print("Command does not exist.")
    
            
