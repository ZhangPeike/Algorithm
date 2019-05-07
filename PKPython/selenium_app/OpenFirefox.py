#!/usr/bin/python2
print "Hello python2, hello selenium"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.python.org")
# print driver.tilte