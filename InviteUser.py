from Login import driver
import time

URL = "https://stg01.trinethire-ops.com/users/invitations"
NAME = "Hoai Thuong"
FEMAIL = "linhthuong"
LEMAIL = "@trinetqa.com"
PHONE = "435"
TITLE = "Admin"
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"

# Invite one User
def inviteuser(n=1):
    # get URL
    driver.get(URL)
    driver.implicitly_wait(20)

    # get id Invite New Team Member button
    driver.find_element_by_id("invite-user-button").click()
    time.sleep(0.5)

    # get id Full Name
    driver.find_element_by_id("user_invitation_full_name").send_keys(NAME + ' ' + str(n).rjust(5, '0'))
    time.sleep(0.5)

    # get id Email
    driver.find_element_by_id("user_invitation_email").send_keys(FEMAIL + str(n).rjust(5, '0') + LEMAIL)
    time.sleep(0.5)

    # get id Phone
    driver.find_element_by_id("user_invitation_phone").send_keys(PHONE + str(n).rjust(7, '0'))
    time.sleep(0.5)

    # get id Permission Level
    driver.find_element_by_id("user_invitation_title").send_keys(TITLE)
    time.sleep(0.5)

    # get xpath to click on Admin
    driver.find_element_by_xpath('//span[contains(text(),"Admin")]').click()

    # get class Invite button
    driver.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

    #driver.get_screenshot_as_file(OUTPUT + 'Invite.png')

# Invite many User
def invitemanyusres():
    for x in range (5, 10):
        inviteuser(x)
        driver.implicitly_wait(20)
