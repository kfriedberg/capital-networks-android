from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
import time

logfile_name = "checklog-" + time.strftime("%Y%m%d%H%M%S") + ".txt"

with open("credentials.txt") as credentials:
    username = credentials.readline().strip()
    password = credentials.readline().strip()

with open("sites.txt") as sites, open(logfile_name, "a") as logfile, Chrome() as driver:
    print("Logging to " + logfile_name)
    driver.set_page_load_timeout(10)
    for site in sites:
        site = site.strip()
        print(site, end = '\t')
        print(site, end = '\t', file = logfile)
        try:
            driver.get("http://" + username + ":" + password + "@" + site + ":9000/settings")
            daily_type = Select(driver.find_element(By.NAME, "daily_type"))
            daily_type_text = daily_type.first_selected_option.get_attribute("text")
            print(daily_type_text)
            print(daily_type_text, file = logfile)
        except TimeoutException:
            print("Site took too long to load, could be down")
            print("Site took too long to load, could be down", file = logfile)
        except NoSuchElementException:
            print("Didn't find element. Is this the right page?")
            print("Didn't find element. Is this the right page?", file = logfile)
        except WebDriverException as ex:
            if "ERR_NAME_NOT_RESOLVED" in ex.msg:
                print("Site name does not resolve in DNS")
                print("Site name does not resolve in DNS", file = logfile)
            else:
                raise
                
