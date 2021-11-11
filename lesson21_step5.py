from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckBox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[type='radio']#robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
    time.sleep(20)
    browser.quit()