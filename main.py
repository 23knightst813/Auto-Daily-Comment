from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Set the path to the chromedriver executable
chrome_driver_path = os.getenv("DRIVER_PATH")

# Set the path to the Brave Browser executable
options = Options()
options.binary_location = os.getenv("BROWSER_PATH")