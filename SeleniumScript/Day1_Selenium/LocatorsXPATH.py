

# Here we can see XPATH locators in the Selenium #

# We have two type of XPATH locators:
# 1) Absolute / Full XPATH
#It is a collection of Tags and Node, we need to write the nodes from root till the element we need to locate.

#e.g: /html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input

# 2) Relative / Partial XPATH : Mainly we use the Relative XPAth in the real sceanrio.

# Syntax : Tagname [@Attribute = "Value"]
#        : //input[@id = "snamll_searchterms"]
# If we do not know the Tagname we can use *
#Syntax: : //*[@Attribute = "Value"]

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#One more way to launch the webdriver like chrom, firefox

#   serv_obj = Service("D:\Web-Driver\chromedriver.exe")
#   driver = webdriver.Chrome(service=obj_serv)

driver = webdriver.Chrome()

driver.get("http://automationpractice.com/index.php")

driver.maximize_window()

print(driver.current_url)

print(driver.title)

# Absolute XPATH/ Full Xpath # --------------------------
# /html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/input[4]

#driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/input[4]").send_keys("T-shirts")

#driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

#------------------------------------------------------------------------------------

# Relative XPATH  Partial XPATH  # -----------------

#driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys("T-shirts")   #here we use input as tagname
#driver.find_element(By.XPATH, "//*[@id='searchbox']/button").click()                     # here we use * in place of tagname.

#--------------------------------------------------------------------------------------

# we can use more XPATH options such as 'OR', 'AND', 'Contains()', 'Starts-with()', 'text', in the query.

#driver.find_element(By.XPATH, "//input[@id = 'search_query_top' or @name = 'search_query']").send_keys("Shirts")  #OR

#driver.find_element(By.XPATH, "//*[@name = 'submit_search' and @class = 'btn btn-default button-search']").click()  #AND

#Contains() operator: It is use when one single buttong work two behaviour like start and stop on sigle button.
#Syntax : //Tagname[contains(@Attribute, 'value')] // *[contains(@Attribute, 'value')]

#Starts-with(): It is us when we know the locators are start with the alphatet.

#driver.find_element(By.XPATH, "//input[contains(@id, 'search')]").send_keys("Jeans")
#driver.find_element(By.XPATH,"//button[starts-with(@name, 'submit_search')]").click()

#text(): it us use when we have text format in the web pages like one link as women section so wonmen is a text.
# Syntax: //a[text()='Women']

driver.find_element(By.XPATH, "//a[text()='Women']").click()











