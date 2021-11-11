from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    number2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    x = int(number1) + int(number2)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(x))

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(20)
    browser.quit()





