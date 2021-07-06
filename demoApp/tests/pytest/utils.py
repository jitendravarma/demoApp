import re
import time
import requests

from selenium.webdriver.common.keys import Keys

BASE_URL = "http://127.0.0.1:8000"


class Utils():
    # base class for all test classes, cutomize and add func as required

    def login(self, user_name, password):
        """
        logout user and login back again
        """
        self.driver.get(BASE_URL + '/logout/')
        self.driver.find_element_by_name("email").click()
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys(user_name)
        self.driver.find_element_by_name("password").click()
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("password").send_keys(Keys.ENTER)

    def page_contains(self, content):
        """
        find a given text in a page and assert True if its present, else fail it
        """
        source = self.driver.page_source
        text_found = re.search(rf'\b{content}\b', source)
        return text_found

    def crashes(self, URL):
        """
        use this to check if url doesnt crashes, should give 200 status code,
        other wise fail it
        """
        self.driver.get(URL)
        status = requests.get(URL)
        return status.status_code

    def get_text_by_attribute(self, _id=None, _class=None, name=None):
        """
        use this function to find HTML elements by id, class or name attribute
        """
        if _id:
            return self.driver.find_element_by_id(_id)
        elif _class:
            return self.driver.find_elements_by_class_name(_class)
        else:
            return self.driver.find_element_by_name(name)

    def fill_element_by_attribute(self, _input, _id=None, _class=None, name=None):
        """
        use this function to fill HTML elements by id, class or name attribute
        eg: any input tag by id or whatever
        """
        if _id:
            return self.driver.find_element_by_id(_id).send_keys(_input)
        elif _class:
            return self.driver.find_element_by_class_name(_class).send_keys(_input)
        else:
            return self.driver.find_element_by_name(name).send_keys(_input)

    def click_by_attribute(self, _input, _id=None, _class=None):
        """
        Use this function to immetate click event on HTML element by id or class
        attribute eg: any input tag by id or whatever
        """
        if _id:
            return self.driver.find_element_by_id(_id).click()
        elif _class:
            return self.driver.find_element_by_class_name(_class).click()
