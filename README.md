# 🩺 IoT-Based Encrypted Blood Pressure Monitoring System

This project simulates an **IoT-based health monitoring system** that collects, encrypts, decrypts, and visualizes real-time patient vitals: **blood pressure**, **glucose levels**, and **heart rate**. The data is encrypted using **Fernet symmetric encryption** to demonstrate a secure transmission model for healthcare IoT systems.

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

Designed as part of a cybersecurity and health technology research initiative, this project explores how encryption can secure sensitive medical data in simulated IoT environments. It mimics real-time patient data generation, encrypts it, verifies decryption accuracy, and visualizes both the data and encryption overhead.

---

## 🚀 Features

- 🔐 **End-to-End Data Encryption & Decryption** using Fernet (symmetric encryption)
- 📊 **Two Visualization Graphs**:
  - Original vs. Decrypted data (Blood Pressure, Glucose, Heart Rate)
  - Byte sizes of Encrypted vs. Unencrypted values
- 🧪 **User Input Validation**: Accepts and validates user-entered vitals
- ✅ **Decryption Accuracy Check**: Ensures decrypted data matches the original

---

## 🧠 Technologies Used

- **Python 3**
- [`cryptography`](https://pypi.org/project/cryptography/)
- [`matplotlib`](https://matplotlib.org/)
- `random`, `time` (standard libraries)

---

## 🖥️ How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/YOURUSERNAME/iot-bp-monitor.git
cd iot-bp-monitor

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the Script
python iot_bp_encryption_monitor.py

### 4. Output
Enter your own health values when prompted.
Graphs will be saved automatically in the same folder:
health_metrics_decrypted_comparison.png
byte_sizes_encrypted_vs_unencrypted.png
