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


def get_url(driver, url):
    driver.get(url)



if __name__ == "__main__":
    print(os.name)
    driver = get_driver()
    get_url(driver, "https://www.google.com")