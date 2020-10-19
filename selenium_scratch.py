from selenium.webdriver import Chrome, ChromeOptions, Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# time = 1

options = ChromeOptions()
driver = Chrome(options=options)

driver.get('https://scratch.mit.edu/join')
assert 'Scratch' in driver.title

input_element = driver.find_element_by_id("username")
input_element.send_keys('WDM_test_selenium_0')

input_element = driver.find_element_by_id("password")
input_element.send_keys('scratch')

input_element = driver.find_element_by_id("passwordConfirm")
input_element.send_keys('scratch')
input_element.send_keys(Keys.RETURN)

# print(driver.title)
time.sleep(0.5)

country_element = driver.find_element_by_name("country")
country_select_element = Select(country_element)
country_select_element.select_by_value("Japan")

driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div/div[3]/button").click()

time.sleep(0.5)

birth_month_element = driver.find_element_by_name("birth_month")
birth_month_select_element = Select(birth_month_element)
birth_month_select_element.select_by_value("1")

birth_year_element = driver.find_element_by_name("birth_year")
birth_year_select_element = Select(birth_year_element)
birth_year_select_element.select_by_value("2020")

driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div/div[3]/button").click()

time.sleep(0.5)

driver.find_element_by_id("GenderRadioOptionFemale").click()
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div/div[2]/button").click()

input_element = driver.find_element_by_id("email")
input_element.send_keys('wd.machida@gmail.com')

time.sleep(0.5)

driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div/div[3]/button").click()

# driver.quit()
