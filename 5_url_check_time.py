from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from configparser import ConfigParser


def login(driver):
    driver.find_element_by_id('email').click()
    input_login = driver.find_element_by_id('email')
    input_login.send_keys(my_login)
    input_login.send_keys(Keys.ENTER)
    input_password = driver.find_element_by_id('password')
    input_password.send_keys(password)
    input_password.send_keys(Keys.ENTER)


def url_checker(driver):
    # with open(file_address + '/data/5_url_checked_time.txt', 'a') as clear_checker:
    #     clear_checker.write("")
    with open(file_address + "data/2_url_uncheck8.txt", "r") as url_uncheck:
        for url in url_uncheck.read().split("\n"):
            hash_url = url.split()[0]
            time.sleep(1)
            driver.get(standart_url + 'documentView/%s/' % hash_url)
            wait = WebDriverWait(driver, 300)

            Parser_type_field = wait.until(EC.element_to_be_clickable((
                By.XPATH, '//*[@id="parser_type"]'))).\
                get_attribute('value')

              # end_time_field = wait.until(
              #   EC.element_to_be_clickable((
              #       By.XPATH, '//*[@id="left"]/div/form/div/div[5]/div/table/tbody/tr[1]/td[5]/div/input'))).\
              #   get_attribute('value')

            if Parser_type_field == "ParseType27":

                with open(file_address + 'data/3_URL8.txt', 'a') as url_checked:
                    url_checked.write( hash_url + "\n")
            else:
                pass


if __name__ == '__main__':
    try:
        cfg = ConfigParser()
        cfg.read("./0_Settings.ini")
        my_login = cfg.get('login_data', 'login')
        password = cfg.get('login_data', 'password')
        dashboard = cfg.get('data', 'dashboard')
        parsed = cfg.get('data', 'parsed')
        standart_url = cfg.get('data', 'standart_url')
        file_address = cfg.get('address', 'file_address_is')
        period_since = cfg.get('period', 'since')
        period_till = cfg.get('period', 'till')

        driver = webdriver.Chrome()
        driver.get(standart_url)
        driver.maximize_window()

        login(driver)
        time.sleep(2)
        url_checker(driver)
    except IndexError:
        print("UrlsTime: Checked")
        driver.close()
