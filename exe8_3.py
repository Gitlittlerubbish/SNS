#! usr/bin/python3
# __author__ == "Littlerubbish"

import socket

def get_data(URL):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if s:
        s.connect( (URL, 80) )
        s.sendall(bytes(f"GET / HTTP/1.1\r\nHost: {URL}\r\nConnection: close\r\n\r\n", "UTF-8"))
        
        data = s.recv(4096 * 16)
        print(data.decode())
        throughput = len(str(data, "UTF-8"))

        rt_list = [data, throughput]
    s.close()

    return rt_list

def main():
    URL = "www.example.com"

    rt_list = get_data(URL)

    print(f"Throughout is:{rt_list[1]}")

if __name__ == "__main__":
    main()