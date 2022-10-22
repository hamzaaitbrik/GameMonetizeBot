import csv
from selenium import webdriver
#from db import db
from time import sleep
from random import uniform
from selenium.webdriver.common.by import By
#from sqlalchemy import null


driver = webdriver.Chrome('C:\\Users\\mehdi\\Desktop\\chromedriver')
db = []




#def writeCSV(db):
#    with open('dbCreated.csv', 'w') as created:
#        dbWriter = csv.writer(created, delimiter=',')
#        for row in dbWriter:


def dbFill():
    with open('db.csv', 'r') as database:
        dbReader = csv.reader(database, delimiter=',')
        for row in dbReader:
            db.append(
                {
                    'firstName':str(row[0]).replace(' ', ''),
                    'lastName':str(row[1]).replace(' ', ''),
                    'cdName':str(row[2]).replace(' ', ''),
                    'email':str(row[3]).replace(' ', ''),
                    'password':str(row[4]).replace(' ', '')
                }
            )


def registration(db):
    for i in range(len(db) + 1):
        #driver.get('https://gamemonetize.com/')
        #sleep(uniform(1,2.2))
        #driver.find_element(By.XPATH, '/html/body/header/div/div/a[3]').click()
        driver.get('https://gamemonetize.com/account/register.php')
        sleep(uniform(1,2.2))
        driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div/div/div/div/div[2]/div/form/input[1]').send_keys(db[i]['firstName'])
        sleep(uniform(1,2.2))
        driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div/div/div/div/div[2]/div/form/input[2]').send_keys(db[i]['lastName'])
        sleep(uniform(1,2.2))
        driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div/div/div/div/div[2]/div/form/input[3]').send_keys(db[i]['cdName'])
        sleep(uniform(1,2.2))
        driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div/div/div/div/div[2]/div/form/input[4]').send_keys(db[i]['email'])
        sleep(uniform(1,2.2))
        driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div/div/div/div/div[2]/div/form/input[5]').send_keys(db[i]['password'])
        sleep(uniform(1,2.2))
        driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div/div/div/div/div[2]/div/form/button').click()
        sleep(uniform(1,2.2))
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[3]/a').click()
        sleep(uniform(1,2.2))
        driver.delete_all_cookies()
        #sleep(uniform(1,2.2))
        #driver.close()
        sleep(uniform(10,20))
        #del db[i]
        #tempList = []
        dbCreated = open('./dbCreated.csv', 'a', newline='', encoding='utf-8')
        writer = csv.writer(dbCreated)
        #for row in writer:
            #if str(row[0]) == '':
        writer.writerow(
            [
                db[i]['firstName'],
                db[i]['lastName'],
                db[i]['cdName'],
                db[i]['email'],
                db[i]['password']
            ]
        )




def main():
    dbFill()
    registration(db)





if(__name__ == '__main__'):
    main()
