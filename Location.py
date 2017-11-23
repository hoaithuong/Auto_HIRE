from Login import drive
import time

URL = "https://stg01.trinethire-ops.com/admin/locations"
NAME = "VN"
ADDRESS = "US"
CITY = "US"
STATE = "US"
COUNTRY = "US"
ZIP = "12345"
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"


def createlocation(n=1):
    drive.get(URL)
    drive.implicitly_wait(20)

    drive.find_element_by_id("add-location").click()
    time.sleep(0.5)

    drive.find_element_by_id("location_name").send_keys(NAME+ ' ' + str(n).rjust(5, '0'))
    time.sleep(0.5)

    drive.find_element_by_id("location_address").send_keys(ADDRESS)
    time.sleep(0.5)

    drive.find_element_by_id("location_city").send_keys(CITY)
    time.sleep(0.5)

    drive.find_element_by_id("location_state").send_keys(STATE)
    time.sleep(0.5)

    drive.find_element_by_id("location_country").send_keys(COUNTRY)
    time.sleep(0.5)

    drive.find_element_by_id("location_zip_code").send_keys(ZIP)
    time.sleep(0.5)

    drive.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

    #drive.get_screenshot_as_file(OUTPUT + 'Location.png')

def createmanylocations():
    for x in range(1, 5):
        createlocation(x)
        drive.implicitly_wait(1)
