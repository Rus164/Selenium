from selenium.webdriver.common.by import By


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get_current_url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Верный url " + get_url)

