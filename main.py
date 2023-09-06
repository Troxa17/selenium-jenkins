from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


service = Service(r"C:\Users\Troxa\OneDrive\Рабочий стол\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

class Selenium_Func:

    def Flash_Live(self):
        driver.get('https://www.flashscore.com/')
        time.sleep(5)
        driver.find_element(By.CLASS_NAME,'filters__tab selected').click()
        time.sleep(5)


Selenium = Selenium_Func()
Selenium.Flash_Live()