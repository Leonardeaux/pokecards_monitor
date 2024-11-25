import selenium as se
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


# Verify if the script is running on linux or windows
if os.name == 'posix':
    gecko_path = 'webdrivers/geckodriver'
else:
    gecko_path = 'webdrivers/geckodriver.exe'


def get_driver():
    options = webdriver.FirefoxOptions()
    options.binary_location = gecko_path

    driver = webdriver.Firefox(options=options)

    return driver


if __name__ == "__main__":
    print(os.name)
    driver = get_driver()
    url = "https://www.cardmarket.com/fr/Pokemon"
    driver.get(url)