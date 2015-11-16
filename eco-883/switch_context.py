#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import os
import sys
from appium import webdriver

#Retreiving enviroment variables
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

desired_capabilities = {}
desired_capabilities['platformName'] = 'iOS'
desired_capabilities['platformVersion'] = '9.0'
desired_capabilities['browserName'] = 'safari'
desired_capabilities['deviceName'] = 'iPhone Simulator'
# desired_capabilities['appium-version'] = '1.4.15beta1'
desired_capabilities['appiumVersion'] = {'appium-url': 'v1.4.15beta1.tar.bz2'}
# appiumVersion: {"appium-url": "arbitraryurl"}`
desired_capabilities['device-orientation'] = 'portrait'
desired_capabilities['name'] = 'switchingContext'
# desired_capabilities['proxy'] = {"proxyAutoconfigUrl": "http://127.0.0.1:19876/pac.js", "proxyType":"PAC"}

driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = desired_capabilities)
# driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = desired_capabilities)
# driver = webdriver.Remote(command_executor = ('http://localhost:4723/wd/hub'),  desired_capabilities = desired_capabilities)

driver.implicitly_wait(30)


driver.get("https://www.google.com/")
print driver.contexts

time.sleep(10)

driver.switch_to.context ("NATIVE_APP")
print driver.contexts

time.sleep(10)

driver.switch_to.context ("WEBVIEW_1")
print driver.contexts

# time.sleep(10)

# driver.switch_to.context ("NATIVE_APP")
# driver.contexts

driver.quit()
