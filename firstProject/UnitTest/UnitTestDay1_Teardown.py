import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class HRApplication(unittest.TestCase):
    def setUp(self):
        service_obj= Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
        self.driver=webdriver.Chrome(service=service_obj)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def test_1loginvalidation(self):
        self.driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(4)

    def test_2aftervalidation(self):
        print("It's second test case")

    def test_3titlevalidation(self):
        a=self.driver.title
        assert "OrangeHRM" in a
        print(a)
        time.sleep(4)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()







