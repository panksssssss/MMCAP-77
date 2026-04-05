# ☁️ Cloud Storage Growth Dashboard

An interactive **Streamlit web application** to simulate and predict corporate cloud storage usage using a hybrid **Exponential + Logistic Growth Model**.

---

## 🔗 Live Demo

👉 https://mmca-project-69-bkqyvbaycssvnxaxcpybbe.streamlit.app/

---

## 📌 Project Overview

Managing cloud storage efficiently is critical for modern organizations. This project helps visualize and forecast storage growth while providing **early expansion alerts**.

It combines:

* ⚡ **Exponential Growth** (rapid data increase)
* 📉 **Logistic Growth** (capacity constraints)

to produce a **realistic storage prediction model**.

---

## 🚀 Features

* 📊 Interactive dashboard with real-time updates
* 🎛️ User-controlled parameters via sidebar
* 📈 Dynamic Plotly charts
* 📦 Key metrics (storage, growth, duration)
* ⚠️ Automatic alert when storage reaches **80% capacity**
* 🧠 Hybrid mathematical model for accurate forecasting

---

## 🧮 Mathematical Model

### Exponential Growth

```
S_exp = S0 * e^(r * t)
```

### Logistic Growth

```
S_log = S_max / (1 + e^(-r * (t - T/2)))
```

### Combined Model

```
S_combined = min(S_exp + daily_upload * t, S_log)
```

---

## 🖥️ Tech Stack

* **Python**
* **Streamlit**
* **NumPy**
* **Plotly**

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/cloud-storage-growth-dashboard.git
cd cloud-storage-growth-dashboard
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

---

## 📥 Input Parameters

| Parameter             | Description         |
| --------------------- | ------------------- |
| Initial Storage (GB)  | Starting storage    |
| Maximum Capacity (GB) | Storage limit       |
| Growth Rate           | Rate of increase    |
| Time (Days)           | Simulation duration |
| Daily Upload (GB/day) | Daily data addition |

---

## 📊 Output

* 📈 Growth curves (Exponential, Logistic, Combined)
* 📦 Final storage usage
* ⚠️ Expansion alert when nearing capacity

---

## 📈 Use Cases

* Cloud storage planning
* Capacity forecasting
* IT infrastructure optimization
* Data growth analysis

---

## 📂 Project Structure

```
📁 cloud-storage-growth-dashboard
│-- app.py
│-- requirements.txt
│-- README.md
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Pankaj Sharma**

---

## ⭐ Support

If you found this useful, please ⭐ star the repository!
