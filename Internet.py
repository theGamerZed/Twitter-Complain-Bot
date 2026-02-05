from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
    def tweet_the_complain(self):
        pass


