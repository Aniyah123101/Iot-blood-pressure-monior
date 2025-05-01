import time
import random
import matplotlib.pyplot as plt
from cryptography.fernet import Fernet
import matplotlib

# Set matplotlib backend to 'Agg' to avoid GUI issues and save plots as files
matplotlib.use('Agg')

# Function to generate IoT healthcare data
def generate_data(duration=120):
    blood_pressure = [random.randint(70, 150) for _ in range(duration)]
    glucose = [random.randint(80, 180) for _ in range(duration)]
    heart_rate = [random.randint(60, 100) for _ in range(duration)]
    print("Generated data for blood pressure, glucose, and heart rate.")
    return blood_pressure, glucose, heart_rate

# Function to encrypt data using Fernet
def encrypt_data(data, cipher_suite):
    encrypted_data = [cipher_suite.encrypt(str(d).encode()) for d in data]
    print("Data encryption complete.")
    return encrypted_data

# Function to decrypt data using Fernet
def decrypt_data(encrypted_data, cipher_suite):
    decrypted_data = [int(cipher_suite.decrypt(d).decode()) for d in encrypted_data]
    print("Data decryption complete.")
    return decrypted_data

# Generate data and encryption key
blood_pressure, glucose, heart_rate = generate_data()
key = Fernet.generate_key()
cipher_suite = Fernet(key)
print("Encryption key generated.")

# Encrypt the data
encrypted_blood_pressure = encrypt_data(blood_pressure, cipher_suite)
encrypted_glucose = encrypt_data(glucose, cipher_suite)
encrypted_heart_rate = encrypt_data(heart_rate, cipher_suite)

# Decrypt the data
decrypted_blood_pressure = decrypt_data(encrypted_blood_pressure, cipher_suite)
decrypted_glucose = decrypt_data(encrypted_glucose, cipher_suite)
decrypted_heart_rate = decrypt_data(encrypted_heart_rate, cipher_suite)

# Verify if decrypted data matches the original data
assert blood_pressure == decrypted_blood_pressure, "Blood Pressure decryption failed!"
assert glucose == decrypted_glucose, "Glucose decryption failed!"
assert heart_rate == decrypted_heart_rate, "Heart Rate decryption failed!"
print("Decryption verification successful. Decrypted data matches original data.")

# Ask user for input and validate
try:
    user_bp = int(input("Enter a blood pressure value (70-150): "))
    if 70 <= user_bp <= 150:
        print(f"The entered blood pressure value {user_bp} is within the valid range.")
    else:
        print(f"The entered blood pressure value {user_bp} is outside the valid range.")

    user_glucose = int(input("Enter a glucose value (80-180): "))
    if 80 <= user_glucose <= 180:
        print(f"The entered glucose value {user_glucose} is within the valid range.")
    else:
        print(f"The entered glucose value {user_glucose} is outside the valid range.")

    user_hr = int(input("Enter a heart rate value (60-100): "))
    if 60 <= user_hr <= 100:
        print(f"The entered heart rate value {user_hr} is within the valid range.")
    else:
        print(f"The entered heart rate value {user_hr} is outside the valid range.")
except ValueError:
    print("Invalid input. Please enter numeric values.")

# Plot health metrics over time
plt.figure(figsize=(10, 5))
time_axis = list(range(120))
plt.plot(time_axis, blood_pressure, label="Blood Pressure (Original)", linestyle="--")
plt.plot(time_axis, decrypted_blood_pressure, label="Blood Pressure (Decrypted)")
plt.plot(time_axis, glucose, label="Glucose (Original)", linestyle="--")
plt.plot(time_axis, decrypted_glucose, label="Glucose (Decrypted)")
plt.plot(time_axis, heart_rate, label="Heart Rate (Original)", linestyle="--")
plt.plot(time_axis, decrypted_heart_rate, label="Heart Rate (Decrypted)")
plt.xlabel("Time (s)")
plt.ylabel("Measurement")
plt.title("Simulated IoT Healthcare Data (Original vs Decrypted)")
plt.legend()
plt.grid(True)
plt.savefig("health_metrics_decrypted_comparison.png")
print("Saved plot as 'health_metrics_decrypted_comparison.png'.")

# Plot byte sizes for encrypted and unencrypted data
plt.figure(figsize=(10, 5))
unencrypted_bp_byte_sizes = [len(str(bp).encode()) for bp in blood_pressure]
encrypted_bp_byte_sizes = [len(bp) for bp in encrypted_blood_pressure]
unencrypted_glucose_byte_sizes = [len(str(gl).encode()) for gl in glucose]
encrypted_glucose_byte_sizes = [len(gl) for gl in encrypted_glucose]
unencrypted_hr_byte_sizes = [len(str(hr).encode()) for hr in heart_rate]
encrypted_hr_byte_sizes = [len(hr) for hr in encrypted_heart_rate]

plt.plot(time_axis, unencrypted_bp_byte_sizes, label="Unencrypted BP Data Size", linestyle="--")
plt.plot(time_axis, encrypted_bp_byte_sizes, label="Encrypted BP Data Size")
plt.plot(time_axis, unencrypted_glucose_byte_sizes, label="Unencrypted Glucose Data Size", linestyle="--")
plt.plot(time_axis, encrypted_glucose_byte_sizes, label="Encrypted Glucose Data Size")
plt.plot(time_axis, unencrypted_hr_byte_sizes, label="Unencrypted Heart Rate Data Size", linestyle="--")
plt.plot(time_axis, encrypted_hr_byte_sizes, label="Encrypted Heart Rate Data Size")
plt.xlabel("Time (s)")
plt.ylabel("Byte Size")
plt.title("Byte Sizes for Health Data (Encrypted vs. Unencrypted)")
plt.legend()
plt.grid(True)
plt.savefig("byte_sizes_encrypted_vs_unencrypted.png")
print("Saved plot as 'byte_sizes_encrypted_vs_unencrypted.png'.")

print("Plotting complete. Images saved as .png files.")
