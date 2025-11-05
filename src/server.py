import socket


def server():
    # 创建socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(("0.0.0.0", 65500))
    server_socket.listen(1)
    server_client_socket, client_port = server_socket.accept()
    print(f"客户端连接成功{client_port}")
    while True:

        recv_data = server_client_socket.recv(1024)
        recv_content = recv_data.decode("gbk")
        if len(recv_content) > 0:
            print(recv_content)

            # 客户端输入shutdown 和 poweroff关闭服务器
            if recv_content == "shutdown" or recv_content == "poweroff":
                break

            recv_content = "已收到：" + recv_content
            recv_content = recv_content.encode('gbk')
        server_client_socket.send(recv_content)

    server_client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    print("server start...")
    server()
