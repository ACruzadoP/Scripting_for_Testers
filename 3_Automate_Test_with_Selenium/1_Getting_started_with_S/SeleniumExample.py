from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://google.com')

#Apparently, "q" is the name of the element that we use to search on Google. Still don't know why or how to get this info...
element = driver.find_element_by_name('q')

#The following will type "test" into the Google search bar. 
element.send_keys('test')

#The following will hit the Return key, so that the search is performed. 
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.RETURN)

