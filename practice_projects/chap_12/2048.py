from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
browser = webdriver.Firefox()
browser.get("https://gabrielecirulli.github.io/2048/")
moves = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]
#ele = browser.find_element_by_class_name('game-container')
ele = browser.find_element_by_tag_name('html')
#ele = browser.find_element_by_css_selector(".game-container")

while True:
    ele.send_keys(random.choice(moves))

