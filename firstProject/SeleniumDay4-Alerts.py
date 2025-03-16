import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)
driver.find_element(By.ID,"alertBtn").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element(By.ID,"confirmBtn").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Prompt Alert']").click()
time.sleep(2)
driver.switch_to.alert.send_keys("Automation Testing")
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)