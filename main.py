from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os


# Load the environment variables
load_dotenv()

# Increment the day
new_day = int(os.getenv('DAY')) + 1
os.environ['DAY'] = str(new_day)

#Build The Comment
comment = f"Day {new_day} of 100 of {os.getenv('CHALLENGE_NAME')}"

# Set the path to the chromedriver executable
driver_path = os.getenv("DRIVER_PATH")

# Set the path to the Brave Browser executable
options = Options()
options.binary_location = os.getenv("BROWSER_PATH")

#initialize the browser
driver = webdriver.Chrome(service=Service(driver_path), options=options)

# Open the Instagram page
driver.get('https://www.instagram.com/openminded.podcast/reels')

# Xpath to the reels
reels_xpath = "//div[contains(@class, 'v1Nh3')]/a"

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, reels_xpath))
    )

# Pick the newest post
reels = driver.find_elements(By.XPATH, reels_xpath)

# Click on the first reel
reels[0].click()


# Xpath to the comment textarea
comment_xpath = "//textarea[@aria-label='Add a comment…']"

# Wait for the comment textarea to be present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, comment_xpath))
)

# Find the comment textarea
comment_box = driver.find_element(By.XPATH, comment_xpath)

# Type the comment
comment_box.send_keys(str(comment))

# Submit the comment
comment_box.send_keys("\n")

# Close the browser
driver.quit()

