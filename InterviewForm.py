from Login import driver
import time

URL = "https://stg01.trinethire-ops.com/admin/interview_forms/new"
NAME = "Interview "
QUESTION1 = "Question 1"
ANSWER1 = "Answer 1"
QUESTION2 = "Question 2"
ANSWER2 = "Answer 2"
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

def createinterview(n=1):
    # get URL
    driver.get(URL)
    driver.implicitly_wait(20)

    # get class LINK THESE QUESTIONS TO A JOB
    driver.find_element_by_class_name("search-field").click()
    time.sleep(0.5)

    # get Xpath item 2
    driver.find_element_by_xpath('//*[@id="jobs_id_list_chosen"]/div/ul/li[2]').click()
    time.sleep(0.5)

    # get id Interview Name
    driver.find_element_by_id("new_interview_form_name").send_keys(NAME + str(n).rjust(5, '0'))
    time.sleep(0.5)

    # get Xpath Question 1
    driver.find_element_by_xpath('//*[@id="questions"]/div/div/input[1]').send_keys(QUESTION1)
    time.sleep(0.5)

    # get Xpath Answer 1
    driver.find_element_by_xpath('//*[@id="questions"]/div/div/textarea').send_keys(ANSWER1)
    time.sleep(0.5)

    # get id Add Question button
    driver.find_element_by_id("add-question").click()
    time.sleep(0.5)

    # get Xpath Question 2
    driver.find_element_by_xpath('//*[@id="questions"]/div[2]/div/input[1]').send_keys(QUESTION2)
    time.sleep(0.5)

    # get Xpath Answer 2
    driver.find_element_by_xpath('//*[@id="questions"]/div[2]/div/textarea').send_keys(ANSWER2)
    time.sleep(0.5)

    # get class Create Interview form
    driver.find_element_by_class_name("submit-interview-form").click()
    time.sleep(0.5)
