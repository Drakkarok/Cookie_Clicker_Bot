from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class Clicker:
    def __init__(self, time_to_wait, driver: webdriver.Chrome):
        self.driver = driver
        self.click_for_gdpr()
        self.click_got_it()
        self.click_for_language(time_to_wait)

# ---------------------------------------------------------------------------------- START-UP

    def click_got_it(self):
        wait = WebDriverWait(self.driver, 1)
        entity = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/a[1]")))
        entity.click()

    def click_for_gdpr(self):
        wait = WebDriverWait(self.driver, 1)
        entity = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
        entity.click()

    def click_for_language(self, time_to_wait_from_main):
        wait = WebDriverWait(self.driver, 1)
        entity = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[12]/div/div[1]/div[1]/div[2]")))
        entity.click()
        time.sleep(time_to_wait_from_main)

    def click_on_cookie(self):
        entity = self.driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
        entity.click()

# ---------------------------------------------------------------------------------- COOKIE PRODUCERS

    def click_on_cookie_producer(self, nr_upgrade):
        print(f'upgraded: {nr_upgrade}')
        # self.driver.find_element(By.XPATH, f'//*[@id="product{nr_upgrade}"]').click()
        wait = WebDriverWait(self.driver, 0.5)
        entity = wait.until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="product{nr_upgrade}"]')))
        entity.click()

# ---------------------------------------------------------------------------------- UPGRADES

    def click_on_upgrade(self):
        entity = self.driver.find_element(By.XPATH, '//*[@id="upgrade0"]')
        entity.click()
