from Login import driver
import time

URL = "https://stg01.trinethire-ops.com/calendar"
NAME = "Event "
REGARDINGCANDIDATE = 'th'
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

# Invite one Event
def createevent(n=1):
    driver.get(URL)
    driver.implicitly_wait(20)

    driver.find_element_by_id("scheduleEvent").click()
    time.sleep(0.5)

    driver.find_element_by_id("event_name").send_keys(NAME + str(n).rjust(5, '0'))
    time.sleep(0.5)

    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(0.5)

    driver.find_element_by_id("event_application_id").send_keys(REGARDINGCANDIDATE)
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="new_event"]/div[1]/ul/li[5]/div/span/div/div/div[1]').click()
    time.sleep(0.5)

    driver.find_element_by_id("event_job_chosen").click()
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys('\t')
    time.sleep(0.5)

    driver.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

    #driver.get_screenshot_as_file(OUTPUT + 'Event.png')

# Invite many Events
def createmanyevents():
    for x in range (5, 10):
        createevent(x)
        driver.implicitly_wait(20)
