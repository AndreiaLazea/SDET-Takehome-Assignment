from pip._vendor import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\\chromedriver.exe"))

#open bayut.com
driver.get("https://www.bayut.com/")
driver.maximize_window()

#Scroll down to the ' Popular searches' section on the homepage
target = driver.find_element(By.XPATH, '//*[@id="body-wrapper"]/main/div[6]/div/div[2]/div[1]/div[1]/div/div[1]')
actions = ActionChains(driver)
actions.move_to_element(target).perform()

#Open the ' To rent' tab
driver.find_element(By.XPATH, "//*[@id='body-wrapper']/main/div[6]/div/div[2]/div[2]/div/div/div[2]").click()

#Validate l inks under ' Dubai apartments' are functioning correctly
a = driver.find_elements(By.CLASS_NAME, "_78d325fa ")
for value in a[1:6]:
    links = value.get_attribute('href')
    try:
        requests.get(links)
        print("The %s is valid" % links)
    except requests.ConnectionError as exception:
        print("Not valid")

#print a text at the end of the test
print("End of test - Verify Popular Searches Links Work Correctly ")

#close the browser
driver.close()
