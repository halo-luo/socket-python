import socket
import threading
import sys

sys.path.append('..')
from src.client import client


def client_thread():
    try:
        client()
    except ConnectionAbortedError:
        print("已与服务器断开连接")


if __name__ == "__main__":
    print("client_thread running...")
    client_thread()
