from selenium import webdriver
from Login import drive
from datetime import datetime

URL = "https://stg01.trinethire-ops.com/admin/locations"
NAME = "US"
ADDRESS = "US"
CITY = "US"
STATE = "US"
COUNTRY = "US"
ZIP = "12345"
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"


def createlocation():
    drive.get(URL)
    drive.implicitly_wait(20)
    drive.find_element_by_id("add-location").click()
    drive.find_element_by_id("location_name").send_keys(NAME)
    drive.find_element_by_id("location_address").send_keys(ADDRESS)
    drive.find_element_by_id("location_city").send_keys(CITY)
    drive.find_element_by_id("location_state").send_keys(STATE)
    drive.find_element_by_id("location_country").send_keys(COUNTRY)
    drive.find_element_by_id("location_zip_code").send_keys(ZIP)
    drive.find_element_by_class_name("btn-positive").click()
    drive.get_screenshot_as_file(OUTPUT + 'Location.png')

def createfive():
    for x in range(0, 4):
        createlocation()
        drive.implicitly_wait(1)