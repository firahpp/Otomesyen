from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
tiket = 'https://www.tiket.com/'

driver.get(tiket)
try:
    WebDriverWait(driver,5).until(EC.title_contains('tiket.com'))
    Title = driver.title
    print(Title)
    
except TimeoutException:
    print('Tidak ditemukan')
    pass
