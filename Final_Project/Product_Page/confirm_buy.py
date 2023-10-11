import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base


class ConfirmBuy(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    add_to_cart = '//button[@class="e11w80q30 e4uhfkv0 app-catalog-1lk9ql2 e4mggex0"]'
    move_to_cart = '//button[@class="e4uhfkv0 css-gh3izc e4mggex0"]'



    #Getters

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))
    def get_move_to_cart(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.move_to_cart)))

    # #Actions
    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Телефон в корзине")
    def click_move_to_cart(self):
        self.get_move_to_cart().click()
        print("Открыта корзина")



    #Methods

    def basket(self):

        self.click_add_to_cart()
        self.click_move_to_cart()
