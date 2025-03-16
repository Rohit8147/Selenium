import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.implicitly_wait(5)

frame1=driver.find_element(By.XPATH, "//iframe[@id='singleframe']")

driver.switch_to.frame(frame1)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Rohit")
time.sleep(3)