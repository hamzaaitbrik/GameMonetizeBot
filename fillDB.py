import csv
import requests
import json
import names
from random import randint
from password_generator import PasswordGenerator





data = []
domains = ['gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com']
emails = []
keywords = ['happy', 'travel', 'ps4', 'fifa', 'pool', 'soccer', 'summer', 'summer 2022', '2022', 'august', 'messi']
api_url = r'https://api.pushshift.io/reddit/search/comment/?q='
scrape_urls = []
lu = []
du = {}
pg = PasswordGenerator()
pg.minlen = 8
pg.maxlen = 14
pg.excludelchars = '!~$%^&*()+\'"/'

for keyword in keywords:
    scrape_urls.append(str(api_url + keyword + '&size=100'))




def main(lu):
    get_usernames(scrape_urls)
    createEmails()
    #write2json()
    print(emails)
    write2csv()
    #print(f'Collected {len(lu)} users')


def get_usernames(scrape_urls):
    for scrape_url in scrape_urls:
        response = requests.get(scrape_url)
        data.append(json.loads(response.content.decode()))
    for dict in data:
        for i in range(99):
            #print(i)
            #print(dict['data'][i]['author'])
            if(dict['data'][i]['author'] not in lu and dict['data'][i]['author'] != 'AutoModerator'):
                #dict['data'][i]['author'].replace('_','')
                #dict['data'][i]['author'].replace('-','')
                dict['data'][i]['author'] = f"{dict['data'][i]['author']}{randint(1,10)}{randint(1,10)}{randint(1,10)}{randint(1,10)}"
                lu.append(str(dict['data'][i]['author']))
                #print(f'length is: {len(usernames)}')
    #print(f'Sending messages to {len(usernames)} users...')
    for i in range(len(lu)):
        #str(lu[i]).replace('_','').replace('-','')
        du[f'{i}'] = str(lu[i]).replace('_','').replace('-','')

def write2json():
    json_data = json.dumps(du, indent = 4)
    with open('usernames.json', 'w') as outfile:
        outfile.write(json_data)


def createEmails():
    for username in lu:
        emails.append(
            {
                'gmail':f'{str(username).replace("-","").replace("_","")}@{domains[0]}',
                'hotmail':f'{str(username).replace("-","").replace("_","")}@{domains[1]}',
                'outlook':f'{str(username).replace("-","").replace("_","")}@{domains[2]}',
                'yahoo':f'{str(username).replace("-","").replace("_","")}@{domains[3]}'
            }
        )


def write2csv():
    db = open('./db.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(db)
    #for row in writer:
    #if str(row[0]) == '':
    for dict in emails:
        for key in dict.keys():
            writer.writerow(
            [
                names.get_first_name().replace(' ',''), #db[i]['firstName'],
                names.get_last_name().replace(' ',''), #db[i]['lastName'],
                f'{names.get_first_name().replace(" ","")}{names.get_last_name().replace(" ", "")}{randint(1,10)}{randint(1,10)}', #db[i]['cdName'],
                dict[key],
                pg.generate() #db[i]['password']
            ]
        )





if __name__ == '__main__':
    main(lu)