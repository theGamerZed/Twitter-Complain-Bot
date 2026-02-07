import email
from selenium import webdriver
from selenium.webdriver.common.by import By   
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
from dotenv import load_dotenv

load_dotenv() 
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

class InternetSpeedTwitterBot:
    def __init__(self, up , down):
        self.up = up
        self.down = down
        self.driver = webdriver.Chrome(options=chrome_options)
    def goto_website(self,destination):
        self.driver.get(destination)
    def close(self):
        self.driver.quit()
    def accept_cookies(self, cookie_element):
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, cookie_element)))
            cookie_button.click()
            print("Cookie clicked")
            time.sleep(2)  # Wait for popup to close
        except Exception:
            print("No cookie popup found or error clicking it.")
    def get_internet_speed(self):
        pass
        self.goto_website("https://www.speedtest.net/")
        self.driver.implicitly_wait(5)
        self.accept_cookies('//*[@id="onetrust-accept-btn-handler"]')
        start_button = self.driver.find_element(By.CSS_SELECTOR,"#container > div.pre-fold > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.start-button > a > span.start-text")
        start_button.click()
        time.sleep(45)  # Wait for test to complete
        self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(start_button.text,self.down,self.up)
    def tweet_the_complain(self):
        self.goto_website("https://www.x.com")
        self.driver.implicitly_wait(5)
        self.accept_cookies('//*[@id="layers"]/div/div/div/div/div/div[2]/button[1]/div')
        self.driver.execute_script("window.scrollBy(0, 500)") 
        try:
            signin = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a/div')))
            signin.click()
            print(signin.text)
        except Exception as e:
            print(f"Error finding sign-in button: {e}") 
        time.sleep(2)  # Wait for sign-in options to load
        try:
            wait = WebDriverWait(self.driver, 15)
            email_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='text' and @type='text']")))
            email_input.clear()
            time.sleep(2)  # Small delay to ensure field is ready
            email_input.send_keys(os.getenv("EMAIL"))
        except Exception as e:
            print(f"Error finding email input field: {e}")
        time.sleep(2)  # Wait for email to be processed and Next button to become clickable
        try:
            wait = WebDriverWait(self.driver, 15)
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Next']")))
            next_button.click()
            print("Next button clicked")
        except Exception as e:
            print(f"Error finding Next button: {e}")
        time.sleep(2)  # Wait for password field to load
        try:
            password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Password']/ancestor::div//input[@type='password']")))
            password_input.clear()
            password_input.send_keys(os.getenv("PASSWORD"))
            print("Password entered")
        except Exception as e:
            print(f"Error finding password input field: {e}")
