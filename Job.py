from Login import driver
import time

URL = "https://stg01.trinethire-ops.com/jobs/new"
NAME = "JOB"
DESCRIPTION = "JOB"
SALARY = "12"
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

# Create one Job
def createjob(n=1):
    driver.get(URL)
    driver.implicitly_wait(20)

    driver.find_element_by_id("job_name").send_keys(NAME+ ' ' + str(n).rjust(5, '0'))
    time.sleep(0.5)

    driver.find_element_by_id("job_num_openings_chosen").click()
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys('\t')
    time.sleep(0.5)

    driver.find_element_by_id("job_employment_type_chosen").click()
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys('\t')
    time.sleep(0.5)

    driver.find_element_by_class_name("note-editable").send_keys(DESCRIPTION)
    time.sleep(0.5)

    driver.execute_script("window.scrollTo(0, 750)")
    time.sleep(0.5)

    driver.find_element_by_id("job_location_chosen").click()
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys('\t')
    time.sleep(0.5)

    driver.find_element_by_id("job_experience_chosen").click()
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys('\t')
    time.sleep(0.5)

    driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(0.5)

    driver.find_element_by_id("job_user_id_chosen").click()
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys('\t')
    time.sleep(0.5)

    driver.find_element_by_id("job_min_salary").send_keys(SALARY)
    time.sleep(0.5)

    driver.find_element_by_class_name("create-job").click()
    time.sleep(0.5)

    #driver.get_screenshot_as_file(OUTPUT + 'Job.png')

# Create many Jobs
def createmanyjob():
    for x in range (5, 10):
        createjob(x)
        driver.implicitly_wait(20)
