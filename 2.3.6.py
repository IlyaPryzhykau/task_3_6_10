from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(2)

    button_troll = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_troll.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    element_x = browser.find_element(By.ID, 'input_value').text
    y = calc(element_x)

    input_1 = browser.find_element(By.ID, 'answer')
    input_1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
