import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

url = "https://www.expedia.com/Flights-Search?trip=oneway&leg1=from:Washington, DC, United States (WAS),to:Pittsburgh, PA, United States (PIT),departure:11/02/2017TANYT&passengers=adults:1,children:0,seniors:0,infantinlap:Y&options=cabinclass%3Aeconomy&mode=search&origref=www.expedia.com"
# response = requests.get(url)
print 'url', url
driver = webdriver.Chrome()  # replace with .Firefox(), or with the browser of your choice

driver.get(url)  # navigate to the page

driver.find_element_by_id("leg0-evening-arrival").send_keys(Keys.SPACE)
driver.find_element_by_id("departureAirportRowContainer_DCA").send_keys(Keys.SPACE)
driver.find_element_by_id("departureAirportRowContainer_IAD").send_keys(Keys.SPACE)


driver.find_element_by_id("leg0-evening-arrival").click()
driver.find_element_by_id("departureAirportRowContainer_DCA").click()
driver.find_element_by_id("departureAirportRowContainer_IAD").click()

# open new tab
cur_window = 0
driver.execute_script('''window.open("","_blank");''')
# move to next tab
cur_window += 1
windows = driver.window_handles
driver.switch_to.window(windows[cur_window])
# open new url in new tab
driver.get("http://www.google.com")