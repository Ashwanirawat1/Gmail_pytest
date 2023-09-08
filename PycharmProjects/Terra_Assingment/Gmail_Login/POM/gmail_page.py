import time
from Data.ExcelLib import read_locators
from Library.selenium_wrapper import SeleniumWrapper
from selenium.webdriver.common.keys import Keys


class Gmail(SeleniumWrapper):

    def __init__(self, driver):
        super().__init__(driver)

    locators = read_locators('Gmail')

    #  This method is used to check for visibility of element
    def check_visible_gmail_page(self):
        time.sleep(2)
        gmail_page = Gmail.locators['_verify_email_page']
        self.wait_till(gmail_page)

    # This method is used to get object on homepage
    def get_sign_in_text(self):
        sign_in = Gmail.locators['_verify_email_page']
        return self.get_text_from_element(sign_in)

    # This method is used to enter text in Email textbox
    def enter_email(self, value):
        _enter_email = Gmail.locators['_email']
        self.enter_element(_enter_email, value)
        time.sleep(1)

    # This method is used to click on Next Button
    def click_next_button(self):
        _next = Gmail.locators['_next_button']
        self.click_element(_next)
        time.sleep(3)

    # This method is used to get text of Entered Email
    def get_entered_email_text(self):
        email_text = Gmail.locators['_verify_entered_email']
        return self.get_text_from_element(email_text)

    # This method is used to enter text in Email textbox
    def enter_password(self, value):
        _enter_password = Gmail.locators['_password']
        self.enter_element(_enter_password, value)
        time.sleep(1)

    # This method is used to check for visibility of element
    def check_visible_compose(self):
        time.sleep(2)
        compose = Gmail.locators['_verify_compose']
        self.wait_till(compose)

    # This method is used to get object on gmail page
    def get_compose_text(self):
        compose_text = Gmail.locators['_verify_compose']
        return self.get_text_from_element(compose_text)

    # This method is used to move mouse to profile
    def move_mouse_to_profile(self):
        profile = Gmail.locators['_go_to_profile']
        self.move_mouse(profile)
        time.sleep(2)

    # This method is used to get entered gmail from page
    def get_email_text_from_home_page(self):
        home_page_email_text = Gmail.locators['_get_email_text']
        return self.get_text_from_element(home_page_email_text)

    def get_wrong_password_text(self):
        wrong_password = Gmail.locators['_wrong_password_text']
        return self.get_text_from_element(wrong_password)

    def click_profile(self):
        profile_ = Gmail.locators['_go_to_profile']
        self.click_element(profile_)
        time.sleep(2)

    def switch_iframe(self):
        frame_ = Gmail.locators['_iframe']
        self.switch_to_frame_(frame_)

    def move_sign_out(self):
        sign_out = Gmail.locators['_sign_out']
        self.move_mouse(sign_out)

    def click_sign_out(self):
        sign_out = Gmail.locators['_sign_out']
        self.click_element(sign_out)

    def switch_frame(self):
        frame = Gmail.locators['_frame']
        self.switch_to_frame_(frame)
        time.sleep(2)

    def click_view_box(self):
        box = Gmail.locators['_view_box']
        self.click_element(box)

    def click_drive(self):
        drive = Gmail.locators['_drive']
        self.click_element(drive)
        time.sleep(2)

    def click_new(self):
        new = Gmail.locators['_new']
        self.click_element(new)
        time.sleep(5)

    def click_compose(self):
        compose = Gmail.locators['_verify_compose']
        self.click_element(compose)
        time.sleep(2)

    def enter_to(self, value):

        to = Gmail.locators['_to']
        self.enter_element(to, value+Keys.TAB)
        time.sleep(1)



    def enter_subject(self, value):
        subject = Gmail.locators['_subject']
        self.enter_element(subject, value)
        time.sleep(2)

    def enter_write_pad(self, value):
        write_pad = Gmail.locators['_write_pad']
        self.enter_element(write_pad, value)
        time.sleep(1)

    def click_send(self):
        send = Gmail.locators['_send_button']
        self.click_element(send)
        time.sleep(2)


