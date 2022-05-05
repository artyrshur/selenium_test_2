from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path='./chromedriver.exe'
)
driver.get("https://www.ozon.ru/")

# search_field = driver.find_element_by_id("search")
searchbox = driver.find_element_by_xpath('//*[@id="stickyHeader"]/div[3]/div/form/div[2]/input[1]')
searchbox.send_keys('iphone')
searchbox.send_keys(Keys.RETURN)
# searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')

add_to_basket_button = driver.find_element_by_xpath('//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[2]/div[4]/div[1]/div/div/div[1]/div[3]/div[3]/div/div/div/button/span/span')
add_to_basket_button.click()

shopping_basket = driver.find_element_by_xpath('//*[@id="stickyHeader"]/div[4]/a[2]').click()
bad_guy = driver.find_element_by_xpath('//*[@id="layoutPage"]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div[3]/div').click()
