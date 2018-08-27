# ===STEP 3=== #

from selenium import webdriver
from time import sleep  # Sleep will pause the program
import os  # for getting the local path

dirpath = os.getcwd()  # gets local path
driver = webdriver.Chrome(dirpath + "/chromedriver")


# GET PAGE AND CHANGE LANGUAGE TO ENGLISH
driver.get("http://www.dominos.com.cn/menu/menu.html?menuIndex=0&RNDSEED=c42905609c237eff75c1bd6767345f43")  # dominos menu page
english = driver.find_element_by_css_selector('#lanEn > a')
english.click()  # click on english to change tha language
sleep(5)  # Wait for the website to update

# FIND PEPPERONI PIZZA AND CLICK ORDER
myPizza = "Pepperoni Pizza"
pizzaText = driver.find_element_by_xpath('//div[text() = "{}"]'.format(myPizza))  # uses xpath to select the pizza label element

# Here, we have the label that says pepperoni pizza.
# This isn't what we want though
#
# We want to click the button that says to buy
# To do that, we have to have a look at the actual structure of the page
# The label and the button are all wrapped in a bigger div. We can get the button by finding
# the label's parent and getting it's child, the button
#
# That's essentially what the following code does

containerDiv = pizzaText.parent
button = containerDiv.find_element_by_tag_name('a')
button.click()

# LOGIN
username, password = driver.find_element_by_css_selector("#txt-ac-userName"), driver.find_element_by_css_selector("#txt-ac-passWord")
username.send_keys("username")
password.send_keys("password")
loginButton = driver.find_element_by_css_selector("#main > div > div.body > div > div:nth-child(1) > div.operator-bar > div")
loginButton.click()
sleep(4)

# FIND PEPPERONI PIZZA AND CLICK ORDER
myPizza = "Pepperoni Pizza"
pizzaText = driver.find_element_by_xpath('//div[text() = "{}"]'.format(myPizza))  # uses xpath to select the pizza label element
print(pizzaText.get_attribute('outerHTML'))
# Here, we have the label that says pepperoni pizza.
# This isn't what we want though
#
# We want to click the button that says to buy
# To do that, we have to have a look at the actual structure of the page
# The label and the button are all wrapped in a bigger div. We can get the button by finding
# the label's parent and getting it's child, the button
#
# That's essentially what the following code does

containerDiv = pizzaText.find_element_by_xpath('..')
button = containerDiv.find_element_by_css_selector("a[data-mltext='p-buy']")
buttonWrapperSpan = button.find_element_by_xpath('..')
# Okay so what happens here is that it should in theory open up a modal window that allows you to tick certain options
scriptFunction = buttonWrapperSpan.get_attribute('onclick') # This is the function that opens the modal window
driver.execute_script(scriptFunction) # Execute that function

# TODO: Clean up and choose options
