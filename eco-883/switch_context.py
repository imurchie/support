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
desired_capabilities['appiumVersion'] = {'appium-url': 'https://github.com/imurchie/support/blob/master/eco-883/appium-v1.4.15beta1.tar.bz2?raw=true'}
desired_capabilities['device-orientation'] = 'portrait'
desired_capabilities['name'] = 'switchingContext'
# desired_capabilities['proxy'] = {"proxyAutoconfigUrl": "http://127.0.0.1:19876/pac.js", "proxyType":"PAC"}

driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = desired_capabilities)
# driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = desired_capabilities)
# driver = webdriver.Remote(command_executor = ('http://localhost:4723/wd/hub'),  desired_capabilities = desired_capabilities)

driver.implicitly_wait(30)


# driver.get("https://www.google.com/")
url = 'http://davmagic.com/PAGES67.html'
driver.get(url)
print driver.contexts

time.sleep(10)

c_url = driver.current_url
print c_url
if (c_url != url):
  time.sleep(5)

driver.switch_to.context("NATIVE_APP")
print driver.contexts

# time.sleep(10)

driver.switch_to.context("WEBVIEW_1")
print driver.contexts

# time.sleep(10)

# driver.switch_to.context ("NATIVE_APP")
# driver.contexts

driver.quit()
