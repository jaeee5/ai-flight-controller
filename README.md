# 🛸 AI-Powered Flight Controller

An experimental project exploring **autonomous flight control** and **AI-based navigation** for drones using simulation environments.

## 🚀 Overview
This system simulates a drone flight controller capable of:
- Maintaining stable flight via PID control
- Detecting and avoiding obstacles with AI (OpenCV + YOLO)
- Navigating via path planning (A*)
- Streaming telemetry to a live dashboard
- Logging and analyzing flight performance

The project combines **AI, robotics, and flight control engineering** into a modular system you can test and extend.

---

## 🧠 Tech Stack
- **Python 3.10+**
- **PyTorch / OpenCV** for AI & computer vision
- **Flask / Chart.js** for dashboard visualization
- **PX4 SITL** or **Microsoft AirSim** for simulation
- **Matplotlib / NumPy / Pandas** for analytics

---

## ⚙️ Setup
```bash
git clone https://github.com/<your-username>/ai-flight-controller.git
cd ai-flight-controller
pip install -r requirements.txt
```
Then run:
```bash
python main.py
```
