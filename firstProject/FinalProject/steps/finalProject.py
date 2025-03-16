from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

service_obj = Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://aemoriginms6-omnichanneladmin.stellantis.com/vehicle-list-selection")
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(3)


driver.find_element(By.ID,"details-button").click()
time.sleep(3)

driver.find_element(By.XPATH,"//a[@id='proceed-link']").click()

driver.find_element(By.XPATH,"//input[@name='httpd_username']").send_keys("aemorigin-user")
driver.find_element(By.XPATH,"//input[@name='httpd_password']").send_keys("12hourS-1-circle")
driver.find_element(By.XPATH,"//input[@name='login']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//div[@class=' css-1saa4cv-control']").click()
dropdown_options=driver.find_elements(By.XPATH,"//div[@class=' css-b62m3t-container']//following::div[@class=' css-18o7ivx-menu']")
for option in dropdown_options:
    if "Belgium" in option.text:
        option.click()
    else:
        print("market out")


driver.find_element(By.XPATH,"//div[@class=' css-1saa4cv-control']").click()
dropdown_options=driver.find_elements(By.XPATH,"//div[@class=' css-b62m3t-container']//following::div[@class=' css-18o7ivx-menu']")
for option in dropdown_options:
    if "French" in option.text:
        option.click()
    else:
        print("language out")


driver.find_element(By.XPATH,"(//div[@class=' css-b62m3t-container'])[3]").click()
dropdown_options=driver.find_elements(By.XPATH,"(//div[@class=' css-b62m3t-container'])[3]//following::div[@class=' css-18o7ivx-menu']")
for option in dropdown_options:
    if "DS" in option.text:
        option.click()
    else:
        print("language out")
time.sleep(4)

driver.find_element(By.XPATH,"//label[text()='Car Selector Prod Live']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(10)

