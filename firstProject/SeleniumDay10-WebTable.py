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
'''TableText=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td[3]")
print(TableText.text)
row=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td")
for i in row:
    print(i.text, end=", ")
    '''

column=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/td[4]")
for i in column:
    print(i.text)
   