import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base


class MainPage(Base):

    url = 'https://www.citilink.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    catalog = '//a[@href="/catalog/smartfony/"]'



    #Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    # #Actions
    def click_catalog(self):
        self.get_catalog().click()
        print("Открыт выбор телефона")



    #Methods

    def open_catalog(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_catalog()
