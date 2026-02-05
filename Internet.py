from selenium import webdriver
from selenium.webdriver.common.by import By   
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
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
    def get_internet_speed(self):
        self.goto_website("https://www.speedtest.net/")
        self.driver.implicitly_wait(2)
        try:
            # cookie_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
            cookie_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            cookie_button.click()
        except:
            print("No cookie popup found")
        start_button = self.driver.find_element(By.CSS_SELECTOR,"#container > div.pre-fold > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-view > div > div.start-button > a > span.start-text")
        start_button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(start_button.text,self.down,self.up)
    def tweet_the_complain(self):
        pass


