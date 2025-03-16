import time

from selenium.webdriver.common.by import By


class PIMPageClass:
    def __init__(self,driver):
        self.driver=driver
        self.firstname=driver.find_element(By.XPATH, "//input[@name='firstName']")
        self.middlename=driver.find_element(By.XPATH, "//input[@name='middleName']")
        self.lastname=driver.find_element(By.XPATH, "//input[@name='lastName']")
        self.save=driver.find_element(By.XPATH, "//button[text()=' Save ']")

    def enterempdetails(self,fname,mname,lname):
        self.firstname.send_keys(fname)
        self.middlename.send_keys(mname)
        self.lastname.send_keys(lname)

    def savebutton(self):
        time.sleep(5)
        self.save.click()