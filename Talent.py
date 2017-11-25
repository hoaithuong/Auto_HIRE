from Login import driver
import time

URL = "https://stg01.trinethire-ops.com/applications/new"
FNAME = "Hoai"
LNAME = "Thuong"
FEMAIL = "kindthuong"
LEMAIL = "@trinetqa.com"
PHONE = "435"
TITLE = "Admin"
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

# Invite one Talent
def createtalent(n=1):
    driver.get(URL)
    driver.implicitly_wait(20)

    driver.find_element_by_id("application_first_name").send_keys(FNAME)
    time.sleep(0.5)

    driver.find_element_by_id("application_last_name").send_keys(LNAME + ' ' + str(n).rjust(5, '0'))
    time.sleep(0.5)

    driver.find_element_by_id("application_email").send_keys(FEMAIL + str(n).rjust(5, '0') + LEMAIL)
    time.sleep(0.5)

    driver.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

    #driver.get_screenshot_as_file(OUTPUT + 'Talent.png')

# Invite many Talents
def createmanytalents():
    for x in range (5, 10):
        createtalent(x)
        driver.implicitly_wait(20)
