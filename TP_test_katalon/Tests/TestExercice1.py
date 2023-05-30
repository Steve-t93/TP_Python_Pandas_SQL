import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

class Exercice1TestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("./chromedriver.exe")
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username = "Admin"
        self.password = "admin123"
        self.browser.implicitly_wait(30)

    def test_login(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys(self.username)
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys(self.password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()


    def test_logout(self):
        self.test_login()
        self.browser.find_element(By.XPATH, "//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        self.browser.find_element(By.LINK_TEXT, "Logout").click()

    def test_loginKO(self):
        driver = self.browser
        driver.get(self.url)
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Steve")
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("1234")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def test_deconnexion(self):
        self.test_logout()


if __name__ == '__main__':
    unittest.main(verbosity=2)



