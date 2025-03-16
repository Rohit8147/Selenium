import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
driver.implicitly_wait(5)
driver.find_element(By.ID, "msdd").click()
time.sleep(2)
option1=driver.find_elements(By.XPATH, "//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all']")
for i in option1:
    print(i.text)
    if "Dutch" in i.text:
        i.click()
    else:
        pass
'''Select(driver.find_element(By.XPATH,"//select[@id='Skills']")).select_by_visible_text("APIs")
time.sleep(2)
Select(driver.find_element(By.XPATH,"//select[@id='Skills']")).select_by_value("C")
time.sleep(2)
Select(driver.find_element(By.XPATH,"//select[@id='Skills']")).select_by_index(2)
time.sleep(2)'''