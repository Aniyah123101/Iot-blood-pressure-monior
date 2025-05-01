import socket
import random
import time
from cryptography.fernet import Fernet
import hashlib

# Client setup
HOST = "127.0.0.1"
PORT = 65432
key = b"s9W1zlasKugykJvxaJvvkaAwVOz-hDbxoTkhSyz1k64="
cipher_suite = Fernet(key)

def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

def add_hash(data):
    hash_obj = hashlib.sha256(data.encode())
    return f"{data}|{hash_obj.hexdigest()}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    try:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        while True:
            # Simulate sending random health data
            blood_pressure = random.randint(70, 150)
            glucose = random.randint(80, 180)
            heart_rate = random.randint(60, 100)
            data_to_send = f"BP: {blood_pressure}, Glucose: {glucose}, Heart Rate: {heart_rate}"

            # Add a hash for integrity and encrypt the data
            data_with_hash = add_hash(data_to_send)
            encrypted_data = encrypt_data(data_with_hash)

            # Send encrypted data
            print(f"Sending (encrypted): {encrypted_data}")
            client_socket.sendall(encrypted_data)

            time.sleep(5)

    except KeyboardInterrupt:
        print("Terminating connection due to KeyboardInterrupt.")
        client_socket.sendall(b"TERMINATE")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Client socket closed.")
