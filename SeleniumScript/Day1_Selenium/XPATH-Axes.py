
#We do have different XPATH Aexes in the Selenium
# Self , Parent , Child , Ancestor , Descendant , following , following -sibling , preceding , preceding - sibling.



# Self : Self is a node which is the start node for travesing in the DOM, we need to select the self node first.
# //tagname[attribute = 'value']/self::tagname

# Child: Traverse all child element of the current html tag: //*[attribute = 'value']/child::tagname.

# Parent: Traverse parent element of the current html tag: //*[attribute = 'value']/parent::tagname.

# Following: Traverse all element that comes after the current tag: //*[attribute = 'value']/following::tagname

#Following-sibling: Traverse from current html tag to next sibling html tag, parllel node of same class:

# //current html tag[@attribute = 'value']/following-sibling::siblingtag[@attribut = 'value']

#Preceding: Traverse all nodesthat comes before the current html tag: //*[attribute = 'value']/preceding::tagname

#preceding-sibling: Traverse from current HTML tag to previous sibling html tag:

# //current html tag[@attribute = 'value']/preceding-sibling::sibling tag[@attribut = 'value']

# Ancestor : Traverse all the ancestor elements(Grandparent, parent, etc) of the current html tag: //*[attribute = 'value']/ancestor::tagname

# Descedant: Traverse all descendant element (child node, grandchild node, etc) of current html tag: //*[attribute = 'value']/descendant::tagname

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/indices/bse/bse100?src=moneyhome_bseIn ")
text_message = driver.find_element(By.XPATH, "//a[contains(text(), 'Axis Bank Ltd')]/self::a").text

print(text_message)   # Axis Bank Ltd

# parent #

text_parent = driver.find_element(By.XPATH, "//a[contains(text(), 'Axis Bank Ltd')]/parent::td").text

print(text_parent)   # Axis Bank Ltd

# child #

childs = driver.find_elements(By.XPATH, "//a[contains(text(), 'Axis Bank Ltd')]/ancestor::tr/child::td")

print(len(childs))  #6

#ancestor #

text_ancestor = driver.find_element(By.XPATH, "//a[contains(text(), 'Axis Bank Ltd')]/ancestor::tr").text

print(text_ancestor)   # Axis Bank Ltd. A 728.20 730.95 -2.75 -0.38

#descendant #

descendants = driver.find_elements(By.XPATH, "//a[contains(text(), 'Axis Bank Ltd')]/ancestor::tr/descendant::*")

print("The number of nodes descendant", len(descendants)) # 9

# following nodes #

followings = driver.find_elements(By.XPATH, "//a[contains(text(), 'Axis Bank Ltd')]/ancestor::tr/following::*")

print("The number of nodes descendant", len(followings))   #1030


# following-siblings #

followings_sibling = driver.find_elements(By.XPATH, "//a[contains(text(), 'Axis Bank Ltd')]/ancestor::tr/following-sibling::*")

print(len(followings_sibling))   #86

#Preceding#

precedings = driver.find_elements(By.XPATH, "//a[contains(text(), 'Axis Bank Ltd')]/ancestor::tr/preceding::*")

print(len(precedings))    #354

#Preceding-sibling#

precedings_sibling = driver.find_elements(By.XPATH, "//a[contains(text(), 'Axis Bank Ltd')]/ancestor::tr/preceding-sibling::*")

print(len(precedings_sibling))  #13

driver.quit()