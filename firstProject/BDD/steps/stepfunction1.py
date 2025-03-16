import time
import behave
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@Given ("I launch OrangeHRM website")
def openwebsite(context):
    service_obj = Service("C://Users//a778983//OneDrive - Eviden//Desktop//chromedriver-win64//chromedriver.exe")
    context.driver = webdriver.Chrome(service=service_obj)
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)



@When ("I enter {0} and {1} as a user and click login")
def Login(context, username, password):
    context.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(4)


@Then ("I verify if the user is successfully login or not")
def verify(context):
    check=context.driver.find_element(By.XPATH, "//span[text()='PIM']").is_displayed()
    if check == True:
        assert True
    else:
        assert False


@Then ("I click on PIM and add Employee")
def goto(context):
    context.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
    context.driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()
    time.sleep(4)


@Then ("I enter firstname {0} Middlename {1} Lastname {2} anc click save")
def adddetails(context,firstname,middlename,lastname):
    context.driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys(firstname)
    context.driver.find_element(By.XPATH, "//input[@name='middleName']").send_keys(middlename)
    context.driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys(lastname)
    context.driver.find_element(By.XPATH, "//button[text()=' Save ']").click()
    time.sleep(4)

