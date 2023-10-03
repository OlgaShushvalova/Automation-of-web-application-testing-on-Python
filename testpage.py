import time
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

ids = dict()
with open("./locators.yaml") as f:
    locators = yaml.safe_load(f)
for locator in locators["xpath"].keys():
    ids[locator] = (By.XPATH, locators["xpath"][locator])
for locator in locators["css"].keys():
    ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while opertion with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

# ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(ids["LOCATOR_LOGIN_FIELD"], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(ids["LOCATOR_PASS_FIELD"], word, description="password form")

    def add_title(self, word):
        self.enter_text_into_field(ids["LOCATOR_TITLE_POST"], word, description="title")

    def add_description(self, word):
        self.enter_text_into_field(ids["LOCATOR_DESCRIPTION_POST"], word, description="description")

    def add_content(self, word):
        self.enter_text_into_field(ids["LOCATOR_CONTENT_POST"], word, description="description")

    def add_name(self, word):
        self.enter_text_into_field(ids["LOCATOR_YOUR_NAME"], word, description="contact_name")

    def add_email(self, word):
        self.enter_text_into_field(ids["LOCATOR_YOUR_EMAIL"], word, description="contact_email")

    def add_contact_content(self, word):
        self.enter_text_into_field(ids["LOCATOR_CONTENT_FIELD"], word, description="contact_content")

# CLICK
    def click_login_button(self):
        self.click_button(ids["LOCATOR_LOGIN_BTN"], description="login")

    def click_add_post_button(self):
        self.click_button(ids["LOCATOR_ADD_POST"], description=" post")

    def click_save_button(self):
        self.click_button(ids["LOCATOR_SAVE_POST"], description="save")

    def click_contact_button(self):
        self.click_button(ids["LOCATOR_CONTACT"], description="send")

    def click_contact_us_button(self):
        self.click_button(ids["LOCATOR_CONTACT_BTN"], description="contact")

# GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(ids["LOCATOR_ERROR_FIELD"], description="error label")

    def login_success(self):
        return self.get_text_from_element(ids["LOCATOR_SUCCESS"], description="username")

    def find_new_post_title(self):
        return self.get_text_from_element(ids["LOCATOR_FIND_NEW_POST"], description="result")

    def get_alert_message(self):
        time.sleep(1)
        logging.info("Get alert message")
        txt = self.get_alert()
        logging.info(f"Alert message is {txt}")
        return txt
