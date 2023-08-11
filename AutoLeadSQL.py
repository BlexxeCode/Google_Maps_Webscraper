import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector
import pandas as pd
from datetime import date
import time

# future additions
#  prompt to input maps url, business type, amount of businesses
#  turn into executable


cnx = mysql.connector.connect(user='root', password='password@12',
                              host='localhost', database='business_lead')
cursor = cnx.cursor()
if cnx:
    print('Connected')

browser = 'C://Users//andki//AppData//Local//Vivaldi//Application//vivaldi.exe'
options = webdriver.ChromeOptions()
options.binary_location = browser

Type = input('Type of locations?')
url2 = input("Google Maps URL")
Max = int(input('Amount of locations to obtain info from?'))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url1 = 'https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm'
driver.get(url1)
time.sleep(5)
driver.find_element('css selector', 'div.g-c-Hf').click()

time.sleep(10)
driver.get(url2)
time.sleep(8)

add_business = "INSERT INTO leads(Date_entered,Busniess_Name,Business_Type,Phone,Address,City,State,Zip,Source)" \
               "VALUES(%(Date_entered)s, %(Busniess_Name)s, %(Business_Type)s, %(Phone)s, %(Address)s, %(City)s, " \
               "%(State)s, %(Zip)s, %(Source)s)"
p = 1
while p <= Max:
    list = driver.find_elements('css selector', 'div.dbg0pd')
    print(len(list))
    
    for bis in list:
        if bis.text == '':
            continue
        bis.click()
        time.sleep(3)

        try:
            name = driver.find_element('css selector', 'div.SPZz6b')
            print(name.text)

            address = driver.find_element('css selector', 'span.LrzXr')
            spl_address = address.text.split(',')

            phone = driver.find_element('css selector', 'a.Od1FEc.mI8Pwc').get_attribute('data-phone-number')

            webtest = driver.find_elements('css selector', 'a.mI8Pwc')
            if len(webtest) == 2:
                web = webtest[-2].get_attribute('href')
            else:
                web = 'N/A'
        except selenium.common.exceptions.NoSuchElementException as e:
            continue
        try:
            Btype = driver.find_element('css selector', 'span.YhemCb').text
        except selenium.common.exceptions.NoSuchElementException as e:
            Btype = Type

        if len(spl_address) < 2:
            city = spl_address[0]
        else:
            city = spl_address[-2]
        data = {
            'Date_entered': str(date.today()),
            'Busniess_Name': name.text,
            'Business_Type': Btype,
            'Phone': phone,
            'Address': spl_address[0],
            'City': city,
            'State': 'NY',
            'Zip': int(address.text[-5:]),
            'Source': 'Google Maps',

        }
        cursor.execute(add_business, data)
        cnx.commit()

        print(Btype)
        print(address.text)
        print(web)
        print(phone)
        print('-' * 30)
        p += 1
        if p > Max:
            break
    driver.find_element('css selector', 'a#pnnext').click()
    time.sleep(5)

cursor.close()
cnx.close()
