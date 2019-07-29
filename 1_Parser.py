import datetime
import time
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login(driver):
    driver.get(standart_url + dashboard)
    time.sleep(2)
    driver.find_element_by_id('email').click()
    input_login = driver.find_element_by_id('email')
    input_login.send_keys(my_login)
    input_login.send_keys(Keys.ENTER)
    input_password = driver.find_element_by_id('password')
    input_password.send_keys(password)
    input_password.send_keys(Keys.ENTER)
    print('Login Successful')
    time.sleep(5)
    driver.get(standart_url + parsed)


def switching():
    for page in range(int(switch_page)):
        print("Parsing:")
        parsed_page()
        page_select()


def going_on_start_pages():
    next_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/section/div/div/table/thead/tr[1]/td/div/div[5]/ul/li[6]/a/span")))
    for i in range(int(start_page) - 1):
        next_btn.click()
        next_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/section/div/div/table/thead/tr[1]/td/div/div[5]/ul/li[6]/a/span")))
        wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="loading-bar-spinner"]/div')))  # spiner
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[2]/div')))  # first hash, check clicable


def page_select():
    next_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/section/div/div/table/thead/tr[1]/td/div/div[5]/ul/li[6]/a/span")))
    for i in range(1):
        next_btn.click()
        next_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/section/div/div/table/thead/tr[1]/td/div/div[5]/ul/li[6]/a/span")))
        wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="loading-bar-spinner"]/div')))  # spiner
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[2]/div')))  # first hash, check clicable


def date_select():
    wait.until(EC.element_to_be_clickable((By.ID, 'reportrange')))
    time.sleep(3)
    driver.find_element_by_id("reportrange").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/ul/li[6]")))
    driver.find_element_by_xpath("/html/body/div[6]/div[1]/ul/li[6]").click()
    input_date = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[2]/div[1]/input")))
    input_date.click()
    input_date.send_keys(Keys.CONTROL + 'a')
    input_date.send_keys(date_1)
    input_date2 = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/input")
    input_date2.send_keys(Keys.CONTROL + 'a')
    input_date2.send_keys(date_2)
    input_date2.send_keys(Keys.ENTER)
    driver.find_element_by_xpath("//button[contains(@class,'applyBtn') and not(@disabled)]").click()
    print("Date Selected")


def level_0():
    wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="loading-bar-spinner"]/div')))
    wait.until(EC.invisibility_of_element_located((By.ID, 'loading-bar-spinner')))  # spiner
    time.sleep(20)
    sort_by_risk_level = driver.find_element(By.XPATH, "//th[contains(text(),'current_risk_level')]")
    sort_by_risk_level.click()
    print("Pressed: Risk Level_0 ")
    time.sleep(2)


def parsed_page():
    with open(file_address + '/data/1_log.txt', 'a') as file:
        file.write("\n" + "\n" + "\n" + "Parsed by " + datetime.datetime.now().strftime(
            '%H:%M:%S, %d/%m/%y') + "  Date: " + date_1 + " - " + date_2 + "\n" + "\n")
    for y in range(1, 51):
        wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="loading-bar-spinner"]/div')))  # spiner
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[2]/div')))  # first hash, check clicable
        color_box = wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/section/div/div/table/tbody/tr[%s]" % y)))
        rgb = color_box.value_of_css_property('background-color')
        if rgb != "rgba(0, 128, 0, 0.14)":
            hash_id = ('/html/body/div[2]/section/div/div/table/tbody/tr[%s]/td[2]/div' % y)
            agancy = ('/html/body/div[2]/section/div/div/table/tbody/tr[%s]/td[4]/div' % y)
            advertiser = ('/html/body/div[2]/section/div/div/table/tbody/tr[%s]/td[5]/div' % y)
            contract_data = ('/html/body/div[2]/section/div/div/table/tbody/tr[%s]/td[6]/div' % y)
            risk_level = ('/html/body/div[2]/section/div/div/table/tbody/tr[%s]/td[7]/div' % y)
            with open(file_address + '/data/1_log.txt', 'a') as file:
                hash_ids = wait.until(EC.element_to_be_clickable((By.XPATH, hash_id))).text
                advertisers = wait.until(EC.element_to_be_clickable((By.XPATH, advertiser))).text
                agancys = wait.until(EC.element_to_be_clickable((By.XPATH, agancy))).text
                contract_datas = wait.until(EC.element_to_be_clickable((By.XPATH, contract_data))).text
                risk_levels = wait.until(EC.element_to_be_clickable((By.XPATH, risk_level))).text
                file.write(
                    hash_ids + " || " + agancys + " | " + advertisers + " || " + contract_datas + " || " + risk_levels + " || " + "\n")
        else:
            pass
    print("Parsed!")


def start_parsing():
    going_on_start_pages()
    switching()


if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read("./0_Settings.ini")
    date_1 = cfg.get('parser_date', 'first_date')
    date_2 = cfg.get('parser_date', 'second_date')
    my_login = cfg.get('login_data', 'login')
    password = cfg.get('login_data', 'password')
    dashboard = cfg.get('data', 'dashboard')
    parsed = cfg.get('data', 'parsed')
    standart_url = cfg.get('data', 'standart_url')
    file_address = cfg.get('address', 'file_address_is')
    start_page = cfg.get('switch_page', 'start_page')
    switch_page = cfg.get('switch_page', 'end_page')

    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 300)

    login(driver)
    date_select()
    level_0()
    start_parsing()
    driver.close()



