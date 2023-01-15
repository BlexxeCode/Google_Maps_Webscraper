import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import pandas as pd
import time
from datetime import date

driverPATH = 'C://Users//andki//Downloads//chromedriver_win32'
browser = 'C://Users//andki//AppData//Local//Vivaldi//Application//vivaldi.exe'

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name('C://Users//andki//OneDrive//Documents//credentials.json')
file = gspread.authorize(credentials)
sheet = file.open('Test')
sheet = sheet.sheet1
sheet.update_acell('F1', 'Date Lead Entered')
sheet.update_acell('G1', 'Lead or Client')
sheet.update_acell('H1', 'Contact Name')
sheet.update_acell('I1', 'Phone')
sheet.update_acell('J1', 'Email')
sheet.update_acell('K1', 'Type of Business')
sheet.update_acell('L1', 'Source')
sheet.update_acell('M1', 'Business Name')
sheet.update_acell('N1', 'Website')
sheet.update_acell('O1', 'Address')
sheet.update_acell('P1', 'City')
sheet.update_acell('Q1', 'State')
sheet.update_acell('R1', 'Zip')


options = webdriver.ChromeOptions()
options.binary_location = browser

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm'
driver.get(url)
time.sleep(5)
driver.find_element('css selector', 'div.g-c-Hf').click()

time.sleep(10)

url = 'https://www.google.com/search?sa=X&tbs=lrf:!1m4!1u45!2m2!46m1!1e1!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e3!2m4!1e2!5m2!2m1!2e4!3sIAE,lf:1,lf_ui:2&tbm=lcl&sxsrf=AJOqlzUaw3QOERQtCi9Bx_tWm6BYi1UzWQ:1673579134871&q=healthcare%20offices%20in%20brooklyn&rflfq=1&num=10&ved=2ahUKEwj9y8KWyMP8AhWvEVkFHVvlCgAQwywoBnoECAMQFg&biw=1090&bih=722&dpr=1.25&rlfi=hd:;si:&rlst=f'
driver.get(url)
time.sleep(5)

num = 2

for i in range(4, 43, 2):
    driver.find_element('xpath', '/html/body/div[6]/div/div[9]/div[1]/div/div[2]/div['
                                 '2]/div/div/div/div/div/div/div/div/div[1]/div[4]/div['
                                 '' + str(i) + ']/div/div/div/a/div/div/div[1]/span').click()
    time.sleep(10)
    name = driver.find_element('css selector', 'div.SPZz6b')
    print(name.text)

    address = driver.find_element('css selector', 'span.LrzXr')
    spl_address = address.text.split(',')
    try:
        Btype = driver.find_element('xpath',
                                    '/html/body/div[6]/div/div[9]/div[2]/div/div[2]/async-local-kp/div/div/div['
                                    '1]/div/g-sticky-content-container/div/block-component/div/div[1]/div/div/div/div['
                                    '1]/div/div/div[1]/div/div[2]/div[2]/div')
        web = driver.find_element('css selector', 'a.dHS6jb').get_attribute('href')
        phone = driver.find_element('css selector', 'a.Od1FEc.dHS6jb').get_attribute('data-phone-number')

        sheet.update_acell('F'+str(num), str(date.today()))
        sheet.update_acell('G'+str(num), 'Lead')
        sheet.update_acell('H'+str(num), ' ')
        sheet.update_acell('I'+str(num), phone)
        sheet.update_acell('J'+str(num), '')
        sheet.update_acell('K'+str(num), Btype.text)
        sheet.update_acell('L'+str(num), 'Google Maps')
        sheet.update_acell('M'+str(num), name.text)
        sheet.update_acell('N'+str(num), web)
        sheet.update_acell('O'+str(num), spl_address[0])
        sheet.update_acell('P'+str(num), spl_address[-2])
        sheet.update_acell('Q'+str(num), 'NY')
        sheet.update_acell('R'+str(num), address.text[-5:])

    except selenium.common.exceptions.NoSuchElementException as e:
        continue

    print(Btype.text)
    print(address.text)
    print(web)
    print(phone)
    print('-' * 30)
    num += 1
driver.find_element('css selector', 'span.SJajHc.NVbCr').click()
time.sleep(5)

p = 0
while p < 11:
    for i in range(4, 43, 2):
        driver.find_element('xpath', '/html/body/div[6]/div/div[9]/div[1]/div/div[2]/div['
                                     '2]/div/div/div/div/div/div/div/div/div/div[1]/div[4]/div['
                                     '' + str(i) + ']/div/div/div/a/div/div/div[1]/span').click()
        time.sleep(10)
        name = driver.find_element('css selector', 'div.SPZz6b')
        print(name.text)

        address = driver.find_element('css selector', 'span.LrzXr')
        spl_address = address.text.split(',')
        try:
            Btype = driver.find_element('xpath',
                                        '/html/body/div[6]/div/div[9]/div[2]/div/div[2]/async-local-kp/div/div/div['
                                        '1]/div/g-sticky-content-container/div/block-component/div/div['
                                        '1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div')
            web = driver.find_element('css selector', 'a.dHS6jb').get_attribute('href')
            phone = driver.find_element('css selector', 'a.Od1FEc.dHS6jb').get_attribute('data-phone-number')

            sheet.update_acell('F' + str(num),str(date.today()))
            sheet.update_acell('G' + str(num), 'Lead')
            sheet.update_acell('H' + str(num), ' ')
            sheet.update_acell('I' + str(num), phone)
            sheet.update_acell('J' + str(num), '')
            sheet.update_acell('K' + str(num), Btype.text)
            sheet.update_acell('L' + str(num), 'Google Maps')
            sheet.update_acell('M' + str(num), name.text)
            sheet.update_acell('N' + str(num), web)
            sheet.update_acell('O' + str(num), spl_address[0])
            sheet.update_acell('P' + str(num), spl_address[-2])
            sheet.update_acell('Q' + str(num), 'NY')
            sheet.update_acell('R' + str(num), address.text[-5:])

        except selenium.common.exceptions.NoSuchElementException as e:
            continue

        print(Btype.text)
        print(address.text)
        print(web)
        print(phone)
        print('-' * 30)
        num += 1
    driver.find_element('css selector', 'a#pnnext').click()
    time.sleep(5)

    p += 1