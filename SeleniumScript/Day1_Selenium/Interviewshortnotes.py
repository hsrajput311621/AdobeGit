
# methods classes and various function use in selenium, to test the using locators.
# switch_to: it is used in following ways:

#1) driver.switch_to.alert : It is used to switch the focus of the locator to the alert rather than the locator.
#2) driver.switch_to.window(childwindowid): it will change the focus to child window from the parent window.
#3) driver.switch_to.window(parentwindowid):  It will change the focus back to parent window which is launched initially.
#4) driver.window_handles : it will provide us the windowIDs of all the browsers open.
#5) get_attribute() : It returns values of any attribute of web element, for this we need to pass the attribute inside the brackets.
#6) object.select_by_visible_text("Oct"): Select class is use to pic the date from the date picker box.
#7) from selenium.webdriver.support.select import Select : import the Select clasee from selenium.
#8) from selenium.webdriver import ActionChains : import class ActionChains for Mouse and Keyboard operations.
#9) driver.switch_to.frame("iframeResult") : switch to frame from the normal webpage.
#10) ActionChains(driver).double_click(button).perform() : to perform double click action.
#11) ActionChains(driver).drag_and_drop(Source_ele, target_ele).perform() :it will drag an element from one position(soruce) to another or destination.
#12) ActionChains(driver).context_click(button).perform(): It will perform the right click function.
#13) driver.switch_to.alert.accept() : accept class to close the alert by using OK button.
#14) driver.switch_to.alert.dismiss() : dismiss class to close the alert by using Cancel button.
#15) Select(dropcountry).select_by_visible_text("India") : It will select from the dropdown by text.
#a) Select(dropcountry).select_by_value("10") : It will select from the dropdown by Value.
#b) Select(dropcountry).select_by_index(13) : It will select from the dropdown by index
#16) dropselect.options : here we are using options for fetching the name of the state in the dropdown.
#17) driver.switch_to.frame() :It will use to switch to the specific frame and we need to add the name in brackets().
#18) driver.switch_to.parent_frame()  #in selenium frame we can switch back to parent frame, from inner frame.
#19) driver.switch_to.default_content() : it will switch back to default/main page.
#20) ActionChains(driver).key_down(Keys.CONTROL)---> ActionChains(driver).send_keys("a")  ---> act.key_up(Keys.CONTROL) ---> act.perform()
# it will helps us to use keyboard key (ctrl+A) : where act = ActionChains(driver), we can also wrtie the above command in single line as follows.
#a) act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform().
#21) act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform(): we can perform keyboard action of CTRL+C = copy command.
#22) act.send_keys(Keys.TAB).perform() : Tab commands to navigate.
#23) act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform() : We can perform ctrl+V for paste.
#24) Contains() operator use with Xpath to find the locators: It is use when one single button work two behaviour like start and stop on sigle button.
#25) Starts-with(): It is us when we know the locators are start with the alphabet.
#26) act=ActionChains(driver) ---> act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform():
# Above will use to mouse hover.
#27) flag = driver.find_element(By.XPATH,"//img[@alt = 'Flag of India']" )
#a) driver.execute_script("arguments[0].scrollIntoView();", flag)
#b) value = driver.execute_script("window.pageY0ffset;")
#c) print("Number of pixels moved, ", value): This will scroll down to find the element requested by the locators.
#28) driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)"): if we remove -, it will use to scroll down to the end of the page.
#a) value = driver.execute_script("window.pageY0ffset;")
#b) print("Numcber of pixels moved, ", value) : This will scroll up to the top of the page.
#29) webdriver.ChromeOptions().ops.add_argument("--disable-notifications") :this will use to disable the notification popup before opening the website.
#30) act = ActionChains(driver) : ActionChains() is a class to perform the mouse and keyboard action in selenium.
#a) act.drag_and_drop_by_offset(left_slider, 100, 0).perform() : This is use the slider to move left.
#b) act.drag_and_drop_by_offset(right_slider,-39, 0).perform() : This is use to slide the image to right.
#31) print(right_slider/left_slider.location) : this will tell us the locaiton of the slider when move to left / right.
#32)Implicit wait: It is need to call only one time and we can use it all the program,it always take max time,
# by the time we get the locators the command will execute.
#a) Explicit wait: it works based on condition, till the locators are visible or present.
#b) from selenium.webdriver.support.wait import WebDriverWait : Explicit use the WebDriverWait class in the selenium for the Explicit wait,
#c) it will take two argument one is object and one time in seconds.
#d) from selenium.webdriver.support import expected_conditions as EC   # here EC as a allias of Expected_conditions.
#e) mywait = WebDriverWait(driver, 10,poll_frequency= 2 , ignored_exceptions=[Exception]) # this is declaration part of the Explicit wait.
#f) mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']"))).click().


# Important class to import in the selenium.

#from selenium import webdriver
#import webdriver_manager.chrome
#from selenium.webdriver.common.by import By : By class for find_element with the help of locators.
#from selenium.webdriver.chrome.service import Service  : Service object for calling Chrome class.
#from selenium.webdriver.support.select import Select : Select class is use to switch command to alert and dropdown, datepicker.
#from selenium.webdriver.support.wait import WebDriverWait : Explicit wait.
#from selenium.webdriver.support import expected_conditions as EC   # here EC as a allias of Expected_conditions: Exlicit wait
#import time : it is use to use time.sleep()
#import webdriver_manager.utils: ActionChains is use when we import in selenium.
#from selenium.webdriver import ActionChains: for mouse,keyboard operations
#import requests as requests : need to import requests in selenium.







