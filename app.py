from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time

#set chromodriver.exe path

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

driver.implicitly_wait(0.5)

#launch URL(поиск элемента на странице по XPATH)

driver.get("https://medium.com/")
time.sleep(5)
elem = driver.find_elements(By.XPATH,  '/html/body/div[1]/div/div[1]/nav/div/a[1]')
print(elem)
time.sleep(10)






