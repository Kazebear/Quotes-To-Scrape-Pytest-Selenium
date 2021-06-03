from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
driver.get('http://books.toscrape.com')
elem = driver.find_element_by_link_text('Travel')
elem.send_keys(Keys.RETURN)
driver.close()