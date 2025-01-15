from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

load_dotenv()

INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
new_day = int(os.getenv('DAY')) + 1
os.environ['DAY'] = str(new_day)

comment = f"Day {new_day} of 100 of {os.getenv('CHALLENGE_NAME')}"
driver_path = os.path.join(os.path.dirname(__file__), os.getenv('DRIVER_PATH'))
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

def login_to_instagram(driver):
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)
    
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_input = driver.find_element(By.NAME, "password")
    
    username_input.send_keys(INSTAGRAM_USERNAME)
    password_input.send_keys(INSTAGRAM_PASSWORD)
    
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    time.sleep(5)

def main():
    try:
        options = webdriver.ChromeOptions()
        options.binary_location = brave_path
        driver = webdriver.Chrome(service=Service(driver_path), options=options)
        
        login_to_instagram(driver)
        
        driver.get('https://www.instagram.com/openminded.podcast/reels')
        
        accept_cookies_xpath = "//button[contains(text(), 'Allow all cookies')]"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, accept_cookies_xpath))
        ).click()
        
        reels_xpath = "//div[contains(@class, 'v1Nh3')]/a"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, reels_xpath))
        )
        
        reels = driver.find_elements(By.XPATH, reels_xpath)
        reels[0].click()
        
        comment_xpath = "//textarea[@aria-label='Add a comment…']"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, comment_xpath))
        )
        
        comment_box = driver.find_element(By.XPATH, comment_xpath)
        comment_box.send_keys(comment)
        comment_box.send_keys("\n")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()