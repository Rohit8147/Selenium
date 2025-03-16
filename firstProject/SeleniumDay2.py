import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.durgasoft.com/registration.asp")
print(driver.current_url)
print(driver.title)

employed = (driver.find_element(By.XPATH,"//input[@value='Employed']"))
print(employed.is_displayed()) #true
print(employed.is_enabled()) #true
print(employed.is_selected()) #false
employed.click()
print(employed.is_selected())
