from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
import datetime
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


def timer():
    per_since = float(period_since) * 60
    per_till = float(period_till) * 60
    timers = (randint(int(per_since), int(per_till)))
    time.sleep(timers)


def perform_document(hashid):
    time.sleep(5)
    driver.get(standart_url + 'documentView/%s/' % hashid)
    wait = WebDriverWait(driver, 300)
    adv_mapped_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#advertiser")))
    adv_dropdown_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//div[@id="advertiser"]/div[1]/span/span[2]/span')))
    time.sleep(2)
    adv_dropdown_button.click()
    adv_dropdown_textfield = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="advertiser"]/input[1]')))
    advertiser_name = adv_mapped_field.get_attribute('value').strip()
    if advertiser_name == 'N/A':
        advertiser_name = 'Omicron'
    adv_dropdown_textfield.send_keys(advertiser_name)
    time.sleep(1)

    list_elements_adv = driver.find_elements_by_xpath('//span[@class="ui-select-highlight"]/parent::div')
    if len(list_elements_adv) == 1:
        adv_dropdown_textfield.send_keys(Keys.ENTER)
    else:
        adv_dropdown_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[@class="ui-select-highlight"]/parent::div[not(text())]')))
        time.sleep(1)
        adv_dropdown_element.click()

    time.sleep(1)
    agc_mapped_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#agency")))
    agc_dropdown_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//div[@id="agency"]/div[1]/span/span[2]/span')))
    time.sleep(2)
    agc_dropdown_button.click()
    agc_dropdown_textfield = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="agency"]/input[1]')))
    agency_name = agc_mapped_field.get_attribute('value').strip()
    if agency_name == 'N/A':
        agency_name = 'Omicron'
    agc_dropdown_textfield.send_keys(agency_name)
    time.sleep(1)

    list_elements_ags = driver.find_elements_by_xpath('//span[@class="ui-select-highlight"]/parent::div')
    if len(list_elements_ags) == 1:
        agc_dropdown_textfield.send_keys(Keys.ENTER)
    else:
        agc_dropdown_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[@class="ui-select-highlight"]/parent::div[not(text())]')))
        time.sleep(1)
        agc_dropdown_element.click()

    timer()

    #driver.save_screenshot(file_address + "screenshots/" + hashid + ".png")
    save_btn = driver.find_element_by_xpath('//button[text()="Save Header"]')
    save_btn.click()
    print(hashid)
    with open(file_address + 'data/4_hash_completed.txt', 'a') as file1:
        file1.write(hashid + " ||| " + datetime.datetime.now().strftime('%H:%M:%S || %d.%m') + "\n")
    print(datetime.datetime.now().strftime('%H:%M:%S'))

# def time_change_zero ():
#     list_elements_zero = driver.find_elements_by_xpath('//input[contains(@arrow-keys-index,":5")]').get_attrebut("value")
#     print(list_elements_zero)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    t1 = datetime.datetime.now()
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

        driver.get(standart_url + dashboard)
        driver.maximize_window()
        login(driver)

        array = []
        with open(file_address + "data/3_URL.txt", "r") as links:
            list_links = links.read().split("\n\n")[0].split("\n")
            for hash_item in list_links:
                duplicate = False
                for item in array:
                    if item == hash_item:
                        duplicate = True
                        print("Duplicate was deleted: " + item + "!")
                if not duplicate:
                    array.append(hash_item)

            for url in array:
                perform_document(url)
            driver.close()
            t2 = datetime.datetime.now()
            ft = t2 - t1
            print('Program completed!\nFull time work: ' + str(ft))
    except TimeoutException:
        t3 = datetime.datetime.now()
        ftr = t3 - t1
        print('Completed with an error while running: ' + str(ftr))
