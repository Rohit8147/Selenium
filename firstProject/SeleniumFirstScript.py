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
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Rohit")

ph_n=8147388442
driver.find_element(By.ID,"ph_no").send_keys(ph_n)
driver.find_element(By.ID,"email").send_keys("rohit@gmail.com")
driver.find_element(By.XPATH,"//input[@value='Employed']").click()
driver.find_element(By.ID,"CORE_JAVA").click()
time.sleep(1)
driver.find_element(By.ID,"SPRING").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='date']").send_keys("12/01/2025")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='time']").send_keys("10:00 AM")
time.sleep(1)
driver.find_element(By.ID, "desc").send_keys("Intrested to join the Java Course")
time.sleep(1)
#driver.find_element(By.XPATH,"//input[@name='Submit']").click()
driver.find_element(By.LINK_TEXT,"Academic Projects").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.back()
time.sleep(2)
driver.refresh()
time.sleep(2)
