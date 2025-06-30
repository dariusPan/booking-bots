from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Config from .env
BOOKING_URL = "https://my.qreserve.com/login"
USERNAME = os.getenv("USER")
PASSWORD = os.getenv("PASS")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
BDATE = os.getenv("BDATE")
TSTART = os.getenv("TSTART")
TEND = os.getenv("TEND")

DELAY_WEB = 3
DELAY_CLICK = 0.5
DELAY_LOAD = 10

def run_bot():
    print("[Bot] Starting the booking bot...")

    # webdrive setup
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-popup-blocking')
    # options.add_argument('--incognito')
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(executable_path="C:/Users/jm.pan/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=options)
    
    # Initialize WebDriver
    try:
        driver = webdriver.Chrome()
    except Exception as e:
        print(f"[Error] Failed to start ChromeDriver: {e}")
        return

    try:
        # Step 1: Navigate to the booking site
        driver.get(BOOKING_URL)
        print(f"[Bot] Navigating to {BOOKING_URL}")
        time.sleep(DELAY_WEB)
        
        # enter credential
        user = driver.find_element(by=By.XPATH, value='//*[@id="email-address"]')
        user.send_keys(USERNAME)
        password = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
        password.send_keys(PASSWORD)
        button = driver.find_element(by=By.XPATH, value='//*[@id="sign-in"]')
        button.click()
        time.sleep(DELAY_LOAD)

        # book facility
        button = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/section[1]/div/div/div[2]/ul/li[8]/button')

        button.click()
        time.sleep(DELAY_LOAD)

        # choose badminton
        button = driver.find_element(by=By.XPATH, value='//*[@id="create-new-reservation"]')
        button.click()
        time.sleep(DELAY_LOAD)

        # choose venue
        button = driver.find_element(by=By.XPATH, value='//*[@id="reserve-next"]')
        button.click()
        time.sleep(DELAY_LOAD)
        button = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/input')
        button.click()
        button.send_keys(Keys.CONTROL + "a")
        button.send_keys(BDATE)
        button.send_keys(Keys.RETURN)
        time.sleep(DELAY_CLICK)

        # pick the date
        button_start = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/input')
        button_start.click()
        button_start.send_keys(Keys.CONTROL + "a")
        button_start.send_keys(TSTART)
        button_start.send_keys(Keys.RETURN)
        time.sleep(DELAY_CLICK)

        button_end = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[2]/div/div[4]/div/div/div/div/div/input')
        button_end.click()
        button_end.send_keys(Keys.CONTROL + "a")
        button_end.send_keys(TEND)
        button_end.send_keys(Keys.RETURN)
        time.sleep(DELAY_LOAD)

        # Reserve
        button = driver.find_element(by=By.XPATH, value='//*[@id="reserve-next"]')
        button.click()
        time.sleep(DELAY_LOAD)
        button = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/fieldset/div[1]/div/span/select')
        button.click()
        time.sleep(DELAY_CLICK)
        button = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/fieldset/div[1]/div/span/select/option[3]')
        button.click()
        time.sleep(DELAY_LOAD)
        button = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/fieldset/div[2]/div/span/select')
        button.click()
        time.sleep(DELAY_CLICK)
        button = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/fieldset/div[2]/div/span/select/option[3]')
        button.click()
        time.sleep(DELAY_CLICK)
        button = driver.find_element(by=By.XPATH, value='//*[@id="book-reserve"]')
        button.click()
        time.sleep(DELAY_LOAD)
        driver.close()
        print("booking successful")
    
    except (NoSuchElementException, TimeoutException) as e:
        print(f"[Error] Element not found or timed out: {e}")
    except Exception as e:
        print(f"[Error] Unexpected error occurred: {e}")
    finally:
        print("[Bot] Closing browser...")
        driver.quit()
        print("[Bot] Bot finished.")
