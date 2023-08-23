# By this we do not always download the Chromedriver, the below syntax will automatically download the
#latest driver and run the automation tool.

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
