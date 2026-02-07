import pickle
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
        self.accept_cookies("//button[.//span[normalize-space()='Accept all cookies']]")

        with open("x_cookies.pkl", "rb") as f: # Get this from a prior login session, you can use browser dev tools to export cookies or use Selenium to save them after logging in once
            cookies = pickle.load(f)
        for cookie in cookies:
           try:
                cookie.pop("sameSite", None)
                cookie.pop("expiry", None)
                self.driver.add_cookie(cookie)
           except Exception as e:
                print(f"Error adding cookie: {e}")
        self.driver.refresh()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/home']")))  # confirm login via presence of home link... or use a waiting time to see it manually if you want...
        print("✅ Logged in via cookies")
        icon_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//a[@data-testid='SideNav_NewTweet_Button']")))
        # self.driver.execute_script("arguments[0].click();", icon_btn) use this if normal click doesn't work it is called javascript click and it can bypass some issues with normal click
        icon_btn.click()
        print("Icon button clicked")
        time.sleep(2)  # Wait for the tweet box to appear
        tweet_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox' and @contenteditable='true']")))
        tweet_box.clear()
        tweet_content = f"Hey Internet Provider[vodafone], why is my internet speed {self.down} Mbps down and {self.up} Mbps up? this is just a python project BTW"
        tweet_box.send_keys(tweet_content)
        print("Tweet content entered")
        time.sleep(2)  # Wait for content to be entered
        post_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweetButton']"))) 
        post_btn.click()
        print("Tweet posted")
        print("✅ Complaint tweeted successfully")
        # onto the next project...

