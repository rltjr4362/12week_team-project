from selenium import webdriver

url = 'https://www.op.gg//'

driver = webdriver.Chrome('chromedriver')
driver.get(url)
driver.implicitly_wait(3)

driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[5]/a').click()

data = driver.page_source

driver.quit()