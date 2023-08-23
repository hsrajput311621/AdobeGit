
# What to perform in the task:
#1 Count numbers of row and columns
#2 Read specific row and column data
#3 Read all the rows and columns data
#4 read data based on conditional(List books name whose author is Mukesh)



# Webtable is of two type in the website:

#1) Static webtable
#2) Dynamic webtable

import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com")

#driver.implicitly_wait(5)

driver.maximize_window()

print(driver.current_url)

print(driver.title)

#1 Count numbers of row and columns

rowsnumber = driver.find_elements(By.XPATH, "//table[@name = 'BookTable']/tbody/tr")

print(len(rowsnumber))  #7

colnumbers = driver.find_elements(By.XPATH, "//table[@name = 'BookTable']/tbody/tr/th")

print(len(colnumbers)) #4

time.sleep(2)

#2 Read specific row and column data:

#spec_ele = driver.find_element(By.XPATH, "//td[normalize-space()='Master In Selenium']")
#print(spec_ele.text)

# driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]")


#3 Read all the rows and columns data

for r in range(2, len(rowsnumber)+1):
    for c in range(1, len(colnumbers)+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end="        ")
    print(" ")


#4 read data based on conditional(List books name whose author is Mukesh)

for r in range(2, len(rowsnumber)+1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name ='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        Subject = driver.find_element(By.XPATH, "//table[@name ='BookTable']/tbody/tr[" + str(r) + "]/td[3]").text
        Price = driver.find_element(By.XPATH, "//table[@name ='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName, "         ",authorName, "          ",Subject,"           ", Price)


driver.close()
