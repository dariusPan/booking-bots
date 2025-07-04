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
EQP = os.getenv("EQP")

if USERNAME is None:
    print("Environment variable is not available")

DELAY_WEB = 3
DELAY_LOAD = 10

def keep_sending(driver, duration, xpath_value, keys):
    try:
        # Wait up to 10 seconds, checking every 500 ms by default
        element = WebDriverWait(driver, timeout=duration, poll_frequency=.5).until(
            EC.presence_of_element_located((By.XPATH, xpath_value))
        )
        element.send_keys(keys)
    except:
        NotFoundError(driver)

def keep_clicking(driver, duration, xpath_value):
    try:
        # Wait up to 10 seconds, checking every 500 ms by default
        element = WebDriverWait(driver, timeout=duration, poll_frequency=.5).until(
            # lambda driver: driver.find_element(by=By.XPATH, value=xpath_value)
            EC.presence_of_element_located((By.XPATH, xpath_value))
        )
        element.click()
    except:
        NotFoundError(driver)
        
def NotFoundError(driver):
    print("Element not found within the timeout.")
    driver.close()
    
def run_bot(TESTFLAG):
    print("[Bot] Starting the booking bot...")

    # webdrive setup
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-popup-blocking')
    # options.add_argument("--kiosk")
    # options.add_argument('--incognito')
    # options.add_argument('--headless')
    
    # Initialize WebDriver
    try:
        driver = webdriver.Chrome(options)
    except Exception as e:
        print(f"[Error] Failed to start ChromeDriver: {e}")

    try:
        # Step 1: Navigate to the booking site
        driver.get(BOOKING_URL)
        print(f"[Bot] Navigating to {BOOKING_URL}")
        
        # enter credential
        keep_sending(driver, DELAY_LOAD, '//*[@id="email-address"]', USERNAME)
        keep_sending(driver, DELAY_LOAD, '//*[@id="password"]', PASSWORD)
        keep_clicking(driver, DELAY_LOAD, '//*[@id="sign-in"]')
        # time.sleep(DELAY_WEB)
    
        # book facility
        # '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/section[1]/div/div/div[2]/ul/li[8]/button'
        if EQP == 'LW':
            keep_clicking(driver, DELAY_LOAD, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/section[1]/div/div/div[2]/ul/li[19]/button')
        elif EQP == 'ALD':
            keep_clicking(driver, DELAY_LOAD, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/section[1]/div/div/div[2]/ul/li[4]/button')
        else:
            keep_clicking(driver, DELAY_LOAD, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/section[1]/div/div/div[2]/ul/li[8]/button')
        # time.sleep(10)
        
        # reserving
        # print("wait for create")
        time.sleep(10)
        keep_clicking(driver, DELAY_LOAD, '//*[@id="create-new-reservation"]')
        # print("created")
        time.sleep(10)
        keep_clicking(driver, DELAY_LOAD, '//*[@id="reserve-next"]')
        # print("checkpoint")

        try:
            # Wait up to 10 seconds, checking every 500 ms by default
            element = WebDriverWait(driver, timeout=DELAY_LOAD, poll_frequency=.5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/input'))
            )
            element.click()
            time.sleep(0.5)
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys('2025-06-19')
            element.send_keys(Keys.RETURN)
        except:
            NotFoundError(driver)

        try:
            # Wait up to 10 seconds, checking every 500 ms by default
            element = WebDriverWait(driver, timeout=DELAY_LOAD, poll_frequency=.5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/input'))
                
            )
            element.click()
            time.sleep(0.5)
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys('1200pm')
            element.send_keys(Keys.RETURN)
        except:
            NotFoundError(driver)
        
        try:
            # Wait up to 10 seconds, checking every 500 ms by default
            element = WebDriverWait(driver, timeout=DELAY_LOAD, poll_frequency=.5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[2]/div/div[4]/div/div/div/div/div/input'))
            )
            element.click()
            time.sleep(0.5)
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys('1230pm')
            element.send_keys(Keys.RETURN)
        except:
            NotFoundError(driver)
        print("Head to last page first")

        # Reserve wait 5 secs to deconflict
        time.sleep(10)
        keep_clicking(driver, DELAY_LOAD, '//*[@id="reserve-next"]')
        time.sleep(0.5)
        keep_clicking(driver, DELAY_LOAD, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/fieldset/div[1]/div/span/select')
        keep_clicking(driver, DELAY_LOAD, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/fieldset/div[1]/div/span/select/option[3]')
        keep_clicking(driver, DELAY_LOAD, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/fieldset/div[2]/div/span/select')
        keep_clicking(driver, DELAY_LOAD, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]/div/fieldset/div[2]/div/span/select/option[3]')
        keep_clicking(driver, DELAY_LOAD, '//*[@id="reservation-book-stage-buttons"]/button[1]')

        # Wait till the date and time is available
        time.sleep(28)

        try:
            # Wait up to 10 seconds, checking every 500 ms by default
            element = WebDriverWait(driver, timeout=DELAY_LOAD, poll_frequency=.5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/input'))
            )
            element.click()
            time.sleep(0.5)
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(BDATE)
            element.send_keys(Keys.RETURN)
        except:
            NotFoundError(driver)

        try:
            # Wait up to 10 seconds, checking every 500 ms by default
            element = WebDriverWait(driver, timeout=DELAY_LOAD, poll_frequency=.5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div/div/input'))
                
            )
            element.click()
            time.sleep(0.5)
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(TSTART)
            element.send_keys(Keys.RETURN)
        except:
            NotFoundError(driver)
        
        try:
            # Wait up to 10 seconds, checking every 500 ms by default
            element = WebDriverWait(driver, timeout=DELAY_LOAD, poll_frequency=.5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[2]/div/div[4]/div/div/div/div/div/input'))
            )
            element.click()
            time.sleep(0.5)
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(TEND)
            element.send_keys(Keys.RETURN)
        except:
            NotFoundError(driver)
        print("Filling in booking date and time")

        # Reserve wait 3 secs to deconflict
        time.sleep(3)
        keep_clicking(driver, DELAY_LOAD, '//*[@id="reserve-next"]')
        time.sleep(0.5)
        if TESTFLAG:
            print('[Bot] Test complete')
        else:
            keep_clicking(driver, DELAY_LOAD, '//*[@id="book-reserve"]')
            print('[Bot] Booking Successful')
        driver.close()
    
    except Exception as e:
        print(f"[Error] Unexpected error occurred: {e}")
    finally:
        print("[Bot] Closing browser...")
        driver.quit()
        print("[Bot] Bot finished.")
