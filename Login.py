from selenium import webdriver

CHROMEDRIVER = "D:\\Data - Thuong\\AUTO\\SELENIUM\\chromedriver_win32\\chromedriver.exe"
#CHROMEDRIVER = "D:\\Selenium\\chromedriver.exe"

URL = 'https://stg01.trinethire-ops.com/users/sign_in'
USERNAME = 'thuongtest100@trinetqa.com'
PASSWORD = '12345!@#$%'
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

driver = webdriver.Chrome(CHROMEDRIVER)
driver.maximize_window()
driver.set_page_load_timeout(30)

def login():
    driver.get(URL)
    driver.implicitly_wait(20)
    driver.find_element_by_id("user_email").send_keys(USERNAME)
    driver.find_element_by_id("user_password").send_keys(PASSWORD)
    driver.find_element_by_id("login_submit").click()
    #driver.get_screenshot_as_file(OUTPUT + 'Hire.png')

