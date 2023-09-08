import logging
import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


# Generic Functions
class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    # Generic method is used to click an element
    def click_element(self, element):
        self.driver.find_element(element[0], element[1]).click()
        logging.info("Clicked on")

    # Generic method is used to enter an element
    def enter_element(self, element, text):
        self.driver.find_element(element[0], element[1]).send_keys(text)

    # Generic method is used to get text from element
    def get_text_from_element(self, element):
        object_ = self.driver.find_element(element[0], element[1])
        return object_.text

    # Generic method is used to get text from multiple elements
    def get_text_from_multiple_elements(self, element):
        objects = self.driver.find_elements(element[0], element[1])
        # for obj in objects:
        return objects

    # Generic method is used to take data from table
    def get_table_data(self, element):
        rows = self.driver.find_elements(element[0], element[1])
        table_data = []
        for row in rows:
            table_data.append(row.text)
        return table_data

    # Generic method is used to move mouse to specifics module
    def move_mouse(self, element):
        action = ActionChains(self.driver)
        target = self.driver.find_element(element[0], element[1])
        action.move_to_element(target).perform()
        time.sleep(2)

    # Generic method is used to drag element to specifics target element
    def drag_and_drop(self, source, target):
        source = self.driver.find_element(source[0], source[1])
        target = self.driver.find_element(target[0], target[1])
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()
        time.sleep(4)

    # Generic method is used to switch to iframe
    def switch_to_frame_(self, element):
        iframe = self.driver.find_element(element[0], element[1])
        self.driver.switch_to.frame(iframe)
        time.sleep(2)

    # Generic method is used to handle windows
    def switch_to_window_handles(self, value):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[value])

    # Generic method is used for select item
    def select_element(self, element, item=None):
        element = self.driver.find_element(element[0], element[1])
        s = Select(element)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            raise Exception

    # Generic method is used for select item
    def find_month_date(self, element):
        self.driver.find_element(element[0], element[1])

    # Generic method is used to check visibility of element
    def wait_till(self, element):
        wait = WebDriverWait(self.driver, timeout=15)
        if wait.until(visibility_of_element_located((element[0], element[1]))):
            return
        else:
            raise NoSuchElementException
