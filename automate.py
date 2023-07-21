from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)



#Step 1:Go to CLNx Login Page
clnxLoginPath = "https://clnx.utoronto.ca/home.htm"
driver.get(clnxLoginPath) 
wait = WebDriverWait(driver, 10)

#Step 2: Click on Faculty and Staff
button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Faculty & Staff']"))) 
button.click()

#Step 3: Click on Log in to CLNx with your UTORid
button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[strong[span[text()='Log in to CLNx with your UTORid']]]"))) 
button.click()

#Step 4: Enter UTORid and Password if not logged in
current_url = driver.current_url
if(not current_url == "https://clnx.utoronto.ca/myAccount/dashboard.htm"):
    #Step 4.1: Enter UTORid 
    userName = "dengweia"
    user_name_field = wait.until(EC.presence_of_element_located((By.ID, "username" )))
    user_name_field.send_keys(userName)
    
    #Step 4.2: Enter Password
    password = "Victor928@"
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password" )))
    password_field.send_keys(password)
    
    #Step 4.3: Click on Log in
    button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='log in']"))) 
    button.click()

#Step 5: Click on Menu
button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[i[text()='menu']]"))) 
driver.execute_script("arguments[0].click();", button)

#Step 6: Click on Switch Account
button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[span[text()='Access Different Account']]"))) 
driver.execute_script("arguments[0].click();", button)

#Step 7: Click on Correct Account
switch_Account = "Victor Deng (vdeng)"
button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='"+switch_Account+"']"))) 
driver.execute_script("arguments[0].click();", button)