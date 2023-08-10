from scraper import Scraper
from clicker import Clicker
import json
import sys
import os


class Brain:
    def __init__(self, scraper: Scraper, clicker: Clicker):
        self.scraper = scraper
        self.clicker = clicker
        self.upgrade_list = ["cursor", "grandam", "farm", "mine", "factory", "bank"]
        self.upgrade_power_cost = [100, 500, 1000, 11000, 55000, 120000]
        self.current_file = "data.json.txt"
        self.content_current_file = {}
        self.brain_to_not_stop = True

        self.delete_old_json()
        self.create_json()
        self.read_from_json()
        self.get_some_cookies()
        self.calculate_what_upgrade()

    def calculate_what_upgrade(self):
        if self.brain_to_not_stop:
            self.read_from_json()
            for index_entity in range(0, 6):
                for index_upgrade in range(0, 5):
                    self.calculate_how_much_to_upgrade_cookie_producer(index_entity)
                    if index_upgrade == 4:
                        self.calculate_how_much_to_upgrade_power()
                        del self.upgrade_power_cost[0]
        else:
            self.brain_to_not_stop = False
            self.exit_program()

    def get_some_cookies(self):
        for index in range(0, 10):
            self.clicker.click_on_cookie()

    def calculate_how_much_to_upgrade_cookie_producer(self, nr_upgrade):
        difference = self.scraper.scrap_cookie_number() - self.scraper.scrap_cost_of_cookie_producer(nr_upgrade)
        if difference > 0:
            self.upgrade_cookie_producer(nr_upgrade)
        else:
            self.time_to_wait_upgrade_cookie_producer(nr_upgrade)

    def calculate_how_much_to_upgrade_power(self):
        if len(self.upgrade_power_cost) != 0:
            print("deci e diferita de 0 ------------------------------")
            difference = self.scraper.scrap_cookie_number() - self.upgrade_power_cost[0]
            if difference > 0:
                self.upgrade_power()
            else:
                self.time_to_wait_upgrade_power()
        else:
            pass

    def upgrade_cookie_producer(self, nr_upgrade):
        self.clicker.click_on_cookie_producer(nr_upgrade)
        self.write_to_json(nr_upgrade)

    def upgrade_power(self):
        self.clicker.click_on_upgrade()
        print("A FOST UPGRADAT UN POWER ----------------------------")

    def write_to_json(self, nr_upgrade):
        with open(self.current_file, "r") as file:
            json_content = file.read()
            self.content_current_file = json.loads(json_content)
        self.content_current_file[self.upgrade_list[nr_upgrade]][0] += 1
        self.content_current_file[self.upgrade_list[nr_upgrade]][1] = self.scraper.scrap_cost_of_cookie_producer(nr_upgrade)
        print(f'asta trebuie scris ca si nr de upgraduri: {self.content_current_file[self.upgrade_list[nr_upgrade]][0]}')
        print(f'asta trebuie scris ca si cost de upgraduri: {self.content_current_file[self.upgrade_list[nr_upgrade]][1]}')
        with open(self.current_file, "w") as file:
            json.dump(self.content_current_file, file)

    def read_from_json(self):
        try:
            with open("data.json", "r") as file:
                json_content = file.read()
                self.content_current_file = json.loads(json_content)
        except FileNotFoundError:
            self.create_json()

    def create_json(self):
        initial_data = {
            self.upgrade_list[0]: [0, 15],
            self.upgrade_list[1]: [0, 100],
            self.upgrade_list[2]: [0, 1100],
            self.upgrade_list[3]: [0, 12000],
            self.upgrade_list[4]: [0, 130000],
            self.upgrade_list[5]: [0, 1400000]
        }
        with open(self.current_file, "w") as file:
            json.dump(initial_data, file)

    def time_to_wait_upgrade_cookie_producer(self, nr_upgrade):
        self.get_some_cookies()
        # time_to_wait = self.scraper.scrap_cost_of_cookie_producer(nr_upgrade) / self.scraper.scrap_cookie_per_second()
        # time.sleep(time_to_wait)
        self.calculate_how_much_to_upgrade_cookie_producer(nr_upgrade)

    def time_to_wait_upgrade_power(self):
        self.get_some_cookies()
        self.calculate_how_much_to_upgrade_power()

    def exit_program(self):
        sys.exit()

    def delete_old_json(self):
        if os.path.exists(self.current_file):
            os.remove(self.current_file)
