# ===STEP 1=== #

# downloads:
#   selenium - pip install selenium
#   selenium driver- here i'm using firefox driver(gecko)
#   https://www.seleniumhq.org/download/
from selenium import webdriver
import os  # for getting the local path

dirpath = os.getcwd()  # gets local path
driver = webdriver.Chrome(dirpath + "/chromedriver")

driver.get("http://www.dominos.com.cn/menu/menu.html?menuIndex=0&RNDSEED=c42905609c237eff75c1bd6767345f43")  # dominos menu page
english = driver.find_element_by_css_selector('#lanEn > a')
english.click()  # click on english to change tha language

# TODO: order pizza!
