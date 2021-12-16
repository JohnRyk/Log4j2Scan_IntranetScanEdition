#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, threading
  
def recv_msg(udp_socket):
    """接收数据并显示"""
    while True:
        # 1. 接收数据
        recv_msg = udp_socket.recvfrom(1024)
        # 2. 解码
        recv_ip = recv_msg[1]
        #recv_msg = recv_msg[0].decode("gbk")#.decode("utf-8")  #注意这里的编码如果是windows选择gbk,linux选择utf-8
#        recv_msg = recv_msg[0].decode("utf-8")
        recv_msg = recv_msg[0].decode("latin-1")
        #recv_msg = recv_msg[0]
        # 3. 显示接收到的数据
        msg = ">>>%s:/%s" % (str(recv_ip), recv_msg)
        with open('log','a') as f:
            f.write(msg)
            f.write("\n")
        print(msg)
  
def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定本地信息
    udp_socket.bind(("172.17.0.1", 53))
 
    # 3. 创建一个子线程用来接收数据
    t = threading.Thread(target=recv_msg, args=(udp_socket,))
    t.start()
 
if __name__ == "__main__":
    main()
