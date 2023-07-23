import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

def selectors(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '.first_block input.first').send_keys('Ivan')
    browser.find_element(By.CSS_SELECTOR, '.first_block input.second').send_keys('Ivanov')
    browser.find_element(By.CSS_SELECTOR, '.first_block input.third').send_keys('ivanov@')
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    return browser.find_element(By.TAG_NAME, "h1").text


class TestSel(unittest.TestCase):
    def test_sel_1(self):
        self.assertEqual(selectors('http://suninjuly.github.io/registration1.html'),
                         "Congratulations! You have successfully registered!")

    def test_sel_2(self): # должен упасть
        self.assertNotEqual(selectors('http://suninjuly.github.io/registration2.html'),
                         "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()
