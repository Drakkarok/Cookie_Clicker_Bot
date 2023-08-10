from create_page import CreatePage
from clicker import Clicker
from scraper import Scraper
from brain import Brain


url_of_game = "https://orteil.dashnet.org/cookieclicker/"
time_to_wait_from_main = 3

create_page = CreatePage(url_of_game)
clicker = Clicker(time_to_wait_from_main, create_page.driver)
scraper = Scraper(create_page.driver)
brain = Brain(scraper=scraper, clicker=clicker)
