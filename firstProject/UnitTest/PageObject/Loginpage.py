import time

from selenium.webdriver.common.by import By


class LoginPageClass:
    def __init__(self,driver):
        self.driver=driver
        self.username=driver.find_element(By.XPATH, "//input[@name='username']")
        self.password=driver.find_element(By.XPATH, "//input[@name='password']")
        self.submitbutton=driver.find_element(By.XPATH, "//button[@type='submit']")


    def usernameentry(self,uname):
        self.username.send_keys(uname)

    def passwordentry(self,passw):
        self.password.send_keys(passw)

    def loginbuttonclick(self):
        self.submitbutton.click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()