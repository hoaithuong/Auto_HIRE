from Login import driver
import time

URL = "https://stg01.trinethire-ops.com/applications/new"
TALENTURL = "https://stg01.trinethire-ops.com/talent_pools"
FNAME = "Hoai"
LNAME = "Thuong"
FEMAIL = "antitythuong+b"
LEMAIL = "@trinetqa.com"
PHONE = "435"
TITLE = "Admin"
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

# Invite one Talent
def createtalent(n=1):
    # get URL
    driver.get(URL)
    driver.implicitly_wait(20)

    # get id First Name
    driver.find_element_by_id("application_first_name").send_keys(FNAME)
    time.sleep(0.5)

    # get id Last Name
    driver.find_element_by_id("application_last_name").send_keys(LNAME + ' ' + str(n).rjust(5, '0'))
    time.sleep(0.5)

    # get id Email
    driver.find_element_by_id("application_email").send_keys(FEMAIL + str(n).rjust(5, '0') + LEMAIL)
    time.sleep(0.5)

    # get class Add Talent button
    driver.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

    # Screenshot a picture
    #driver.get_screenshot_as_file(OUTPUT + 'Talent.png')

# Update a Talent
def updatetalent(n=1):
    # get URL of Talent
    driver.get(TALENTURL)
    driver.implicitly_wait(20)

    # get xpath to open a talent
    driver.find_element_by_xpath('//*[@id="tv-name-view"]/div[1]/div/table/tbody/tr[1]/td[1]/div/div[2]/div/a').click()
    time.sleep(0.5)

    # get xpath to go to Profile tab
    driver.find_element_by_xpath('//*[@id="candidateDetail"]/div[1]/div/div[2]/ul[2]/li[3]/a').click()
    time.sleep(0.5)

    # get class Edit all button
    driver.find_element_by_class_name('btn-edit-profile').click()
    time.sleep(0.5)

    # get id First Name
    driver.find_element_by_id('application_first_name').clear()
    time.sleep(0.5)
    driver.find_element_by_id("application_first_name").send_keys(FNAME)
    time.sleep(0.5)

    # get id Last Name
    driver.find_element_by_id("application_last_name").clear()
    time.sleep(0.5)
    driver.find_element_by_id("application_last_name").send_keys(LNAME + ' ' + str(n).rjust(7, '0'))
    time.sleep(0.5)

    # get id Email
    driver.find_element_by_id('application_email').clear()
    time.sleep(0.5)
    driver.find_element_by_id("application_email").send_keys(FEMAIL + str(n).rjust(7, '0') + LEMAIL)
    time.sleep(0.5)

    # get class Save button
    driver.find_element_by_class_name('btn-done-editing-profile').click()
    time.sleep(0.5)

# Invite many Talents
def createmanytalents():
    for x in range (1, 5):
        createtalent(x)
        driver.implicitly_wait(20)
