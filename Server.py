import socket
import threading
from cryptography.fernet import Fernet
import matplotlib.pyplot as plt
import matplotlib
import signal
import sys

# Set matplotlib backend to 'Agg' to save plots without GUI
matplotlib.use('Agg')

HOST = "127.0.0.1"
PORT = 65432
key = b"s9W1zlasKugykJvxaJvvkaAwVOz-hDbxoTkhSyz1k64="
cipher_suite = Fernet(key)

threads = []  # Keep track of client threads

# Lists to store decrypted values for each metric
decrypted_bp = []
decrypted_glucose = []
decrypted_hr = []

def decrypt_data(data):
    """Decrypt the received data."""
    return cipher_suite.decrypt(data).decode()

def handle_client(conn, addr):
    """Handle a single client connection."""
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data or data == b"TERMINATE":
                print(f"Client {addr} disconnected.")
                break
            try:
                # Decrypt the received data
                decrypted_message = decrypt_data(data)
                print(f"Received (encrypted): {data}")
                print(f"Decrypted data: {decrypted_message}")

                # Separate actual data from the hash
                actual_data, _ = decrypted_message.rsplit("|", 1)

                # Parse the numeric values
                data_parts = actual_data.split(", ")
                bp_value = int(data_parts[0].split(": ")[1])
                glucose_value = int(data_parts[1].split(": ")[1])
                hr_value = int(data_parts[2].split(": ")[1])

                # Append decrypted values
                decrypted_bp.append(bp_value)
                decrypted_glucose.append(glucose_value)
                decrypted_hr.append(hr_value)

            except Exception as e:
                print(f"Error processing data from {addr}: {e}")

    # Generate the plots after client disconnects
    generate_plots()

def generate_plots():
    """Generate both the encrypted vs decrypted data sizes plot and the received IoT healthcare data plot."""
    time_axis = list(range(len(decrypted_bp)))

    # Calculate total sizes for encrypted and decrypted data
    encrypted_sizes = [len(cipher_suite.encrypt(f"BP: {bp}, Glucose: {glucose}, Heart Rate: {hr}".encode()))
                       for bp, glucose, hr in zip(decrypted_bp, decrypted_glucose, decrypted_hr)]
    decrypted_sizes = [len(f"BP: {bp}, Glucose: {glucose}, Heart Rate: {hr}".encode())
                       for bp, glucose, hr in zip(decrypted_bp, decrypted_glucose, decrypted_hr)]

    # Plot 1: Encrypted vs Decrypted Data Sizes
    plt.figure(figsize=(12, 6))
    plt.plot(time_axis, encrypted_sizes, label="Encrypted Data Size (bytes)", linestyle="--", color="blue")
    plt.plot(time_axis, decrypted_sizes, label="Decrypted Data Size (bytes)", color="orange")
    plt.xlabel("Time (s)")
    plt.ylabel("Size (bytes)")
    plt.title("Encrypted vs Decrypted Data Sizes Over Time")
    plt.legend()
    plt.grid(True)
    plt.savefig("encrypted_vs_decrypted_data_sizes.png")
    print("Saved plot as 'encrypted_vs_decrypted_data_sizes.png'.")

    # Plot 2: Received IoT Healthcare Data
    plt.figure(figsize=(12, 6))
    plt.plot(time_axis, decrypted_bp, label="Blood Pressure", linestyle="--", color="blue")
    plt.plot(time_axis, decrypted_glucose, label="Glucose", color="orange")
    plt.plot(time_axis, decrypted_hr, label="Heart Rate", color="green")
    plt.xlabel("Time (s)")
    plt.ylabel("Measurement")
    plt.title("Received IoT Healthcare Data Over Time")
    plt.legend()
    plt.grid(True)
    plt.savefig("received_health_metrics_over_time.png")
    print("Saved plot as 'received_health_metrics_over_time.png'.")

def signal_handler(sig, frame):
    """Handle server shutdown gracefully."""
    print("\nServer shutting down gracefully...")
    for t in threads:
        t.join()  # Wait for all threads to finish
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        threads.append(client_thread)
        client_thread.start()
