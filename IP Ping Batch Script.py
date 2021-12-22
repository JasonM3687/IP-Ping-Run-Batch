# IP pinging batch running script
import subprocess
import time
import os

while 1:
    #Gets script starting time
    start_time = time.time()
    
    #Runs the 6 batch files, input format C:\Destination\batch_file.bat (keep the r before the start of the string)
    subprocess.call([r'C:\Users\Jason Matuszak\Desktop\bat1.bat'])
    subprocess.call([r'C:\Users\Jason Matuszak\Desktop\bat2.bat'])
    subprocess.call([r'C:\Users\Jason Matuszak\Desktop\bat3.bat'])
    subprocess.call([r'C:\Users\Jason Matuszak\Desktop\bat4.bat'])
    subprocess.call([r'C:\Users\Jason Matuszak\Desktop\bat5.bat'])
    subprocess.call([r'C:\Users\Jason Matuszak\Desktop\bat6.bat'])

    #IP address of the computer you want to ping
    ip_addr = '192.168.1.1'
    #Sending ping command out to cmd
    stream = os.popen('ping ' + ip_addr)
    #Reading/storing cmd output 
    output = stream.read()
    
    #Re-running scripts or sleeping based on ping status
    if 'Destination host unreachable' in output:
        print('IP unreachable...Time to sleep')
        #Sleeps for an hour (in seconds)
        time.sleep(3600)
    elif 'Destination host unreachable' not in output:
        print("IP reachable, re-running scripts")

    #Gets script ending time
    end_time = time.time()
    #Calculates and outputs scripts total execution time
    print("Total time elapsed: " + str(end_time-start_time) + " Seconds.")

    
    
