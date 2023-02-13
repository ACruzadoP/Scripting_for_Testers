from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get('http://automationpractice.pl/index.php?id_category=3&controller=category')
driver.maximize_window()

product_containers = driver.find_elements("class name","product-container")

for index,product_container in enumerate(product_containers):
    hover = ActionChains(driver).move_to_element(product_container).perform()
    driver.find_element("xpath", '//*[@id="center_column"]/ul/li[%s]/div/div[2]/div[2]/a[1]/span'%(index+1)).click()
    time.sleep(1)
    driver.find_element("xpath", '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span').click()
    time.sleep(1)
    