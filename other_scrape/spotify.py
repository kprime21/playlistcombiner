from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()

driver.get('https://open.spotify.com/playlist/0nkMz6KPJvVRru9iYCa2GB')


sleep(1)
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()
ActionChains(driver).send_keys(Keys.TAB).perform()




SCROLL_PAUSE_TIME = 0.5
a = 35
titles = []
sleep(2)
i = 0

while (a<300):

    titles.append(driver.find_elements(By.XPATH,".//div[contains(@class,'Type__TypeElement-goli3j-0 cnoRHG t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line')]"))
    sleep(2)
    driver.execute_script("return arguments[0].scrollIntoView();", titles[i][a])
    sleep(2)
    print(titles)
    i+=1
    




# titles = driver.find_elements(By.XPATH,".//div[contains(@class,'Type__TypeElement-goli3j-0 cnoRHG t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line')]")

# for a in titles:
#     print(a.text)