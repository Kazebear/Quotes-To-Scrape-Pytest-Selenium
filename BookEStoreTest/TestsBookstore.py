from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_home_page():
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    driver.get('http://books.toscrape.com')
    assert "All products" in driver.title
    driver.close()


def test_travel_page():
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    driver.get('http://books.toscrape.com')
    travel_link = driver.find_element_by_partial_link_text('Trav')
    travel_link.send_keys(Keys.RETURN)
    assert "Travel" in driver.title
    driver.close()
