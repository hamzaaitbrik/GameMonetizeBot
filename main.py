import csv
from typing import List
#import js2py
import pyautogui as pyag
#from webbrowser import Chrome
from selenium import webdriver
from time import sleep
from random import uniform, randint
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By




webdriver = webdriver.Chrome('C:\\Users\\Admin23\\Desktop\\chromedriver')
uploadAccounts = []
uploadGames = []
categoriesn = []
tagsn = []




# JS
#zipElementClick = r'document.getElementById("recommendationDiv4").click()'
#screenshot1ElementClick = r'document.getElementById("recommendationDiv").click()'
#screenshot2ElementClick = r'document.getElementById("recommendationDiv1").click()'
#screenshot3ElementClick = r'document.getElementById("recommendationDiv2").click()'




def uploadFiles(x, y, filePath):
    pyag.click(x,y)
    sleep(uniform(2.5,5))
    pyag.write(str(filePath))
    sleep(uniform(2.5,5))
    pyag.press('enter')


def accountsFill():
    with open('dbCreated.csv', 'r') as accounts:
        accountsReader = csv.reader(accounts, delimiter=',')
        for row in accountsReader:
            uploadAccounts.append(
                {
                    'email':str(row[3]).replace(' ', ''),
                    'pass':str(row[4]).replace(' ', '')
                }
            )



def gamesFill():
    with open('games.csv', 'r') as games:
        gamesReader = csv.reader(games, delimiter=',')
        for row in gamesReader:
            uploadGames.append(
                {
                    'name':str(row[0]),#.replace(' ', ''),
                    'description':str(row[1]),#.replace(' ', ''),
                    'controls':str(row[2]),#.replace(' ', ''),
                    'screenshot#1Path':str(row[3]).replace(' ', ''),
                    'screenshot#2Path':str(row[4]).replace(' ', ''),
                    'screenshot#3Path':str(row[5]).replace(' ', ''),
                    'zipPath':str(row[6]).replace(' ', '')
                }
            )

# #categories = 20
# #tags = 544

def select(xpath, n):
    sleep(uniform(0.2,1))
    Select(webdriver.find_element(By.XPATH, xpath)).select_by_index(n)
    sleep(uniform(0.2,1))

def generate(start, finish, list, listlen):
    r = randint(start, finish)
    if(r not in list):
        list.append(r)
    if(len(list) != listlen):
        generate(start, finish, list, listlen)
    return list


# upload zip x = 305,740
# upload zip y = 400,500

# upload screenshot#1 x = 830,960
# upload screenshot#1 y = 320,500

# upload screenshot#2 x = 985,1120
# upload screenshot#2 y = 320,500

# upload screenshot#3 x = 1145,1275
# upload screenshot#3 y = 320,500



def uploadProcess():
    for account in uploadAccounts:
        webdriver.get('https://gamemonetize.com/account/login.php')
        webdriver.maximize_window()
        sleep(uniform(2.5,5))
        webdriver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div/div/div/div/div[2]/div[1]/form/input[1]').send_keys(account['email'])
        sleep(uniform(1.5,5))
        webdriver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div/div/div/div/div[2]/div[1]/form/input[2]').send_keys(account['pass'])
        sleep(uniform(2.5,5))
        webdriver.find_element(By.XPATH, '/html/body/main/section/div/div/div/div/div/div/div/div/div[2]/div[1]/form/button').click() # Login
        sleep(uniform(2.5,5))
        for game in uploadGames:
            #webdriver.get('https://gamemonetize.com/account/login.php')
            #sleep(uniform(0.2,1))
            sleep(uniform(2.5,5))
            webdriver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[1]/a').click() # Add Game
            sleep(uniform(5,10))
            webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/form/div/div[1]/div/div/input').send_keys(game['name'])
            sleep(uniform(2.5,5))
            webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/form/div/div[2]/button').click() # Add Game 2
            sleep(uniform(5,10))
            uploadFiles(randint(305,740), randint(400,500), game['zipPath']) # Upload Zip
            sleep(uniform(30,50))
            uploadFiles(randint(830,960), randint(320,500), game['screenshot#1Path']) # Upload Screenshot#1
            sleep(uniform(30,50))
            uploadFiles(randint(985,1120), randint(320,500), game['screenshot#2Path']) # Upload Screenshot#2
            sleep(uniform(30,50))
            uploadFiles(randint(1145,1275), randint(320,500), game['screenshot#3Path']) # Upload Screenshot#3
            sleep(uniform(5,10))
            #webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/form/div/div[2]/button').click() # Add Game 2
            #sleep(uniform(5,10))
            #Select(webdriver.find_element_by_xpath('/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/form[2]/span[1]/span[1]/span/ul')).select_by_index(2)
            webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/form[2]/textarea[1]').send_keys(game['description']) # Add Description
            sleep(uniform(2.5,5))
            webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/form[2]/textarea[2]').send_keys(game['controls']) # Add Controls
            sleep(uniform(2.5,5))
            webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/form[2]/label[4]/div/label').click() # Optimized for Mobile Devices
            #sleep(uniform(2.5,5))
            #Select(webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/form[2]/select[1]')).select_by_index(2) # Select Categories
            #sleep(uniform(2.5,5))
            #Select(webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/form[2]/select[1]')).select_by_index(1) # Select Categories
            #sleep(uniform(2.5,5))
            #Select(webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/form[2]/select[2]')).select_by_index(3) # Select Tags
            #sleep(uniform(2.5,5))
            generate(1, 20, categoriesn, 2) # Generating 2 Categories
            for categoryn in categoriesn: # Add Categories
                select('/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/form[2]/select[1]', categoryn)
            generate(1, 367, tagsn, 68) # Generating 68 Tags
            for tagn in tagsn:
                select('/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/form[2]/select[2]', tagn)
            #select('/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/form[2]/select[1]', n = randint(1,20)) # Add Category #1
            #webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[2]/div[1]/form').click() #.send_keys(game['screenshot#1Path']) #Upload Screenshot#1
            #js2py.eval_js(zipElementClick)
            #uploadFiles(screenshot1ElementClick, game['screenshot#1Path']) # Upload Screenshot#1
            #sleep(uniform(2.5,5))
            #webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/form').send_keys(game['screenshot#2Path']) # Upload Screenshot#2
            #uploadFiles(screenshot2ElementClick, game['screenshot#2Path']) # Upload Screenshot#2
            #sleep(uniform(2.5,5))
            #webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[2]/div[3]/form').send_keys(game['screenshot#3Path']) # Upload Screenshot#3
            #uploadFiles(screenshot3ElementClick, game['screenshot#3Path']) # Upload Screenshot#3
            #sleep(uniform(2.5,5))
            #webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/form[1]').send_keys(game['zipPath']) # Upload zip
            #uploadFiles(zipElementClick, game['zipPath']) # Upload Zip
            #sleep(uniform(5,10))
            #webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[1]/input').click() # Request Activation
            webdriver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[3]/div/div[2]/div/div/div/div[1]/form[2]/button').click() # Save Changes
            sleep(uniform(2.5,5))
            #webdriver.Chrome.execute_script('console.log("Hello world!")')



def main():
    accountsFill()
    gamesFill()
    uploadProcess()









if __name__ == '__main__':
    main()