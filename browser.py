'''
Open all the desired search page in my browser. 
'''
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse


cur_window = 0


def open_newtab(driver):
    global cur_window
    if cur_window != 0:
        driver.execute_script('''window.open("","_blank");''')
        cur_window += 1
        

def open_website(driver, source, destination, date, departure_time=None):
    url = "https://www.expedia.com/Flights-Search?trip=oneway" \
         "&leg1=from:{0},to:{1},departure:{2}TANYT" \
         "&passengers=adults:1,children:0,seniors:0,infantinlap:Y" \
         "&options=cabinclass%3Aeconomy" \
         "&mode=search" \
         "&origref=www.expedia.com".format(source, destination, date)
    # response = requests.get(url)
    print 'url', url
    
    open_newtab(driver)
    driver.get(url)  # navigate to the page
    try:
        driver.find_element_by_id("leg0-evening-arrival").click()
    except :
        print "Rerying..."
        time.sleep(1)
        driver.find_element_by_id("leg0-evening-arrival").click()

    # driver.find_element_by_id("departureAirportRowContainer_DCA").click()
    # this old approach always throws 'not clickable error' because the page
    # was not fully loaded when we try to click it
    driver.find_element_by_id("leg0-evening-arrival").send_keys(Keys.SPACE)
    driver.find_element_by_id("departureAirportRowContainer_DCA").send_keys(Keys.SPACE)
    driver.find_element_by_id("departureAirportRowContainer_IAD").send_keys(Keys.SPACE)


def get_date(n, day_of_week):
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    i = 0
    loop = 0  # avoid dead lock
    curdate = today
    while loop < 100:
        curdate += oneday
        if curdate.isoweekday() == day_of_week:
            if i == n:
                return curdate
            i += 1
        loop += 1




if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('source', default="Washington, DC, United States (WAS)", 
                            help='Source airport code')
    argparser.add_argument('destination', default="Pittsburgh, PA, United States (PIT)", 
                            help='Destination airport code')
    argparser.add_argument('-t', '--time-span', default='1week', action="time_span", 
                            help='time span to search in the future')
    argparse.add_argument('-d', '--departure-time', default='evening', action='departure_time', 
                            help='morning, afternoon or evening')
    args = argparser.parse_args()
    source = args.source
    destination = args.destination
    time_span = args.time_span
    departure_time = args.departure_time


    driver = webdriver.Chrome()
    if 'week' in time_span:
        n = int(time_span[:time_span.index('week')])
        # fetch flight detail for next n week
        for i in range(n):
            # n-th Thursday
            nthu = get_date(i, 4)
            open_website(driver, source, destination, nthu.strftime("%m/%d/%Y"), 'evening')

            # n-th Friday
            nfri = nthu + datetime.timedelta(days=1)
            open_website(driver, source, destination, nfri.strftime("%m/%d/%Y"), 'evening')

            # n-th Sunday night
            nsun = nthu + datetime.timedelta(days=3)
            open_website(driver, source, destination, nsun.strftime("%m/%d/%Y"), 'evening')

    time.sleep(60*60)
    driver.close()


