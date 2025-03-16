import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Windows.html")
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//button[@class='btn btn-info']").click()
time.sleep(2)
windowshan=driver.window_handles
driver.save_screenshot("screenshot.png")
print(windowshan)
time.sleep(2)
driver.switch_to.window(windowshan[0])
time.sleep(2)
driver.switch_to.window(windowshan[1])
time.sleep(2)