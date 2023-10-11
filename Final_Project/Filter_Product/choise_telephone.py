import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_class import Base

class ChoisePhone(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(driver)


    # Locators

    check_box = "//input[contains(@id,'available.all')]"
    price = '//div[@class="rc-slider-handle rc-slider-handle-2"]'
    rb_feedback = '//input[@name="rating.4.5"]'
    memory_phone = "//input[@id='23178_214256d1gb']"
    internet = "//div[@data-meta-value = 'Интернет']"
    technology_5g = "//input[@id='12499_214']"
    filter_by_price = "//button[@data-meta-value = 'price']"
    phone = "//a[@class='app-catalog-9gnskf e1259i3g0']"
    model = "//input[@id='samsung']"

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, 500);")

    def scroll2(self):
        self.driver.execute_script("window.scrollTo(0, 900);")

    def scroll3(self):
        self.driver.execute_script("window.scrollTo(0, 1600);")

    def scroll4(self):
        self.driver.execute_script("window.scrollTo(0, 2500);")

    def scroll5(self):
        self.driver.execute_script("window.scrollTo(0, 0);")



    # Getters

    def get_check_box(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.check_box)))

    def get_rb_feedback(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.rb_feedback)))
    def get_model(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.model)))


    def get_memory_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.memory_phone)))

    def get_internet(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.internet)))

    def get_technology_5g(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.technology_5g)))

    def get_filter_by_price(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.filter_by_price)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.phone)))

    # def price_choice(self):
    #     return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    # Actions

    def click_check_box(self):
        self.get_check_box().click()
        print("Выбран чек бокс 'Доступен самовывоз'")

    def click_rb_feedback(self):
        self.get_rb_feedback().click()
        print("Выбран фильтр по отзывам")
    def click_model(self):
        self.get_model().click()
        print("Выбрана модель модель Samsung")

    def click_memory_phone(self):
        self.get_memory_phone().click()
        print("Выбран фильтр по памяти")

    def click_internet_phone(self):
        self.get_internet().click()
        print("Выбор сети")

    def click_technology_5g(self):
        self.get_technology_5g().click()
        print("Выбор сети 5G")

    def click_filter_by_price(self):
        self.get_filter_by_price().click()
        print("Фильтр цены")

    def click_phone(self):
        self.get_phone().click()
        print("Выбран телефон")
    # def click_price(self):
    #     self.price_choice().click_and_hold(self.price_choice).move_by_offset(-100, 0).release().perform()


    # Methods

    def choise(self):
        self.scroll()
        self.click_check_box()
        self.scroll2()
        self.click_rb_feedback()
        self.scroll3()
        self.click_model()
        self.click_memory_phone()
        self.scroll4()
        self.click_internet_phone()
        self.click_technology_5g()
        self.scroll5()
        self.click_filter_by_price()
        self.click_filter_by_price()
        self.click_phone()
