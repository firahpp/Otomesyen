from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

Option = webdriver.ChromeOptions()
Option.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=Option)


#buka url orangehrm
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.implicitly_wait() #nge set waktu tunggu

driver.maximize_window()
sleep(5)

#input user
driver.find_element(By.NAME, 'username').send_keys('Admin')
driver.find_element(By.NAME,'password').send_keys('admin123')

