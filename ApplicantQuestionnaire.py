from Login import driver
import time

URL = "https://stg01.trinethire-ops.com/admin/questionnaires/new"
NAME = "Applicant Questionnaire "
QUESTIONNAME = "Question 1"
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

def createquestionnaires(n=1):
    # get URL
    driver.get(URL)
    driver.implicitly_wait(20)

    # get id NEW QUESTIONNAIRE NAME
    driver.find_element_by_id("questionnaire_name").send_keys(NAME + str(n).rjust(5, '0'))
    time.sleep(0.5)

    # get class Select Question Type
    driver.find_element_by_xpath('//*[@id="question_type_chosen"]').click()
    time.sleep(0.5)
    driver.switch_to.active_element.send_keys('\t')
    time.sleep(0.5)

    # get class Question name for item 1
    driver.find_element_by_xpath('//*[@id="questions"]/div/div/input[1]').send_keys(QUESTIONNAME)
    time.sleep(0.5)

    # get id Submit button
    driver.find_element_by_id("submitBtn").click()
    time.sleep(0.5)
