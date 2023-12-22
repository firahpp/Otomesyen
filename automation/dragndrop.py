from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

Option = webdriver.ChromeOptions() #Option = menghindari website auto-close
Option.add_experimental_option('detach', True)
Option.add_experimental_option('excludeSwitches', ['enable-logging']) #tidak menampilkan error logging yg tidak berhubungan, di terminal
driver = webdriver.Chrome(options=Option)

url = 'https://demoqa.com/droppable'
driver.implicitly_wait(5)
driver.maximize_window()

driver.get(url) 
#define element
drag = driver.find_element(By.XPATH, '//*[@id="draggable"]')
drop = driver.find_element(By.XPATH, '//*[@id="droppable"]')

#action
action = ActionChains(driver)
action.drag_and_drop(drag, drop)
#action.drag_and_drop_by_offset(drag, 500, 500)
action.perform()
sleep(5)

driver.close()