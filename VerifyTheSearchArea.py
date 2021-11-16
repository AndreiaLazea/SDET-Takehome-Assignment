from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\\chromedriver.exe"))

#Open bayut.com
driver.get("https://www.bayut.com/")
driver.maximize_window()

#Select properties For Sale // For Sale property doesn't exist anymore, but the Proprery Search was selected
driver.find_element(By.XPATH, "//*[@id='body-wrapper']/header/div[4]/div/div[1]/button[1]").click()
sleep(2)

#Select Dubai Marina as a l ocation
driver.find_element(By.XPATH, "//*[@id='body-wrapper']/header/div[4]/div/div[2]/div/div[1]/div[2]/div/div/ul/input").send_keys("Dubai Marina")
sleep(1)

#Search for properties
driver.find_element(By.XPATH, "//*[@id='body-wrapper']/header/div[4]/div/div[2]/div/div[2]/a").click()
sleep(1)

#Verify that all displayed properties contain the selected location
a = driver.find_elements(By.CLASS_NAME, "_7afabd84")
for value in a:
    if "Dubai Marina" in value.text:
        print("The result on the position %d does contain the selected location" % a.index(value))
    else:
        print("The result on the position %d doesn't contain the selected location" % a.index(value))

#print a text at the end of the test
print("End of test - Verify The Search Area ")

#close the browser
driver.close()
