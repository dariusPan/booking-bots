# 🧾 Booking Bot

**Booking Bot** is an automation tool built with **Python** and **Selenium** to automate booking tasks on a target website. It simulates human interaction to fill out forms, click buttons, and complete reservation processes automatically.

This bot is designed for flexibility and can run manually or on a schedule (can run daily). It is cross-platform and can be configured easily using a `.env` file for environment-specific settings such as login credentials and booking preferences.

---

## 🛠️ Requirements

- Python 3.8+
- Google Chrome
- ChromeDriver (matching your Chrome version)
- Virtual environment recommended

---

## 🔐 Using the `.env` File

All sensitive data like usernames, passwords, and URLs are managed through a `.env` file.

### Example `.env`

- USERNAME="myusername@xx.com"
- PASSWORD="mypassword"
- BDATE = '2025-05-19'
- TSTART = '830pm' # Booking time start
- TEND = '930pm'   # Booking time end

- SCHEDULE_DATE = "2025-06-30"  # Format: YYYY-MM-DD
- SCHEDULE_TIME = "14:31"  # Format: HH:MM (24-hour)

---

## 💻 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/booking-bot.git
cd booking-bot
```

### 2. Install virtual environment and dependencies

```bash
python -m venv venv
# Activate the environment:
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# copy or create your .env file
cp .env.example .env
```

### 3. Setup and run program

```bash
pip install .
# adjust booking time and credentials in .env file
python run.py

```

---

## 🔧 What’s Next?

Let me know if you'd like:
- A sample `.env.example` file
- A `Dockerfile` for containerized deployment
- Sample Selenium logic in `Qreserve.py`
- GitHub Actions CI workflow for testing

I can generate or scaffold any of those to help you ship a polished open-source project.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
