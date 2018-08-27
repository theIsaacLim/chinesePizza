# ===STEP 2=== #

from selenium import webdriver
from time import sleep  # Sleep will pause the program
import os  # for getting the local path

dirpath = os.getcwd()  # gets local path
driver = webdriver.Chrome(dirpath + "/chromedriver")

driver.get("http://www.dominos.com.cn/menu/menu.html?menuIndex=0&RNDSEED=c42905609c237eff75c1bd6767345f43")  # dominos menu page
english = driver.find_element_by_css_selector('#lanEn > a')
english.click()  # click on english to change tha language
sleep(4)  # Wait for the website to update

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
# Okay so it looks like that works. The things is, it won't let me buy anything because I haven't signed in
