import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Filter_Product.choise_telephone import ChoisePhone
from Main_Page.main_Page import MainPage
from Product_Page.confirm_buy import ConfirmBuy


def test_select_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('D:\python\pythonSelenium\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print("Начало")

    enter_catalog = MainPage(driver)
    enter_catalog.open_catalog()

    phone = ChoisePhone(driver)
    phone.choise()

    cart = ConfirmBuy(driver)
    cart.basket()