import socket
import threading

def recv_msg(udp_socket):
    while True:
        recv_data, recv_addr = udp_socket.recv(1024)
        print("recv_data:%s" % recv_data.decode("gbk"))


def send_msg(udp_socket):
    while True:
        send_ip = input("请输入目标IP：")
        send_port = int(input("请输入目标端口："))
        send_addr = (send_ip, send_port)
        send_data = input("请输入要发送的数据：")
        udp_socket.sendto(send_data.encode("utf-8"), send_addr)

if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.bind(("", 7878))

    # 创建一个线程负责接收数据
    recv_thread = threading.Thread(target=recv_msg, args=(udp_socket,))
    recv_thread.start()
    # 创建一个线程负责发送数据
    send_thread = threading.Thread(target=send_msg, args=(udp_socket,))
    send_thread.start()
