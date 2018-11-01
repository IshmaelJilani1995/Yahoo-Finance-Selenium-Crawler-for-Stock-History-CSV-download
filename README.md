# Yahoo-Finance-Selenium-Crawler-for-Stock-History-CSV-download
Yahoo! Finance Selenium Crawler for Stock History CSV download
Yahoo! Finance famously disabled their API. You can still, however, download their historical data and other information 
by scraping their site for financial analysis purposes.
This crude, but functional and to be improved, selenium scraper performs this task and I have scraped hundreds of CSVs using it.

# The code is commented and self explanatory apart from the following:

1. For the JSON file, the tickers were imported as text via copy and paste from an excel file available at 
http://investexcel.net/all-yahoo-finance-stock-tickers/ and the following REGEX was applied in Visual studio code to generate a list:

^([A-Za-z]+)$ - in search
"$1", - in replace
add a [ to the start of the list, remove the , and add a ] to the end of the list.

You click ctrl-F and ctrl-H to bring up the boxes in VSC and click the square star symbol just to the far left of the find box to allow the entering of regex

I've used this Regex many times and cannot remember where I originally learnt it from - it's pretty common. It was not my own creation, 
I have simply remembered it from other opensource users.

2.Right click inspect element in Firefox to find the class variables/Xpaths or whatever else is required to locate elements.

3.I deleted the code which was used to debug the system. I don't feel this needs a seperate debugger, it's pretty basic 
and the basic debugging can be done ad hoc by anyone if they needs it.


# Tried for reference:

-To use beautiful soup. Didn't work due to the redirection and the cookie. Probably is a way to make it work, I just felt this would be easier.

-To use Xpaths and inbuilt selenium functions for clicking links/buttons rather than the short Javascript scripts. However, selenium waits for the site to load and this can take "forever" in this instance

-the machine i was running this on was particularly slow aswell, probably contributed to this problem.
To send the link directly, but you need a cookie.

-Set the settings ,which are declared in the code for firefox download habits, permanently through firefox GUI didn't seem to work for the driver.

# Planned Improvements (required to support larger volume than what I used it for which was around 200 CSV's):

0.Add a exception catcher so the system may continue even when it hits an error.

1.Remove the timers and replace it with a check for the element to load instead

2.Have the tickers removed from the list if downloaded so that the process can be interrupted without having to start from the beginning

3.Access history to set period to max

4.Create concurrency for multi-core computers and potential multiple threads/ mutex etc.

5.Create networking for multiple computers

6. Remove images/CSS for quicker loading times
The above I know is possible, below i'm not sure how to approach but shall think about

7?. Dynamically request a cookie so download is possible without browser?
7?. A "shadow" browser?

# Credit to:
http://investexcel.net/all-yahoo-finance-stock-tickers/ for the ticker list
