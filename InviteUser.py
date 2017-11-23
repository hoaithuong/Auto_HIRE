from Login import drive
import time

URL = "https://stg01.trinethire-ops.com/users/invitations"
NAME = "Hoai Thuong"
FEMAIL = "minhthuong"
LEMAIL = "@trinetqa.com"
PHONE = "435"
TITLE = "Admin"
OUTPUT = "C:\\Users\\Hoang\\PycharmProjects\\hireproject\\Screenshots\\"


def inviteuser(n=1):
    drive.get(URL)
    drive.implicitly_wait(20)

    drive.find_element_by_id("invite-user-button").click()
    time.sleep(0.5)

    drive.find_element_by_id("user_invitation_full_name").send_keys(NAME + ' ' + str(n).rjust(5, '0'))
    time.sleep(0.5)

    drive.find_element_by_id("user_invitation_email").send_keys(FEMAIL + str(n).rjust(5, '0') + LEMAIL)
    time.sleep(0.5)

    drive.find_element_by_id("user_invitation_phone").send_keys(PHONE + str(n).rjust(7, '0'))
    time.sleep(0.5)

    drive.find_element_by_id("user_invitation_title").send_keys(TITLE)
    time.sleep(0.5)

    drive.find_element_by_xpath('//span[contains(text(),"Admin")]').click()

    drive.find_element_by_class_name("btn-positive").click()
    time.sleep(0.5)

    #drive.get_screenshot_as_file(OUTPUT + 'Invite.png')

def invitemanyusres():
    for x in range (1, 5):
        inviteuser(x)
        drive.implicitly_wait(20)
