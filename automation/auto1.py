from selenium import webdriver
from time import sleep 

Option = webdriver.ChromeOptions()
Option.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=Option)

#buka url orangehrm
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
print(driver.title)

sleep(7)

