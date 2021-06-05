from selenium import webdriver
from selenium.webdriver.common.keys import Keys

linktexts = ["Books", "Travel", "Mystery", "Historical Fiction", "Sequential Art", "Classics", "Philosophy",
             "Romance", "Womens Fiction", "Fiction", "Childrens", "Religion", "Nonfiction", "Music",
             "Default", "Science Fiction", "Sports and Games", "Add a comment", "Fantasy", "New Adult",
             "Young Adult", "Science", "Poetry", "Paranormal", "Art", "Psychology", "Autobiography",
             "Parenting", "Adult Fiction", "Humor", "Horror", "History", "Food and Drink", "Christian Fiction",
             "Business", "Biography", "Thriller", "Contemporary", "Spirituality", "Academic", "Self Help",
             "Historical",
             "Christian", "Suspense", "Short Stories", "Novels", "Health", "Politics", "Cultural", "Erotica",
             "Crime"]


def test_home_page():
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    driver.get('http://books.toscrape.com')
    assert "All products" in driver.title
    driver.close()


def test_pages_nav():
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    driver.get('http://books.toscrape.com')
    driver.implicitly_wait(10)
    for i in linktexts:
        stri = "".join(i)
        driver.implicitly_wait(3)
        section = driver.find_element_by_link_text(stri)
        section.send_keys(Keys.RETURN)
        driver.implicitly_wait(3)
        assert stri in driver.title
        stri.replace(stri, "")

    driver.close()


def test_pages_books_row():
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    driver.get('http://books.toscrape.com')
    driver.implicitly_wait(10)
    for i in linktexts:
        stri = "".join(i)
        driver.implicitly_wait(3)
        section = driver.find_element_by_link_text(stri)
        section.send_keys(Keys.RETURN)
        driver.implicitly_wait(3)
        contents = driver.find_element_by_class_name("row")
        assert contents.is_displayed()
        stri.replace(stri, "")

    driver.close()
