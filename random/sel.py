from selenium import webdriver
browser = webdriver.Firefox()
print(type(browser))
#<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
browser.get('https://inventwithpython.com')