Architecture of client-server chat system
=========================================


    client  client  client  client

client          server          client

    client  client  client  client


1 server
n clients

1. Server is listening using socket s
2. Client1 connects to s through socket c1
3. Client2 connects to s through socket c2
4. Client3 connects to s through socket c3


i.e where is this: q = [c1, c2, c3]?
Once you get q = [c1, c2, c3]
Loop through it one by one
Each iteration, create a new thread, pass it cn, and pop cn
Continue until q is empty

iteration(cn):
    check if broadcast/unicast
    if broadcast
        handle it
    else
        handle it
