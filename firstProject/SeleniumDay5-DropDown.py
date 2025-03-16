import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)

driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("Rohit")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-button']").click()
time.sleep(3)
search1=driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']")
for i in search1:
    if "Rohit Shetty" in i.text:
        i.click()
    else:
        print("out")
Select(driver.find_element(By.XPATH,"//select[@id='country']")).select_by_visible_text("India")
time.sleep(2)
Select(driver.find_element(By.XPATH,"//select[@id='country']")).select_by_value("china")
time.sleep(2)
Select(driver.find_element(By.XPATH,"//select[@id='country']")).select_by_index(2)
time.sleep(2)
