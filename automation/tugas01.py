from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()


#get url
driver.get('https://www.tiket.com')
sleep(2)
print(driver.title)
driver.get('https://www.tokopedia.com/')
sleep(2)
print(driver.title)
driver.get('https://www.orangsiber.com/')
sleep(2)
print(driver.title)
driver.get('https://automatetheboringstuff.com/')
print(driver.title)

driver.close()
