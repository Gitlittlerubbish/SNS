#! usr/bin/python3

import socket
import sys


def main():
    HOST = ''
    PORT = 8888

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Udp socket created.")
    except socket.error as msg:
        print("Failed to create a udp socket. Error code:", str(msg[0]), ". Message", msg[1])
        sys.exit()

    try:    
        s.bind( (HOST, PORT) )
    except socket.error as msg:
        print("Bind failed, Error Code:", str(msg[0]), "Message:", msg[1])

    print("Socket bind complete.")

    while True:
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        data = d[0]
        addr = d[1]

        if not data:
            break
        reply = "OK..." + str(data, encoding="UTF-8")
        # reply 
        s.sendto(bytes(reply, encoding="UTF-8"), addr)
        
        print("Message[", addr[0], ":", str(addr[1]) + "] - ", str(data.strip(), "UTF-8"))
    
    s.close()

    

if __name__ == "__main__":
    main()