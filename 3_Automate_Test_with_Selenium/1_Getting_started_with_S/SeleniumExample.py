from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://google.com')
driver.maximize_window()

ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


#Apparently, "q" is the name of the element that we use to search on Google. Still don't know why or how to get this info...
element = driver.find_element("name", "q")

#The following will type "test" into the Google search bar. 
element.send_keys('test')

#The following will hit the Return key, so that the search is performed. 
element.send_keys(Keys.RETURN)

