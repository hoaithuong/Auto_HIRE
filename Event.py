from Login import driver
import time

URL = "https://stg01.trinethire-ops.com/calendar"
NAME = "Event "
REGARDINGCANDIDATE = 'th'
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

# Invite one Event
def createevent(n=1):
    # get URL
    driver.get(URL)
    driver.implicitly_wait(20)

    # get id Schedule button
    driver.find_element_by_id("scheduleEvent").click()
    time.sleep(0.5)

    # get id and send the Event Name
    driver.find_element_by_id("event_name").send_keys(NAME + str(n).rjust(5, '0'))
    time.sleep(0.5)

    # Scroll to down
    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(0.5)

    # get id Regarding Candidate and select an item
    driver.find_element_by_id("event_application_id").send_keys(REGARDINGCANDIDATE)
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="new_event"]/div[1]/ul/li[5]/div/span/div/div/div[1]').click()
    time.sleep(0.5)

    # get id Regarding Job and select the first item
    driver.find_element_by_id("event_job_chosen").click()
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys('\t')
    time.sleep(0.5)

    # get class Save button
    driver.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

    # Screenshot the picture
    #driver.get_screenshot_as_file(OUTPUT + 'Event.png')

# Update an Event
def updateevent(n=1):
    # get URL
    driver.get(URL)
    driver.implicitly_wait(20)

    # get id Schedule Event button
    driver.find_element_by_id("scheduleEvent").click()
    time.sleep(0.5)

    # get id and send the Event Name
    driver.find_element_by_id("event_name").send_keys(NAME + str(n).rjust(5, '0'))
    time.sleep(0.5)

    # Scroll to down
    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(0.5)

    # get id Regarding Candidate and select an item
    driver.find_element_by_id("event_application_id").send_keys(REGARDINGCANDIDATE)
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="new_event"]/div[1]/ul/li[5]/div/span/div/div/div[1]').click()
    time.sleep(0.5)

    # get id Regarding Job and select the first item
    driver.find_element_by_id("event_job_chosen").click()
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys('\t')
    time.sleep(0.5)

    # get class Save button
    driver.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

# Invite many Events
def createmanyevents():
    for x in range (5, 10):
        createevent(x)
        driver.implicitly_wait(20)
