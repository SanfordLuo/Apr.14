import socket

def show_menu():
    print("="*20)
    print("1.发送数据")
    print("2.接收数据")
    print("3.退出聊天")
    print("="*20)
    return int(input("请选择："))

def send_func(object):
    send_ip = input("请输入目标ip:")
    send_port = int(input("请输入目标端口:"))
    send_addr = (send_ip, send_port)
    send_data = input("请输入要发送的数据：").encode("utf-8")
    object.sendto(send_data, send_addr)

def recv_func(object):
    recv_byte_data, recv_addr = object.recvfrom(1024)
    recv_data = recv_byte_data.decode("gbk")
    print("ip:%s\n端口:%s\n数据；%s" % (recv_addr[0], recv_addr[1], recv_data))

def run():
    my_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    my_port = int(input("请输入要绑定的本地端口号："))
    my_udp_socket.bind(("", my_port))

    while True:
        num = show_menu()
        if num == 1:
            send_func(my_udp_socket)
        elif num == 2:
            recv_func(my_udp_socket)
        elif num == 3:
            print("已退出聊天！")
            break
        else:
            print("您输入有误，请重新输入！")
    my_udp_socket.close()

if __name__ == '__main__':
    run()