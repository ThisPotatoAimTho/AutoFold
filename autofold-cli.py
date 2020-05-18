import psutil
import subprocess
import configparser
import time

fileList = []
config = configparser.ConfigParser()
config.read('config.ini')
foldingClientPath = config['FAH']['Path']
waitTime = config['autofold']['WaitTime']
print(foldingClientPath)

with open('filelist.txt', 'r') as filehandle:
    filecontents = filehandle.readlines()
    for line in filecontents:
        current_file = line[:-1]
        
        fileList.append(current_file)

        
while True:
    taskList = psutil.pids()
    paused = False
    for i in taskList:
        try:
            p = psutil.Process(i)
            if p.name() in fileList:
                print(p.name(), "is running. Pausing FoldingAtHome.")
                subprocess.run(foldingClientPath + " --send-pause")
                paused = True
        except psutil.NoSuchProcess:
            print("Process does not exist.")

    if paused == False:
        print("Specified programs are not running. Unpausing FoldingAtHome.")
        subprocess.run(foldingClientPath + " --send-unpause")

    time.sleep(int(waitTime))

            
        
    
    
    

