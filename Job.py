from Login import drive
from selenium.webdriver.common.keys import Keys
import time

URL = "https://stg01.trinethire-ops.com/jobs/opens"
NAME = "JOB"
DESCRIPTION = "JOB"
SALARY = "12"
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"


def createjob(n=1):
    drive.get(URL)
    drive.implicitly_wait(20)

    drive.find_element_by_id("add-job").click()
    time.sleep(1)

    drive.find_element_by_id("job_name").send_keys(NAME+ ' ' + str(n).rjust(5, '0'))
    time.sleep(1)

    drive.find_element_by_id("job_num_openings_chosen").click()
    time.sleep(1)
    drive.find_element_by_xpath('//span[contains(text(),"3")]').click()
    time.sleep(1)

    drive.find_element_by_id("job_priority_chosen").click()
    time.sleep(1)
    drive.find_element_by_id("job_priority_chosen").send_keys(Keys.TAB)
    time.sleep(1)

    drive.find_element_by_class_name("note-editable").send_keys(DESCRIPTION)
    time.sleep(1)

    drive.find_element_by_id("job_location_chosen").click()
    time.sleep(1)
    drive.find_element_by_id("job_location_chosen").send_keys(Keys.TAB)
    time.sleep(1)

    drive.find_element_by_id("job_experience_chosen").click()
    time.sleep(1)
    drive.find_element_by_id("job_experience_chosen").send_keys(Keys.TAB)
    time.sleep(1)

    drive.find_element_by_id("job_user_id_chosen").click()
    time.sleep(1)
    drive.find_element_by_id("job_user_id_chosen").send_keys(Keys.TAB)
    time.sleep(1)

    drive.find_element_by_id("job_min_salary").send_keys(SALARY)
    time.sleep(1)

    drive.find_element_by_class_name("create-job").click()
    time.sleep(1)

    #drive.get_screenshot_as_file(OUTPUT + 'Job.png')