from selenium import webdriver
import time

# Get URL's Lcation
# CHROMEDRIVER = "D:\\Data - Thuong\\AUTO\\SELENIUM\\chromedriver_win32\\chromedriver.exe"
CHROMEDRIVER = "D:\\Selenium\\chromedriver.exe"

URL = 'https://stg01.trinethire-ops.com/users/sign_in'
USERNAME = 'hi1+thuong+28dec@trinetqa.com'
PASSWORD = '12345!@#$%'
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

# driver is Chrome
driver = webdriver.Chrome(CHROMEDRIVER)

# open with maximize window
driver.maximize_window()
driver.set_page_load_timeout(30)

# Login function
def login():
    # get URL
    driver.get(URL)
    driver.implicitly_wait(20)

    # get id Email
    driver.find_element_by_id("user_email").send_keys(USERNAME)
    time.sleep(0.5)

    # get id Password
    driver.find_element_by_id("user_password").send_keys(PASSWORD)
    time.sleep(0.5)

    # get id Login button
    driver.find_element_by_id("login_submit").click()
    time.sleep(0.5)

    # Screenshot a picture
    #driver.get_screenshot_as_file(OUTPUT + 'Hire.png')

