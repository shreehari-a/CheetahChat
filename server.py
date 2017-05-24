import socket
from threading import Thread
import time


users = {}
def broadcast(name, message):
    print name 
    print message
    for to_name, conn in users.items():
        if to_name != name:
            print "broadcasting"
            print users.values()
            try:
                conn.send(name + ' >' +message + '\n')
            except socket.error:
                pass

def privatechat(name ,message, to_name):
    print name 
    print message
    print to_name
    for toname, conn in users.items():
        if ' '+toname == to_name:
            try:
                conn.send('(secret message)'+name + ' >' + message + '\n')
            except socket.error:
                pass

def handle_a_socket(cn, addr,tcount):
    
    #non blocking socket 
    cn.setblocking(0)

    #assign client with a name
    name = "Client-%s"%(len(users)+1)
    cn.send("You are %s"%name)

    #add username and connection to dictionary
    users[name] = cn
    print users

    #initialise command
    command = ""
    while True:
        #recieve data for the particular connection
        try:
            #recieve user command     
            command = cn.recv(1024).strip()
           
            #process command to identify pc or bc
            command_list = command.split('"') 
            print
            print 
            print
            #if data is to be "bc" 
            if command_list[0] == "bc ":
                print "this is broadcast message"
                broadcast(name,command_list[1])
             
            elif command_list[0] == "pc " and command_list[2]:
                print "this is to be sent to user"
                privatechat(name,command_list[1],command_list[2])
            
            elif data == "exit":
                print "connection closed"
                #cn.close()
                #broadcast(user_left)
            else:
                print "usage error"
            if command:
                print "[", tcount, "]", addr, command
                command = None
        except:
            pass


def server():
    #initialise socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #request for the text of page
    host = socket.gethostname()
    port = 6000
    server.bind((host,port))
    server.listen(5)
    thread_count = 0

    print 'listening'
    
    conn = None
    addr = None

    while True:
        # Accept new connection.
        try:
            conn, addr = server.accept()
            if conn and addr:
                thread_count += 1
                t = Thread(target=handle_a_socket, args=(conn, addr,thread_count))
                t.start()


        except socket.error:
            continue

server()
