# Google_Maps_Webscraper


This is a python webscraper extracts information from Google Maps using the webscraping library Selenium. Using CSS elements and xpaths, specific information about certain businesses such as name, address, type, phone number, etc is extracted form each business in the list. For this script, achrome is used and depending on which version chrome or chromium based broswer is used, a specfic chromedriver file will be needed. In this case I used Vivaldi so I had to specify the browser .exe file as well as use the right chromedriver.   
The webdriver_manager library can be used, however it may cause some issues if you used anything other than Chrome, so as a surefire method, use this link to get a specific driver: 
https://chromedriver.chromium.org/downloads

To use this, a Google Maps link of a certain type of business is used and automatically goes through each lsiting until it reaches the number specified by the max number given by the user. 

Once the informationm is extracted for each one, the info is saved, with is done in either excel or a SQL database, depending on the python script. For both excel and SQL, a sheet/table was made beforehand and the information was inserted into the table.
