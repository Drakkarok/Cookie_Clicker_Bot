from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scraper:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def scrap_cookie_number(self):
        wait = WebDriverWait(self.driver, 1)
        entity = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='cookies']")))
        print(f'scrap_cookie_number: {float(entity.get_attribute("textContent").split()[0].replace(",", ""))}')
        return float(entity.get_attribute("textContent").split()[0].replace(",", ""))

    def scrap_cookie_per_second(self):
        wait = WebDriverWait(self.driver, 1)
        entity = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='cookies']")))
        print(f'scrap_cookie_per_second: {float(entity.get_attribute("textContent").split()[3].replace(",", ""))}')
        return float(entity.get_attribute("textContent").split()[3].replace(",", ""))

    def scrap_cost_of_cookie_producer(self, number_of_upgrade):
        wait = WebDriverWait(self.driver, 1)
        # entity = wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[@id='product{number_of_upgrade}']")))
        entity = wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[@id='productPrice{number_of_upgrade}']")))
        print(f'scrap_cost_of_cookie_producer {number_of_upgrade}: {float(entity.get_attribute("textContent").replace(",", ""))}')
        return float(entity.get_attribute("textContent").replace(",", ""))
