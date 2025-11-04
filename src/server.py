import socket

def server():
    # 创建socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(("", 65501))
    server_socket.listen(1)
    server_client_socket, client_prot = server_socket.accept()
    while True:
        
        recv_data = server_client_socket.recv(1024)
        recv_content = recv_data.decode("gbk")
        if len(recv_content) > 0:
            print(recv_content)
            if recv_content == 'q':
                break
            recv_content = "已收到：" + recv_content
            recv_content = recv_content.encode('gbk')
        server_client_socket.send(recv_content)
    
    server_client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    print("server start...")
    server()
