# @Time    : 2019/12/12 10:15
# @Author  : Hugh
# @email   : 609799548@qq.com

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Base:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def finds(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))

    def send(self, locator, text, timeout=10):
        self.find(locator, timeout).send_keys(text)

    def click(self, locator, timeout=10):
        self.find(locator, timeout).click()

    def clear(self, locator, timeout=10):
        self.find(locator, timeout).clear()

    def get_text(self, locator, timeout=10):
        return self.find(locator, timeout).text

    def get_alert_text(self, opt='accept', timeout=10):
        a = WebDriverWait(self.driver, timeout).until(expected_conditions.alert_is_present())
        t = a.text
        if opt == 'accept':
            a.accept()
        else:
            pass
        return t

    def is_element_exist(self, locator, timeout):
        try:
            self.find(locator, timeout)
            return True
        except Exception as e:
            print('e----->', e)
            return False

    def move_to_element(self, locator, timeout=10):
        e = self.find(locator, timeout)
        ActionChains(self.driver).move_to_element(e).perform()

