import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://login.salesforce.com/?locale=in")
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//input[@id='username']").send_keys("1998rohitkumar.r-nj7u@force.com")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("9085730042@Rk")

driver.find_element(By.XPATH,"//input[@id='Login']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='View Accounts']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[@title='New']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='Name']").send_keys("Rohit Kumar Singh")
driver.find_element(By.XPATH,"(//input[@name='Phone'])[1]").send_keys("8147388332")
driver.find_element(By.XPATH,"//button[@id='combobox-button-268']").click()
type=driver.find_elements(By.XPATH,"//div[@id='dropdown-element-268']")
for option in type:
    if "Analyst" in option.text:
        option.click()
        break
time.sleep(5)

driver.find_element(By.XPATH,"(//button[text()='Save'])[2]").click()
time.sleep(5)


verify=driver.find_element(By.XPATH,"(//lightning-formatted-text[text()='Rohit Kumar Singh'])[1]").is_displayed()
print(verify)


