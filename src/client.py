import socket

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 65501))
    while True:    
        ipt = input()
        if len(ipt) > 0:
            
            send_data = ipt.encode('gbk')
            client_socket.send(send_data)

            # 更换为shutdown关闭服务器
            if ipt == "shutdown":
                break

            recv_data = client_socket.recv(1024)
            recv_content = recv_data.decode('gbk')
            print("客户端接收数据为：", recv_content)
    client_socket.close()


if __name__ == "__main__":
    print("client start...")
    client()
