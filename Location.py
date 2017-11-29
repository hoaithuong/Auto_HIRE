from Login import driver
import time

URL = "https://stg01.trinethire-ops.com/admin/locations"
NAME = "TQ"
ADDRESS = "US"
CITY = "US"
STATE = "US"
COUNTRY = "US"
ZIP = "12345"
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

# Create one Location
def createlocation(n=1):
    driver.get(URL)
    driver.implicitly_wait(20)

    driver.find_element_by_id("add-location").click()
    time.sleep(0.5)

    driver.find_element_by_id("location_name").send_keys(NAME+ ' ' + str(n).rjust(5, '0'))
    time.sleep(0.5)

    driver.find_element_by_id("location_address").send_keys(ADDRESS)
    time.sleep(0.5)

    driver.find_element_by_id("location_city").send_keys(CITY)
    time.sleep(0.5)

    driver.find_element_by_id("location_state").send_keys(STATE)
    time.sleep(0.5)

    driver.find_element_by_id("location_country").send_keys(COUNTRY)
    time.sleep(0.5)

    driver.find_element_by_id("location_zip_code").send_keys(ZIP)
    time.sleep(0.5)

    driver.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

    #drive.get_screenshot_as_file(OUTPUT + 'Location.png')

# Update a location
def updatelocation(n=1):
    driver.get(URL)
    driver.implicitly_wait(20)

    driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div/table/tbody/tr[1]/td[8]/div/a[1]').click()
    time.sleep(0.5)

    driver.find_element_by_id('location_name').clear()
    time.sleep(0.5)
    driver.find_element_by_id("location_name").send_keys(NAME+ ' ' + str(n).rjust(7, '0'))
    time.sleep(0.5)

    driver.find_element_by_id('location_address').clear()
    time.sleep(0.5)
    driver.find_element_by_id("location_address").send_keys(ADDRESS)
    time.sleep(0.5)

    driver.find_element_by_id('location_city').clear()
    time.sleep(0.5)
    driver.find_element_by_id("location_city").send_keys(CITY)
    time.sleep(0.5)

    driver.find_element_by_id('location_state').clear()
    time.sleep(0.5)
    driver.find_element_by_id("location_state").send_keys(STATE)
    time.sleep(0.5)

    driver.find_element_by_id('location_country').clear()
    time.sleep(0.5)
    driver.find_element_by_id("location_country").send_keys(COUNTRY)
    time.sleep(0.5)

    driver.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

# Create many Locations
def createmanylocations():
    for x in range(5, 10):
        createlocation(x)
        driver.implicitly_wait(1)
