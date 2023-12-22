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

list_data = [{'first_name':'Firah', 'last_name':'Putri Pratiwi', 
           'email':'mautauaja@xx.com', 'age':'23', 'salary':'300000','department':'Store'
           },
             {'first_name':'Taylor', 'last_name':'Swift', 
           'email':'bbcaaa@xx.com', 'age':'39', 'salary':'190000000','department':'Music'
           },
             {'first_name':'Grizzie', 'last_name':'Bear', 
           'email':'wwwbear@xx.com', 'age':'17', 'salary':'2000','department':'Detective'
           }]

for data in list_data:
    driver.find_element(By.ID, 'firstName').send_keys(data['first_name'])
    driver.find_element(By.ID, 'lastName').send_keys(data['last_name'])
    driver.find_element(By.ID, 'userEmail').send_keys(data['email'])
    driver.find_element(By.ID, 'age').send_keys(data['age'])
    driver.find_element(By.ID, 'salary').send_keys(data['salary'])
    driver.find_element(By.ID, 'department').send_keys(data['department'])