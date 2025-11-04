import socket
import threading


def handle_thread_server(server_client_socket, shutdown_event):
    while True:
        recv_data = server_client_socket.recv(1024)
        recv_content = recv_data.decode('gbk')
        print(f"{recv_content}")
        if len(recv_content) == 0:
            break

        if recv_content == 'shutdown' or recv_content == 'poweroff':
            shutdown_event.set()
            server_client_socket.send("服务器即将关闭".encode('gbk'))
            break

        recv_content = "收到：" + recv_content
        recv_content = recv_content.encode('gbk')
        server_client_socket.send(recv_content)


        
    server_client_socket.close()

def server_thread():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(("0.0.0.0", 65500))
    server_socket.listen(64)
    global shutdown_event
    shutdown_event = threading.Event()

    while not shutdown_event.is_set():

        server_client_socket, client_port = server_socket.accept()
        print(f"客户端连接成功{client_port}")
        
        thread_server = threading.Thread(
            target=handle_thread_server,
            args=(server_client_socket, shutdown_event))
        thread_server.daemon = True
        thread_server.start()

    server_client_socket.close()



if __name__ == "__main__":
    print("server_thread running...")
    server_thread()
