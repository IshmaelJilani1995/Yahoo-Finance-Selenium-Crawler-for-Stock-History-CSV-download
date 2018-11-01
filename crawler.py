import time
from selenium import webdriver as wd 
import json

#setting firefox profile to not throw dialog and so save to disk for csvs
profile = wd.FirefoxProfile()
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', "text/csv")


#open tickers.json and load it as tickers
with open("tickers.json", "r") as tickersjson:
    tickers = json.load(tickersjson)

#iterate through each ticker
for i in range(len(tickers)):
    ticker = tickers[i]
    #setup webdriver as driver with profile above
    driver = wd.Firefox(firefox_profile=profile)
    #navigate to link, which is modified for only the period of time for AAPL
    driver.get("https://uk.finance.yahoo.com/quote/"+ticker+"/history?period1=345427200&period2=1540944000&interval=1d&filter=history&frequency=1d")
    #crude delay timer (will replace later with waiting for element)
    time.sleep(10) 
    #javascript script to find and click element by class name
    driver.execute_script("document.getElementsByClassName('btn btn-primary agree')[0].click()")
    print("Navigated Oath for " +ticker) #basic verification
    time.sleep(10) 
    driver.execute_script("document.getElementsByClassName('Fl(end) Mt(3px) Cur(p)')[0].click()")
    print("Clicked download Link for " +ticker) 
    time.sleep(10) #waiting for download to complete... hopefully
    driver.close()
