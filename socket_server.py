# -*- coding: utf-8 -*-

import socket

server_ip = "localhost"
server_port = 20002

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
s.bind((server_ip,server_port)) ## ************ ##
# become a server socket
s.listen(5)

while True:
    # accept connections from outside
    (conn, address) = s.accept()
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    from_client = 0
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client = data
        print(from_client)
        # conn.send("I am SERVER")
        resp_para_superv = b"(request \n \
               :sender  ( agent-identifier :name spb@Microrede-UFJF:1099 ) \n \
                   :RECEIVER  (SET ( agent-identifier :name MF_Vn@Microrede-UFJF:1099 ) ) \n \
                       :content '23/08/2022_10:41:48.40600,4118,20000,0,0,4118,20000,0,0,4118,20000,0,0,4118,20000,0,0'  )\r\n"
        conn.sendall(resp_para_superv)

conn.close()
print('client disconnected')
    
    