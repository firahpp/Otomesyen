from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True) # option untuk tidak langsung close jika code tidak ditutup dengan driver.close()
option.add_experimental_option('excludeSwitches', ['enable-logging']) # option untuk tidak menampilkan error logging yang tidak berhubungan dengan jalannya code/automation


driver = webdriver.Chrome(options=option) # optionnya jangan lupa taro disini ya
url = 'https://demoqa.com/menu'
driver.implicitly_wait(10) # waiting, cukup 1 x di tulis
driver.maximize_window() # membuka window ukuran maksimum

driver.get(url) # buka url

# define semua element dari menu yang mau dilakukan aksi berantai / action chain
menu = driver.find_element(By.XPATH, '//a[contains(text(),"Main Item 2")]')
submenu = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')
subsubitem2 = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[2]/a')

action = ActionChains(driver) # panggil method/function dari actionchain

#action chainnya disini
action.move_to_element(menu) 
action.move_to_element(submenu)
action.click(subsubitem2)

action.perform() # menutup rangkaian actionchain can menjalankan semua action

driver.close()
