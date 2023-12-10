from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


#get url
# tiket = 'https://www.tiket.com/'
# tokped = 'https://www.tokopedia.com/'
# orangSiber = 'https://www.orangsiber.com/'
# automateBoring = 'https://automatetheboringstuff.com/'


driver = webdriver.Chrome()

url = ['https://www.tiket.com/', 'https://www.tokopedia.com/', 'https://www.orangsiber.com/'
       'https://automatetheboringstuff.com/']





# driver.get(tiket)
# try
#     WebDriverWait(driver,5).until(EC.title_contains('tiket.com'))
#     Title = driver.title
#     print(Title)
    
# except TimeoutException:
#     print('Tidak ditemukan')
#     pass



