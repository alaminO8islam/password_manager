# 🔐 AI-Powered Password Manager

A secure, smart, and minimal **Password Manager** built using **Python, Flask, and Cryptography**. This web app allows users to safely store, retrieve, and manage passwords using encryption and hashing.

---

## 🚀 Key Features

* **User Authentication** – Master password required to unlock vault.
* **AES Encryption** – All saved passwords are encrypted securely.
* **Password Hashing** – Master password is hashed using bcrypt.
* **Add, View, Delete Entries** – Manage credentials with ease.
* **Web-Based UI** – Built with Flask and HTML (Bootstrap-ready).
* **Local Deployment** – Runs on your local machine via Flask.

---

## 🧠 Use Case

For personal use, educational projects, and cybersecurity practice — focused on secure storage logic without third-party cloud storage.

---

## 🗂️ Project File Structure

```
password_manager/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── crypto_utils.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── dashboard.html
│
├── instance/
│   └── vault.db
│
├── config.py
├── run.py
├── requirements.txt
├── LICENSE
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Language | Framework | Encryption | Hashing | Local Server | IDE |
|----------|-----------|------------|---------|---------------|-----|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) | ![AES](https://img.shields.io/badge/AES--256-6e4cff?style=for-the-badge&logoColor=white) | ![bcrypt](https://img.shields.io/badge/bcrypt-ff8800?style=for-the-badge&logoColor=white) | ![Flask Localhost](https://img.shields.io/badge/Flask%20Server-005f99?style=for-the-badge&logo=flask&logoColor=white)<br>![XAMPP](https://img.shields.io/badge/XAMPP-FB7A24?style=for-the-badge&logo=xampp&logoColor=white) | ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white) |

---

## ✅ Installation & Setup

```bash
# Clone the repo
https://github.com/alaminO8islam/password_manager.git

# Navigate to the project folder
cd password_manager

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt

# Run the app
python run.py
```

Open `http://127.0.0.1:5000` in your browser to access the Password Manager.

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---


## ⭐️ Don't forget to star the repo if you liked it!

---
