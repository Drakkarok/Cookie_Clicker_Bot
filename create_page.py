from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class CreatePage:
    def __init__(self, url_of_game):
        self.driver = None
        self.chrome_options = Options()
        self.service_for_chrome = Service()

        self.change_chrome_options()
        self.initialize_webdriver()
        self.open_specified_page(url_of_game)
        self.maxime_window()

    def change_chrome_options(self):
        self.chrome_options.add_experimental_option("detach", True)

    def initialize_webdriver(self):
        self.driver = webdriver.Chrome(service=self.service_for_chrome, options=self.chrome_options)

    def open_specified_page(self, url_of_game):
        self.driver.get(url_of_game)

    def maxime_window(self):
        self.driver.maximize_window()


