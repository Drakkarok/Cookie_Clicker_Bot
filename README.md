# Cookie_Clicker_Bot

Short description:  
A bot that automatically plays a web hosted CookieClicker for you!  
Link for the game: [https://orteil.dashnet.org/cookieclicker/](url)

Long description:  
A bot made with Selenium for a web broswer game named CookieClicker.  

It actively scrape the web page for:  
a) The current number of cookies that it has;  
b) The cost of cookie procedures (for each one);  
c) The current number of cookies per second that the cookie producers are making.  

Also it:  
a) decides to click for extra cookies;  
b) calculate what to upgrade (extra power or cookie producer);  
c) calculate how much until upgrade (extra power or cookie producer);  
d) upgrades power or cookie producer;  
e) creates a file where it tracks the current cost of cookie producers (they go up in price with every purchase);  
f) closes itself when it hits a certain target (upgrades and powers).  

---

## CONFIGURATION  

### Selenium  
Please follow the guide presented on this page: [https://www.cyberithub.com/how-to-install-selenium-webdriver-in-python-3/](url)  

---

Build using: 
- selenium;  
- time;  
- json;  
- sys;  
- os.  

Functions:
- N/A.

Classes:
- (1) CreatePage;
- (2) Scraper;
- (3) Clicker;
- (4) Brain.

Methods:
- (1) change_chrome_options;
- (1) initialize_webdriver;
- (1) open_specified_page;
- (1) maxime_window;
- (2) scrap_cookie_number;
- (2) scrap_cookie_per_second;
- (2) scrap_cost_of_cookie_producer;
- (3) click_got_it;
- (3) click_for_gdpr;
- (3) click_for_language;
- (3) click_on_cookie;
- (3) click_on_cookie_producer;
- (3) click_on_upgrade;
- (4) calculate_what_upgrade;
- (4) get_some_cookies;
- (4) calculate_how_much_to_upgrade_cookie_producer;
- (4) calculate_how_much_to_upgrade_power;
- (4) upgrade_cookie_producer;
- (4) upgrade_power;
- (4) write_to_json;
- (4) read_from_json;
- (4) create_json;
- (4) time_to_wait_upgrade_cookie_producer;
- (4) time_to_wait_upgrade_power;
- (4) delete_old_json;
- (4) exit_program.
