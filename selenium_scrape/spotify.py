from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

import re

driver = webdriver.Firefox()

driver.get('https://open.spotify.com/playlist/0nkMz6KPJvVRru9iYCa2GB')


#id = Type__TypeElement-goli3j-0 dascyV VrRwdIZO0sRX1lsWxJBe



sleep(2)


number = driver.find_elements(By.XPATH,".//span[contains(@class, 'Type__TypeElement-goli3j-0 bWzOVV RANLXG3qKB61Bh33I0r2')]")
sLen = re.findall(r'([0-9]+)',number[0].text)[0]

print(int(sLen))



titles = driver.find_elements(By.XPATH,".//div[contains(@class,'Type__TypeElement-goli3j-0 cnoRHG t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line')]")
driver.execute_script("return arguments[0].scrollIntoView();", titles[10])
 




