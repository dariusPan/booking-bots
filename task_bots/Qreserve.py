from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
DELAY_LOAD = 10

def keep_sending(driver, duration, xpath_value, keys):
    try:
        # Wait up to 10 seconds, checking every 500 ms by default
        element = WebDriverWait(driver, duration).until(
            # lambda driver: driver.find_element(by=By.XPATH, value=xpath_value)
            EC.presence_of_element_located((By.XPATH, xpath_value))
        )
        element.send_keys(keys)
    except:
        print("Element not found within the timeout.")

def keep_clicking(driver, duration, xpath_value):
    try:
        # Wait up to 10 seconds, checking every 500 ms by default
        element = WebDriverWait(driver, duration).until(
            # lambda driver: driver.find_element(by=By.XPATH, value=xpath_value)
            EC.presence_of_element_located((By.XPATH, xpath_value))
        )
        element.click()
    except:
        print("Element not found within the timeout.")

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
        keep_sending(driver, DELAY_LOAD, '//*[@id="email-address"]', USERNAME)
        keep_sending(driver, DELAY_LOAD, '//*[@id="password"]', PASSWORD)
        keep_clicking(driver, DELAY_LOAD, '//*[@id="sign-in"]')
        # time.sleep(DELAY_LOAD)
        
        # book facility
        keep_clicking(driver, DELAY_LOAD, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/section[1]/div/div/div[2]/ul/li[8]/button')
        # time.sleep(DELAY_LOAD)
        
        keep_clicking(driver, DELAY_LOAD, '//*[@id="create-new-reservation"]')
        # time.sleep(DELAY_LOAD)
        
        # choose venue
        keep_clicking(driver, DELAY_LOAD, '//*[@id="reserve-next"]')
        # time.sleep(DELAY_LOAD)
        print("checkpoint")
        try:
            # Wait up to 10 seconds, checking every 500 ms by default
            element = WebDriverWait(driver, DELAY_LOAD).until(
                # lambda d: d.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/input')
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/input'))
            )
            element.click()
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(BDATE)
            element.send_keys(Keys.RETURN)
        except:
            print("Element not found within the timeout.")
            
        print("checkpoint 2")
        
        # pick the date
        try:
            # Wait up to 10 seconds, checking every 500 ms by default
            element = WebDriverWait(driver, DELAY_LOAD).until(
                # lambda d: d.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/input')
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/input'))
            )
            element.click()
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(TSTART)
            element.send_keys(Keys.RETURN)
        except:
            print("Element not found within the timeout.")
        
        try:
            # Wait up to 10 seconds, checking every 500 ms by default
            element = WebDriverWait(driver, DELAY_LOAD).until(
                # lambda d: d.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[2]/div/div[4]/div/div/div/div/div/input')
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[2]/div/div[4]/div/div/div/div/div/input'))
            )
            element.click()
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(TEND)
            element.send_keys(Keys.RETURN)
        except:
            print("Element not found within the timeout.")

        # Reserve
        keep_clicking(driver, DELAY_LOAD, '//*[@id="reserve-next"]')
        keep_clicking(driver, DELAY_LOAD, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/fieldset/div[1]/div/span/select')
        keep_clicking(driver, DELAY_LOAD, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/fieldset/div[1]/div/span/select/option[3]')
        keep_clicking(driver, DELAY_LOAD, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/fieldset/div[2]/div/span/select')
        keep_clicking(driver, DELAY_LOAD, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/fieldset/div[2]/div/span/select/option[3]')
        keep_clicking(driver, DELAY_LOAD, '//*[@id="book-reserve"]')
        driver.close()
    
    except (NoSuchElementException, TimeoutException) as e:
        print(f"[Error] Element not found or timed out: {e}")
    except Exception as e:
        print(f"[Error] Unexpected error occurred: {e}")
    finally:
        print("[Bot] Closing browser...")
        driver.quit()
        print("[Bot] Bot finished.")
