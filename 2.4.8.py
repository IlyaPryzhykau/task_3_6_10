from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    button_book = browser.find_element(By.ID, 'book')
    button_book.click()

    x_element = browser.find_element(By.ID, 'input_value').text
    y = calc(x_element)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(y)

    button_submit = browser.find_element(By.ID, 'solve')
    button_submit.click()

finally:
    print(browser.switch_to.alert.text.split(': ')[-1])
    browser.quit()



