from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True) # option untuk tidak langsung close jika code tidak ditutup dengan driver.close()
option.add_experimental_option('excludeSwitches', ['enable-logging']) # option untuk tidak menampilkan error logging yang tidak berhubungan dengan jalannya code/automation

driver = webdriver.Chrome(options=option) # optionnya jangan lupa taro disini ya
url = 'https://demoqa.com/droppable'
driver.implicitly_wait(10) # waiting, cukup 1 x di tulis
driver.maximize_window() # membuka window ukuran maksimum

driver.get(url) # buka url

draggable_element = driver.find_element(By.ID, 'draggable') # ini element yang mau digeser
droppable_element = driver.find_element(By.ID, 'droppable') # ini element yang nampung

action = ActionChains(driver)
# action.drag_and_drop(draggable_element, droppable_element)
action.drag_and_drop_by_offset(draggable_element,100,100)
action.perform()

# driver.close()

