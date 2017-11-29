from Login import driver
import time

URL = "https://stg01.trinethire-ops.com/tasks"
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

# Invite one Task
def createtask(n=1):
    driver.get(URL)
    driver.implicitly_wait(20)

    driver.find_element_by_id("new-task-button").click()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="new_task"]/ul/li[1]/div/a').click()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="new_task"]/ul/li[1]/div/div/ul/li[3]').click()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="task_user_id_chosen"]/a').click()
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys('\t')
    time.sleep(0.5)

    driver.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

    #driver.get_screenshot_as_file(OUTPUT + 'Task.png')

# Update a Task
def updatetask(n=1):
    driver.get(URL)
    driver.implicitly_wait(20)

    driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div/div[1]/table/tbody/tr[1]/td[6]/div/a[1]').click()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="edit_task_2112"]/ul/li[1]/div/a/div').click()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="edit_task_2112"]/ul/li[1]/div/div/ul/li[5]').click()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="task_user_id_chosen"]/a').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="task_user_id_chosen"]/div/ul/li[2]').click()
    time.sleep(0.5)

    driver.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

# Invite many Tasks
def createmanytasks():
    for x in range (5, 10):
        createtask(x)
        driver.implicitly_wait(20)
