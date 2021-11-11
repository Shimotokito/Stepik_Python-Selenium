from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('Max')
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('Graur')
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('Graur@mail.ru')
    element = browser.find_element(By.NAME, 'file')
    current_dir = os.path.abspath(os.path.dirname("file.txt"))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "[type='submit").click()

finally:
    time.sleep(10)
    browser.quit()

