from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json


def test_home_page():
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    driver.get('http://quotes.toscrape.com/')
    assert "Quotes to Scrape" in driver.title
    driver.close()


def test_quotes_and_top10():
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    driver.get('http://quotes.toscrape.com/')
    driver.implicitly_wait(3)
    quotes_row = driver.find_element_by_class_name("col-md-8")
    top_ten_row = driver.find_element_by_class_name("col-md-4.tags-box")
    assert quotes_row.is_displayed() and top_ten_row.is_displayed()
    driver.close()


def test_navigate_top10():
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    driver.get('http://quotes.toscrape.com/')
    driver.implicitly_wait(3)

    with open("top10tags.json", "r") as f:
        tags = json.load(f)

        for i in tags:
            stri = "".join(i)
            driver.implicitly_wait(3)
            top_ten_row = driver.find_element_by_class_name("col-md-4.tags-box")
            driver.implicitly_wait(3)
            tag = top_ten_row.find_element_by_link_text(stri)
            driver.implicitly_wait(3)
            tag.send_keys(Keys.RETURN)
            driver.implicitly_wait(3)
            h3tag = driver.find_element_by_tag_name("h3")
            tag_browsed = h3tag.find_element_by_link_text(stri)
            quotes_row = driver.find_element_by_class_name("col-md-8")
            assert tag_browsed.is_displayed() and quotes_row.is_displayed()
            stri.replace(stri, "")

        f.close()

    driver.close()


def test_nav_next_previous():
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    driver.get('http://quotes.toscrape.com/')
    driver.implicitly_wait(3)

    with open("top10tags.json", "r") as f:
        tags = json.load(f)

        for i in tags:
            stri = "".join(i)
            driver.implicitly_wait(2)
            top_ten_row = driver.find_element_by_class_name("col-md-4.tags-box")
            driver.implicitly_wait(2)
            tg = top_ten_row.find_element_by_link_text(stri)
            driver.implicitly_wait(2)
            tg.send_keys(Keys.RETURN)
            driver.implicitly_wait(2)
            try:
                next_btn = driver.find_element_by_partial_link_text("Next ")
                if next_btn.is_displayed():
                    next_btn.send_keys(Keys.RETURN)
                    driver.implicitly_wait(2)
                    previous_btn = driver.find_element_by_partial_link_text(" Previous")
                    previous_btn.send_keys(Keys.RETURN)
            except Exception:
                continue
            stri.replace(stri, "")

        f.close()

    driver.close()
