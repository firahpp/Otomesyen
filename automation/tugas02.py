from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

Option = webdriver.ChromeOptions()
Option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=Option)

url = 'https://demoqa.com/webtables'
driver.get(url)
driver.maximize_window()
sleep(2)


driver.find_element(By.ID, 'addNewRecordButton').click()

#input data (1)
driver.find_element(By.ID, 'firstName').send_keys('Firah')
sleep(1)
driver.find_element(By.ID, 'lastName').send_keys('Putri Pratiwi')
sleep(1)
driver.find_element(By.ID, 'userEmail').send_keys('mautauaja@xx.com')
sleep(1)
driver.find_element(By.ID, 'age').send_keys('23')
sleep(1)
driver.find_element(By.ID, 'salary').send_keys('300000')
sleep(1)
driver.find_element(By.ID, 'department').send_keys('Store')
sleep(1)
driver.find_element(By.ID, 'submit').click()

sleep(2)

#input data (2)
driver.find_element(By.ID, 'addNewRecordButton').click()
sleep(1)
driver.find_element(By.ID, 'firstName').send_keys('Taylor')
sleep(1)
driver.find_element(By.ID, 'lastName').send_keys('Swift')
sleep(1)
driver.find_element(By.ID, 'userEmail').send_keys('bbcaaa@xx.com')
sleep(1)
driver.find_element(By.ID, 'age').send_keys('39')
sleep(1)
driver.find_element(By.ID, 'salary').send_keys('190000000')
sleep(1)
driver.find_element(By.ID, 'department').send_keys('Music')
sleep(1)
driver.find_element(By.ID, 'submit').click()

sleep(2)

#input data (3)
driver.find_element(By.ID, 'addNewRecordButton').click()
sleep(1)
driver.find_element(By.ID, 'firstName').send_keys('Grizzie')
sleep(1)
driver.find_element(By.ID, 'lastName').send_keys('Bear')
sleep(1)
driver.find_element(By.ID, 'userEmail').send_keys('wwwbear@xx.com')
sleep(1)
driver.find_element(By.ID, 'age').send_keys('17')
sleep(1)
driver.find_element(By.ID, 'salary').send_keys('2000')
sleep(1)
driver.find_element(By.ID, 'department').send_keys('Detective')
sleep(1)
driver.find_element(By.ID, 'submit').click()
sleep(1)

driver.close()