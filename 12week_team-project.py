from selenium import webdriver

url = 'https://www.op.gg/statistics/champion/'

driver = webdriver.Chrome('chromedriver')
driver.get(url)
driver.implicitly_wait(3)

driver.quit()