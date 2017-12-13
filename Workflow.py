from Login import driver
import time

URL = "https://stg01.trinethire-ops.com/admin/workflows/new"
NAME = "Workflow "
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

def createworkflow(n=1):
    # get URL
    driver.get(URL)
    driver.implicitly_wait(20)

    # get id Workflow Name
    driver.find_element_by_id("workflow_name").send_keys(NAME + str(n).rjust(5, '0'))
    time.sleep(0.5)

    # get class Create New Workflow button
    driver.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

    # get class Add a Step button
    driver.find_element_by_class_name("add-a-step").click()
    time.sleep(0.5)

    # get class Not Hired Statuses
    driver.find_element_by_class_name("not-hired-status").click()
    time.sleep(0.5)

    # get class Hired Statuses
    driver.find_element_by_class_name("hired-status").click()
    time.sleep(0.5)

