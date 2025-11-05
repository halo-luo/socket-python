import socket
import threading
from src.client import client


def client_thread():
    client()


if __name__ == "__main__":
    print("client_thread running...")
    client_thread()
