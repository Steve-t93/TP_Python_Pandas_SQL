from selenium import webdriver

def testSelenium():
    browser = webdriver.Chrome("src/chromedriver.exe")
    browser.get("http://selenium.dev/")
    assert 'Selenium' in browser.title
    browser.quit()

if __name__ == '__main__':
    testSelenium()