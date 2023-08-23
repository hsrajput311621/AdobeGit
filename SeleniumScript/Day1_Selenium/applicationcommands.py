
#time.sleep(5) : it is used to hold the screen for 5 seconds.
#------------------------------------------------------------------------------------

#Application commands :
# title,
# current url ,
# page_source.

#-----------------------------------------------------------------------------------

# Conditional commands :
# is_displayed() :
# is_enabled() :
# is_selected() : Radio buttons, checkbox testing.
#--------------------------------------------------------------------------------------

#Browser commands#
#close()  : it will close the single browser/session and did not kill the process, it will close the current locator of browser/session which is currently focused.
#quite() : it will quite all the browser/sessions as well as kill the process.

#---------------------------------------------------------------------------------------

#Navigation commmand #
# it is used to nagivate between two websites and the reloding of the page.
#back(): it will go back to previous wesite
#forward(): it will go to next website
#refresh(): reload

#Syntax:--->
#driver.get("https://demo.nopcommerce.com/register")
#driver.get("https://money.rediff.com/indices/bse/bse100?src=moneyhome_bseIndices")
#driver.back()
#driver.forward()
#driver.refresh()

#----------------------------------------------------------------------------------------

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register")

driver.maximize_window()

print(driver.current_url)    #"https://money.rediff.com/indices/bse/bse100?src=moneyhome_bseIndices"

print(driver.title)       # Indian Market BSE, NSE, Stock quotes, share market, stock market, stock tips: Rediff Stocks

# print(driver.page_source)
#
# print(driver.current_window_handle)
#
# #print(driver.application_cache)
#
# print(driver.capabilities)
#
# print(driver.desired_capabilities)
#
# print(driver.window_handles)

#is_displayed(), is_enabled(), is_selected() #  uses for validation

searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")

print("Display status", searchbox.is_displayed())

print("Enabled status", searchbox.is_enabled())

male_radiobutton = driver.find_element(By.XPATH, "//input[@id='gender-male']")
print("is Male radio button of make selected", male_radiobutton.is_selected())

female_radiobutton = driver.find_element(By.XPATH, "//input[@id='gender-female']")
print("is Femaile radio button of make selected", female_radiobutton.is_selected())

driver.find_element(By.XPATH, "//input[@id='gender-male']").click()

print("is Male radio button of make selected", male_radiobutton.is_selected())
print("is Femaile radio button of make selected", female_radiobutton.is_selected())

driver.find_element(By.XPATH, "//input[@id='gender-female']").click()

print("is Femaile radio button of make selected", female_radiobutton.is_selected())
print("is Male radio button of make selected", male_radiobutton.is_selected())

driver.close()

