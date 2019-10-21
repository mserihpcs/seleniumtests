from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


import time

driver = webdriver.Chrome('/home/serim/redhat/seleniumtests/chromedriver')
#driver.implicitly_wait(10)

driver.get("https://www.redhat.com/en/technologies/management/insights")

# time.sleep(5)


driver.find_element_by_css_selector("#utility-account > a").click()

#driver.find_element_by_css_selector("div.account-login-wrapper #redhat-account-login-link1").click()

# time.sleep(5)

try:
    element = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "div.account-login-wrapper #redhat-account-login-link"))
    )
    element.click()
except (NoSuchElementException, TimeoutException) as exception:
    print("Element not foud")

#driver.find_element_by_css_selector("div.account-login-wrapper #redhat-account-login-link").click()
driver.find_element_by_id("username").send_keys("bugbeckham")
driver.find_element_by_id("password").send_keys("as12AS!@")
driver.find_element_by_id("_eventId_submit").click()
#assert (driver.find_element_by_css_selector(span:contains[Invalid username or password.])).text
#element = driver.find_element_by_css_selector("span.kc-feedback-text").get_attribute("innerText")
#assert "Invalid username or password." in element

driver.find_element_by_id("customerPortalLink").click()

time.sleep(5)

select = Select(driver.find_element_by_css_selector("a.btn.product-btn.style-scope.ts-chosen-selector"))
print(select.options)

dropdownelement = driver.find_element_by_css_selector("a.btn.product-btn.style-scope.ts-chosen-selector")

for option in dropdownelement.find_elements_by_css_selector('option'):
    if option.text == 'Ansible Tower by Red Hat':
        option.click()


# print('outside try finally')
# driver.find_element_by_css_selector("div.account-login-wrapper #redhat-account-login-link").click()
# #element.click()
# time.sleep(10)
#
# driver.implicitly_wait(1000)
#
# driver.find_element_by_css_selector('#utility-account a')
#
# driver.w
# driver.close()
# driver.quit()

