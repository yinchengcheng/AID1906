#!/usr/bin/python
# -*- coding: utf-8 -*-
# time: 2022/4/9 16:51
#
import socket

# server address
import sys

ADDR = ('172.16.0.111', 8999)


# 客户端文件处理类
class FTPClient:
    def __init__(self, client):
        self.client = client

    def do_list(self):
        self.client.send(b'L')
        data = self.client.recv(128).decode()
        if data == 'OK':
            data = self.client.recv(4096)
            print(data.decode())
        else:
            print(data)

    def do_quit(self):
        self.client.send(b'Q')
        self.client.close()
        sys.exit('谢谢使用！')

    def do_get(self, filename):
        self.client.send(('G ' + filename).encode())
        data = self.client.recv(128).decode()
        if data == 'OK':
            f = open(filename, 'wb')
            while True:
                data = self.client.recv(1024)
                if data == b'##':
                    break
                f.write(data)
            f.close()
        else:
            print(data)



# 连接服务器
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(ADDR)
    except Exception as e:
        print(e)
        return

    # 创建对象
    ftp_client = FTPClient(client)

    while True:
        print('\n===========命令选项============')
        print('*******     list    *********')
        print('*******   get file  *********')
        print('*******   put file  *********')
        print('*******     quit    *********')
        print('=============================')
        cmd = input('>>')
        if cmd.strip() == 'list':
            ftp_client.do_list()
        elif cmd.strip() == 'quit':
            ftp_client.do_quit()
        elif cmd.strip()[:3] == 'get':
            filename = cmd.strip().split(' ')[-1]
            ftp_client.do_get(filename)


if __name__ == '__main__':
    main()
