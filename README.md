# 🩺 IoT-Based Encrypted Blood Pressure Monitoring System

This project simulates an **IoT-based health monitoring system** that collects, encrypts, decrypts, and visualizes real-time patient vitals: **blood pressure**, **glucose levels**, and **heart rate**. The data is encrypted using **Fernet symmetric encryption** to demonstrate a secure transmission model for healthcare IoT systems. The system also simulates secure communication between a client and server, encrypting data with an added hash for integrity.

---

## 👩‍💻 Author

**Aniyah Hall**  
Bachelor of Science in Computer Technology  
**Health Technology & Cybersecurity**  
Bowie State University  
🔐 Undergraduate Researcher, SURI Program  
📧 Email: aniyahhall1231@gmail.com  
🔗 GitHub: [github.com/Aniyah123101](https://github.com/Aniyah123101)

---

## 📌 Project Purpose

Designed as part of a cybersecurity and health technology research initiative, this project explores how encryption can secure sensitive medical data in simulated IoT environments. It mimics real-time patient data generation, encrypts it, verifies decryption accuracy, and visualizes both the data and encryption overhead. The system supports secure communication between a client and server for health data transmission.

---

## 🚀 Features

- 🔐 **End-to-End Data Encryption & Decryption** using Fernet (symmetric encryption)  
- 🧑‍💻 **Simulated IoT Communication**: Client sends encrypted health data to a server, which decrypts and stores the data
- 📊 **Two Visualization Graphs**:  
  - **Original vs. Decrypted data**: Blood Pressure, Glucose, and Heart Rate over time  
  - **Byte Sizes** of Encrypted vs. Unencrypted data  
- 🧪 **User Input Validation**: Accepts and validates user-entered vitals (Blood Pressure, Glucose, Heart Rate)
- ✅ **Decryption Accuracy Check**: Verifies that decrypted data matches the original input
- 🔒 **Data Integrity**: Each transmitted data packet includes a hash for integrity verification
- 🌐 **Socket Communication**: Secure client-server communication with encryption and hash for integrity

---

## 🧠 Technologies Used

- **Python 3**
- [`cryptography`](https://pypi.org/project/cryptography/)
- [`matplotlib`](https://matplotlib.org/)
- `socket` (for client-server communication)
- `random`, `time`, `hashlib` (standard libraries)

---

## 🖥️ How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/YOURUSERNAME/iot-bp-monitor.git
cd iot-bp-monitor

### 2. Install Dependencies
pip install -r requirements.txt

##3. Run the Script
To start the server:
python iot_bp_server.py
To start the client (separate terminal):
python iot_bp_client.py

### 4. Output
Enter your own health values (Blood Pressure, Glucose, Heart Rate) when prompted.
The client sends encrypted data to the server, which decrypts and stores the data.
Graphs will be saved automatically in the same folder:
health_metrics_decrypted_comparison.png: Comparison of original vs. decrypted data
byte_sizes_encrypted_vs_unencrypted.png: Byte size comparison between encrypted and unencrypted data
