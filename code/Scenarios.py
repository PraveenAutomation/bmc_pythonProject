import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.maximize_window()
driver.get("https://www.google.co.in/")
driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Amazon")
driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
time.sleep(5)

# print all the search results:
search_result = driver.find_elements(By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']")
for i in search_result:
    print(i.text)

Amazon_in_link = driver.find_element(By.XPATH, './/h3[contains(text(),\'Amazon.in\')]').click()

signin_link = driver.find_element(By.XPATH, './/span[@id=\'nav-link-accountList-nav-line-1\']')

actionChain = ActionChains(driver)

wait.until(EC.visibility_of_element_located((By.XPATH, './/span[@id=\'nav-link-accountList-nav-line-1\']')))
actionChain.move_to_element(signin_link)
signin_link.click()

email_id = driver.find_element(By.ID, 'ap_email').send_keys('test.automanual@gmail.com')
continue_button = driver.find_element(By.ID, 'continue').click()
password = driver.find_element(By.ID, 'ap_password').send_keys('Test@123456')
signin_continue = driver.find_element(By.ID, 'signInSubmit').click()

time.sleep(10)

searchDropdown = driver.find_element(By.XPATH, './/select[@id=\'searchDropdownBox\']')
selectCategory = Select(driver.find_element(By.XPATH, './/select[@id=\'searchDropdownBox\']'))
searchDropdown.click()
wait.until(EC.visibility_of_all_elements_located((By.XPATH, './/select[@id=\'searchDropdownBox\']//option')))
time.sleep(5)
dropDown_options = driver.find_elements(By.XPATH, './/select[@id=\'searchDropdownBox\']//option')

for i in dropDown_options:
    selectCategory.select_by_visible_text(i.text)
selectCategory.select_by_visible_text('Electronics')
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Dell computers')
driver.find_element(By.ID, 'nav-search-submit-button').click()
min_text_field = driver.find_element(By.XPATH, './/input[@id=\'low-price\']')
max_text_field = driver.find_element(By.XPATH, './/input[@id=\'high-price\']')
Go_button = driver.find_element(By.XPATH, './/input[@class=\'a-button-input\']')

time.sleep(5)

driver.execute_script('arguments[0].scrollIntoView()', min_text_field)
min_text_field.send_keys(20000)
max_text_field.send_keys(30000)
Go_button.click()
next_page_button = driver.find_element(By.XPATH, './/a[contains(@class,\'pagination-next\')]')
wait.until(EC.visibility_of_element_located((By.XPATH, './/a[contains(@class,\'s-pagination-next\')]')))
next_page_button.click()

time.sleep(5)

price_of_products = driver.find_elements(By.CSS_SELECTOR, '.a-price-whole')

for i in price_of_products:
    driver.execute_script('arguments[0].scrollIntoView()', i)
    price_firstPage = float(i.text.replace(',', ''))
    print(price_firstPage)

time.sleep(10)

print("=========================")
price_of_products_secondPage = driver.find_elements(By.CSS_SELECTOR, '.a-price-whole')
for j in price_of_products_secondPage:
    driver.execute_script('arguments[0].scrollIntoView()', j)
    price_secondPage = float(j.text.replace(',', ''))
    print(price_secondPage)


# back to main page
driver.back()
time.sleep(5)
driver.quit()
