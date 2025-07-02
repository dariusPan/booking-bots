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

All sensitive data like usernames, passwords, and URLs are managed through a `.env` file. See .env.example file.

### Example `.env`

- USERNAME="myusername@xx.com"
- PASSWORD="mypassword"
- BDATE = '2025-05-19'
- TSTART = '830pm' # Booking time start
- TEND = '930pm'   # Booking time end
- SCHEDULE_DATE = "2025-06-30"  # Format: YYYY-MM-DD
- SCHEDULE_TIME = "14:29"  # Format: HH:MM (24-hour) Set 1 minute before when you want to run the bot

---

## 💻 Setup Instructions

### 1. Clone the Repository or download Zip file
```bash
git clone https://github.com/yourusername/booking-bot.git
cd booking-bot
```
```
Click on top right code button
Download Zip
Extract Zip file
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
# add in your user and password and change the timing for booking and schedule
```

### 3. Setup and run program

```bash
pip install .
# adjust booking time and credentials in .env file
python run.py
python scheduler.py
# if your schedule time is before the current time, the code will run
# use Ctrl+C to stop the scheduler
# for testing
python run.py test
python scheduler.py test

```

### 4. Windows Task Scheduler Setup (Optional)

- Press `Win + R` → type `taskschd.msc` → press Enter.
- In the **Actions pane**, click **"Create Task..."** (not Basic Task for more options).
- In the general tab
    - **Name**: `RunPythonScript`
    - **Description**: Automatically runs `run.py` on a schedule.
    - **Security options**:
        - Check **"Run whether user is logged on or not"**.
        - Check **"Run with highest privileges"** if needed.
- In the trigger tab
    - Click **"New..."**
    - Choose:
    - Begin task: *On a schedule*
    - Set frequency (e.g. daily, weekly).
    - Set **start date and time**.
    - Click OK.
- In the action tab
    - Click **"New..."**
    - **Action**: *Start a program*
    - **Program/script**:
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
