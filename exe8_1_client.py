#! usr/bin/python3
# __authour__: Littlerubbish

import socket

def main():
    HOST = '127.0.0.1'
    PORT = 65433

    print(f"Creating a client to play with HOST:{HOST}, port:{PORT}.........")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect( (HOST, PORT) )
    print("Socket with server is connected!")

    name = input("Please type in your name: ")
    msg = f"Hello,  I am {name}"

    while True:
        s.send(msg.encode("UTF-8"))

        data = s.recv(1024)

        print("Received from the server:", str(data.decode('UTF-8')))

        ans = input("\ndo you want to continue(y/n): ")
        if ans == 'y':
            continue
        else:
            break

    s.close()



if __name__ == "__main__":
    main()