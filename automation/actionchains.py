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

url = 'https://demoqa.com/menu'
driver.implicitly_wait(5)
driver.maximize_window()

driver.get(url) 

#define element yg mau di lakukan action chains
menu = driver.find_element(By.XPATH, '//a[contains(text(), "Main Item 2")]')
submenu = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')
sub_subitem2 = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[2]/a')

action = ActionChains(driver) #panggil methode action chains
#move element
action.move_to_element(menu) #memindahkan kursor sesuai ke element yg diinginkan
action.move_to_element(submenu)
action.click(sub_subitem2)
action.perform() #menutup aksi
sleep(5)

driver.close()
