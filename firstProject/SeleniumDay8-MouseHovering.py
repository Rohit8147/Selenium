import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Windows.html")
driver.implicitly_wait(5)

action=ActionChains(driver)
interaction=driver.find_element(By.XPATH,"//a[text()='Interactions ']")
draganddrop=driver.find_element(By.XPATH,"//a[text()='Drag and Drop ']")
static=driver.find_element(By.XPATH,"//a[text()='Static ']")
time.sleep(2)
action.move_to_element(interaction).perform()
time.sleep(2)
action.move_to_element(draganddrop).perform()
time.sleep(2)
static.click()

driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)
buttonclick=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
action.double_click(buttonclick).perform()
time.sleep(2)


drag=driver.find_element(By.XPATH,"//p[text()='Drag me to my target']")
drop=driver.find_element(By.XPATH,"//div[@id='droppable']")

action.drag_and_drop(drag,drop).perform()
time.sleep(2)