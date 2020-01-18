#! usr/bin/python3
# __authour__: Littlerubbish

import socket
from _thread import *
import threading

print_lock = threading.Lock()

#thread function
def threaded(c):
    while True:

        data = (c.recv(1024)).decode("UTF-8")
        print("Data form the client is:", data)

        if not data:
            print("Bye")

            #lock released on exit
            # print_lock.release()
            break
    
        # reverse the string received from the client
        data = data[::-1]

        # send back information to the client
        c.send(data.encode("UTF-8"))
    
    # connection closed
    c.close()

def main():
    #define host and port number, then create the socket
    HOST = '127.0.0.1'
    PORT = 65433
    print(f"Creating a server with HOST:{HOST}, port:{PORT}.........")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket is created successfully!")

    # bind port on localhost
    s.bind( (HOST, PORT) )
    print("Socket binded to port:", PORT)

    # put the socket into listening mode
    s.listen(5)
    print("Socket is listening......")

    while True:
        # establish connection from a client
        c, addr = s.accept()    # return sock, addr

        # lock acquired by client
        # print_lock.acquire()
        print("connected to:", addr[0], ":", addr[1])

        #start a new thread and return its identifier
        thread_id = start_new_thread(threaded, (c, ))
        print("Created a new thread, identifier is: ", thread_id)

    s.close()


if __name__ == "__main__":
    main()