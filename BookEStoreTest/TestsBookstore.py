from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json


def test_home_page():
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    driver.get('http://books.toscrape.com')
    assert "All products" in driver.title
    driver.close()


def test_pages_nav():
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    driver.get('http://books.toscrape.com')
    driver.implicitly_wait(10)
    with open('webpages.json', 'r') as f:
        books = json.load(f)
        for i in books:
            stri = "".join(i)
            driver.implicitly_wait(3)
            section = driver.find_element_by_link_text(stri)
            section.send_keys(Keys.RETURN)
            driver.implicitly_wait(3)
            assert stri in driver.title
            stri.replace(stri, "")
        f.close()
    driver.close()


def test_pages_books_row():
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    driver.get('http://books.toscrape.com')
    driver.implicitly_wait(10)
    with open('webpages.json', 'r') as f:
        books = json.load(f)
        for i in books:
            stri = "".join(i)
            driver.implicitly_wait(3)
            section = driver.find_element_by_link_text(stri)
            section.send_keys(Keys.RETURN)
            driver.implicitly_wait(3)
            contents = driver.find_element_by_class_name("row")
            assert contents.is_displayed()
            stri.replace(stri, "")
        f.close()

    driver.close()
