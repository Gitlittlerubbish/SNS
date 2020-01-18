#! usr/bin/python3
# __author__ = "Littlerubbish"

import socket
import sys

HOST = ''
PORT = 8888

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Socket created")
    except socket.error as msg:
        print("Failed to create socket")
        sys.exit()

    while True:
        msg = input("Enter the message to send to server:")
        # print(type(msg))
        try:
            # set the whole string
            s.sendto(bytes(msg, "UTF-8"), (HOST, PORT))

            # receive data from server
            d = s.recvfrom(1024)
            reply = d[0]

            print("Server reply:", str(reply, "UTF-8"))

        except socket.error as msg:
            print("Error Code:", str(msg[0]), "Message", str(msg[1]))
            sys.exit()
        
    s.close()

if __name__ == "__main__":
    main()