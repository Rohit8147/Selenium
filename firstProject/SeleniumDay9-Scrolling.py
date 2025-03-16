import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)
driver.find_element(By.ID,"singleFileInput").send_keys("C://Users//a778983//OneDrive - Eviden//Desktop//Test.png")
time.sleep(5)

element=driver.find_element(By.XPATH,"//a[text()='Blogger']")
driver.execute_script("arguments[0].scrollIntoView();", element)

time.sleep(5)

