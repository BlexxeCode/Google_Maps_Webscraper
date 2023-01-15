import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl
from openpyxl import Workbook
import pandas as pd
from datetime import date
import time

driverPATH = 'C://Users//andki//Downloads//chromedriver_win32'
browser = 'C://Users//andki//AppData//Local//Vivaldi//Application//vivaldi.exe'

path = 'C://Users//andki//OneDrive//Documents//Leads.xlsx'
wb = openpyxl.load_workbook(path)
ws = wb.active

options = webdriver.ChromeOptions()
options.binary_location = browser

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm'
driver.get(url)
time.sleep(5)
driver.find_element('css selector', 'div.g-c-Hf').click()

time.sleep(10)

url = 'https://www.google.com/search?tbs=lrf:!1m4!1u45!2m2!46m1!1e1!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e3' \
      '!2m4!1e2!5m2!2m1!2e4!3sIAE,lf:1,lf_ui:2&tbm=lcl&sxsrf=AJOqlzWAxjShFy5uytqcENhYnWFjG_PJlQ:1673569245515&q' \
      '=healthcare%20offices%20in%20manhattan&rflfq=1&num=10&sa=X&ved=2ahUKEwjij6mqo8P8AhVaF1kFHW7-AjEQwywoBnoECAMQFg' \
      '&cshid=1673569258941226&biw=1536&bih=722&dpr=1.25&rlfi=hd:;si:&rlst=f '
driver.get(url)
time.sleep(5)

num = 209

for i in range(4, 43, 2):
    driver.find_element('xpath', '/html/body/div[6]/div/div[9]/div[1]/div/div[2]/div['
                                 '2]/div/div/div/div/div/div/div/div/div[1]/div[4]/div['
                                 '' + str(i) + ']/div/div/div/a/div/div/div[1]/span').click()
    time.sleep(3)
    name = driver.find_element('css selector', 'div.SPZz6b')
    print(name.text)

    address = driver.find_element('css selector', 'span.LrzXr')
    spl_address = address.text.split(',')
    try:
        Btype = driver.find_element('xpath',
                                    '/html/body/div[6]/div/div[9]/div[2]/div/div[2]/async-local-kp/div/div/div['
                                    '1]/div/g-sticky-content-container/div/block-component/div/div[1]/div/div/div/div['
                                    '1]/div/div/div[1]/div/div[2]/div[2]/div')
        web = driver.find_element('xpath', '/html/body/div[6]/div/div[9]/div[2]/div/div['
                                           '2]/async-local-kp/div/div/div['
                                           '1]/div/g-sticky-content-container/div/block-component/div/div['
                                           '1]/div/div/div/div[1]/div/div/div[4]/c-wiz/div/div/a[1]').get_attribute(
            'href')
        phone = driver.find_element('css selector', 'a.Od1FEc.dHS6jb').get_attribute('data-phone-number')

        ws['F' + str(num)].value = str(date.today())
        ws['F' + str(num)].value = 'Lead'
        ws['I' + str(num)].value = phone
        ws['J' + str(num)].value = ''
        ws['K' + str(num)].value = Btype.text
        ws['L' + str(num)].value = 'Google Maps'
        ws['M' + str(num)].value = name.text
        ws['N' + str(num)].value = web
        ws['O' + str(num)].value = spl_address[0]
        ws['P' + str(num)].value = spl_address[-2]
        ws['Q' + str(num)].value = 'NY'
        ws['R' + str(num)].value = address.text[-5:]

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
        time.sleep(3)
        name = driver.find_element('css selector', 'div.SPZz6b')

        address = driver.find_element('css selector', 'span.LrzXr')
        spl_address = address.text.split(',')
        try:
            Btype = driver.find_element('xpath',
                                        '/html/body/div[6]/div/div[9]/div[2]/div/div[2]/async-local-kp/div/div/div['
                                        '1]/div/g-sticky-content-container/div/block-component/div/div['
                                        '1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/div')
            web = driver.find_element('xpath', '/html/body/div[6]/div/div[9]/div[2]/div/div['
                                               '2]/async-local-kp/div/div/div['
                                               '1]/div/g-sticky-content-container/div/block-component/div/div['
                                               '1]/div/div/div/div[1]/div/div/div[4]/c-wiz/div/div/a['
                                               '1]').get_attribute('href')
            phone = driver.find_element('css selector', 'a.Od1FEc.dHS6jb').get_attribute('data-phone-number')

            ws['A' + str(num)].value = phone
            ws['B' + str(num)].value = ''
            ws['C' + str(num)].value = Btype.text
            ws['D' + str(num)].value = 'Google Maps'
            ws['E' + str(num)].value = name.text
            ws['F' + str(num)].value = web
            ws['G' + str(num)].value = spl_address[0]
            ws['H' + str(num)].value = spl_address[-2]
            ws['I' + str(num)].value = 'NY'
            ws['J' + str(num)].value = int(address.text[-5:])

        except selenium.common.exceptions.NoSuchElementException as e:
            continue
        print(name.text)

        print(Btype.text)
        print(address.text)
        print(web)
        print(phone)
        print('-' * 30)
        num += 1
        wb.save('C://Users//andki//OneDrive//Documents//Leads.xlsx')
    driver.find_element('css selector', 'a#pnnext').click()
    time.sleep(5)

    p += 1
