import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.implicitly_wait(5)


driver.find_element(By.XPATH,"//input[@id='datepicker2']").click()
daterow=driver.find_elements(By.XPATH,"//input[@ID='datepicker2']/following::div[@class='datepick-popup']/div/div[1]/following::table/tbody/tr[3]/td[4]")
print( len(daterow))

datecolums=driver.find_elements(By.XPATH,"//input[@ID='datepicker2']/following::div[@class='datepick-popup']/div/div[1]/following::table/tbody/tr[3]/td[4]")
print(len(datecolums))



pickadate=driver.find_elements(By.XPATH,"//input[@ID='datepicker2']/following::div[@class='datepick-popup']/div/div[1]/following::table/tbody/tr[3]/td[4]")

for i in pickadate:
    i.click()

time.sleep(3)