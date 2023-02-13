from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.selenium.dev/')
driver.maximize_window()



element = driver.find_element("xpath", '//*[@id="docsearch"]/button/span[1]/span')
element.click()

