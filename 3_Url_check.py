from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from configparser import ConfigParser
from selenium.common.exceptions import TimeoutException


def login(driver):
    driver.find_element_by_id('email').click()
    input_login = driver.find_element_by_id('email')
    input_login.send_keys(my_login)
    input_login.send_keys(Keys.ENTER)
    input_password = driver.find_element_by_id('password')
    input_password.send_keys(password)
    input_password.send_keys(Keys.ENTER)


def url_checker(driver):
    # with open(file_address + 'data/3_URL.txt', '') as clear_checker:
    #     clear_checker.write("")
    # with open(file_address + 'data/3_URL.txt', 'a') as url_checked:
    #     url_checked.write("\n")
    with open(file_address + "data/2_url_uncheck.txt", "r") as url_uncheck:
        for url in url_uncheck.read().split("\n"):
            hash_url = url.split()[0]
            if hash_url == "Parsed":
                continue
            # print(hash_url)
            time.sleep(1)
            driver.get(standart_url + 'documentView/%s/' % hash_url)
            wait = WebDriverWait(driver, 300)
            try:
                    adv_mapped_field = wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "input#advertiser"))).get_attribute('value')
                    adv_dropdown_button = wait.until(EC.element_to_be_clickable(
                        (By.XPATH, '//div[@id="advertiser"]/div[1]/span/span[2]/span'))).get_attribute('innerHTML').strip()
                    agc_mapped_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#agency"))).get_attribute(
                        'value')
                    agc_dropdown_button = wait.until(
                        EC.element_to_be_clickable((By.XPATH, '//div[@id="agency"]/div[1]/span/span[2]/span'))).get_attribute(
                        'innerHTML').strip()
            except TimeoutException:
                continue
            if (adv_mapped_field != adv_dropdown_button and adv_dropdown_button != "Omicron Advertiser"
                    or agc_mapped_field != agc_dropdown_button and agc_dropdown_button != "Omicron Agency"):
                with open(file_address + 'data/3_URL.txt', 'a') as url_checked:
                    url_checked.write(hash_url + "\n")
            else:
                pass


if __name__ == '__main__':
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

    print("Urls checked")
    driver.close()
