from Login import driver
import time

URL = "https://stg01.trinethire-ops.com/admin/email_templates/new"
NAME = "Template "
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

def createtemplate(n=1):
    # get URL
    driver.get(URL)
    driver.implicitly_wait(20)

    # get id Template Name
    driver.find_element_by_id("add_email_template_name").send_keys(NAME + str(n).rjust(5, '0'))
    time.sleep(0.5)

    # get id IMPORT EXISTING TEMPLATE
    driver.find_element_by_id("template_copy_select_chosen").click()
    time.sleep(0.5)

    # get Xpath item 3
    driver.find_element_by_xpath('//*[@id="template_copy_select_chosen"]/div/ul/li[4]').click()
    time.sleep(0.5)

    # get id Save Template button
    driver.find_element_by_id("save-template").click()
    time.sleep(0.5)
