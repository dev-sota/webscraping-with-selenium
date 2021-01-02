
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def new_driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://scraping-for-beginner.herokuapp.com/login_page')
    return driver


driver = new_driver()

# Login
elem_username = driver.find_element_by_id('username')
elem_username.send_keys('imanishi')

elem_password = driver.find_element_by_id('password')
elem_password.send_keys('kohei')

elem_login_btn = driver.find_element_by_id('login-btn')
elem_login_btn.click()

# GET
elems_th = driver.find_elements_by_tag_name('th')
keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)


elems_td = driver.find_elements_by_tag_name('td')
values = []
for elem_td in elems_td:
    value = elem_td.text
    values.append(value)


# CSV
df = pd.DataFrame()
df['category'] = keys
df['value'] = values
df.to_csv('result.csv', index=False)

driver.quit()
