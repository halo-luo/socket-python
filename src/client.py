import socket


def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 65500))
    # client_socket.connect(('192.168.1.16', 65500))
    while True:
        ipt = input()
        if len(ipt) > 0:

            send_data = ipt.encode('gbk')
            client_socket.send(send_data)

            recv_data = client_socket.recv(1024)
            recv_content = recv_data.decode('gbk')
            print("客户端接收数据为：", recv_content)

            # 输入q关闭客户端
            if ipt == "q":
                break

    client_socket.close()


if __name__ == "__main__":
    print("client start...")
    client()
