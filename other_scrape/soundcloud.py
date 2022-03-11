from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

#use selenium to scroll down then grab all the songs

driver = webdriver.Firefox()





driver.get("https://soundcloud.com/user6156924791/sets/juice-wrld-unreleased")

sleep(1)
ActionChains(driver).send_keys(Keys.TAB).perform()

ActionChains(driver).send_keys(Keys.ENTER).perform()

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



titles = driver.find_elements(By.XPATH,".//a[contains(@class,'trackItem__trackTitle sc-link-dark sc-link-primary sc-font-light')]")




for a in titles:
    print(a.text)




