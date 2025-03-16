import unittest
from symtable import Class

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time



class UnitTestScripts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service_obj = Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
        global driver
        driver = webdriver.Chrome(service=service_obj)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        print("Start")
        driver.implicitly_wait(5)

    def test_login(self):
        driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("login Done")
        time.sleep(4)

    def test_searchuser(self):
        driver.find_element(By.XPATH, "//span[text()='Admin']").click()
        a="FMLName"
        driver.find_element(By.XPATH, "//label[text()='Username']//following::input[1]").send_keys(a)
        driver.find_element(By.XPATH, "//button[text()=' Search ']").click()

        time.sleep(4)

        l1=driver.find_elements(By.XPATH,"//div[@class='oxd-table-cell oxd-padding-cell']")
        if l1[1].text == a:
            print("It's correct")

        else:
            print("It's wrong")


    @classmethod
    def tearDownClass(cls):
        driver.close()
        print("Bye")















