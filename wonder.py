#!/usr/bin/python3
"""
Use $ ifconfig to find your port
if ifconfig is not available copy the below code
$ sudo apt-get install net-tools

A port will be like wlp3s0 or eth0
wl  -> represents WIFI
eth -> represents LAN cable

Download This file and set
-> port
-> sudo password
-> upload speed
-> download speed


"""
import os

port = 'wlp3s0' # set your port 
sudoPassword = '3773' # set your password 
upSpeed = '512' # set upload speed Kbps
downSpeed = '1024' # set Download Speed in Kbps


def core( sudoPassword , command , choice):
    os.system ('cd /bin/wondershaper')
    os.system('echo %s|sudo -S %s' % (sudoPassword, command)) 
    if ( choice == 1 or choice == 3):
        print('\nDownload Speed -> ' + downSpeed+ ' Kbps\nUpload Speed -> '+ upSpeed + ' kbps are set');
    elif ( choice == 2):
        print('WonderShaper is Resetted');
    elif ( choice == 4):
        print('Download speed is set to '+ downSpeed + ' kbps');
    elif ( choice == 5):
        print('Upload speed is set to ' + upSpeed + ' kbps');    
            

def modifyBoth() :
    global upSpeed 
    global downSpeed 

    print ( 'Enter Upload Speed : ',end='')
    upSpeed = input().strip()

    print ( 'Enter Download Speed : ',end='')
    downSpeed = input().strip()
    
    core ( sudoPassword , 'wondershaper -ca '+port, 2) 
      
print ( 'Set Download speed alone by using 4')
print ( 'Set Upload speed alone by using 5')        
print ( 'Once set or started always use modify or \nStop the wonder ( by entering 2 ) and set again')
print ( '_________________________________________________________\n')
print ( "Enter choice\n1. Run wondershaper\n2. Stop wondershaper\n3. Modify  \n4. Set Download Speed Only \n5. Set Upload Speed only\n6. Exit \nEnter choice here : ",end='')
choice = int (input())
 
if ( choice == 1):
    command = 'wondershaper -a '+port+' -d '+downSpeed+ ' -u '+upSpeed ;
    print ( 'Starting Wondershaper ...')
elif ( choice == 2):
    command = 'wondershaper -ca '+port ;
    print ( 'Resetting Wondershaper...')
elif ( choice == 3):
    modifyBoth()
    command = 'wondershaper -a '+port+' -d '+downSpeed+ ' -u '+upSpeed ;
elif ( choice == 4):
    print ( 'Enter Download speed in kpbs: ',end='')
    downSpeed = input().strip()
    command = 'wondershaper -a '+port+' -d '+downSpeed ;
elif ( choice == 5):
    print ( 'Enter Upload speed in kpbs: ',end='')
    upSpeed = input().strip()
    command = 'wondershaper -a '+port+' -u '+upSpeed ;    
else:
    print ( 'Process terminated')
    exit(0) ;    

     
core ( sudoPassword , command , choice) 
