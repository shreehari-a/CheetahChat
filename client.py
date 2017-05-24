import socket               
import sys
import select
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()  
port =  6000  

s.connect((host, port))

print 'Connected to remote server'
def client():
    # create socket
    data = s.recv(1024).strip()
    sys.stdout.write(data + '\n')
    sys.stdin.flush()
    print 'Usage : bc "<your message" \n or pc "<your message>" <recipient name>'

    sys.stdout.write("Me >")
    sys.stdout.flush()
    t1 = Thread(target=send_data,args=())
    t1.start()
    t2 = Thread(target=recieve_data,args=())
    t2.start()

def send_data():
    while True:
        data = sys.stdin.readline()
        if data:
            sys.stdout.write("Me >")
            sys.stdout.flush()
            s.send(data)

def recieve_data():
    while True:
        data = s.recv(1024).strip()
        if data:
            sys.stdout.write('\r'+ data + '\nMe >')  
            sys.stdout.flush()

client()

