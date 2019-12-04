import requests
import os
import random
import string
import sys

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
url = sys.argv[1]
names = open("names.txt", 'r').read().split('\n')
run = 1
userField = sys.argv[2]
passField = sys.argv[3]


while run == 1:
    for name in names:
        name_extra = ''.join(random.choice(string.digits))
        mails = ['@yahoo.com', '@gmail.com', '@hotmail.com', '@aol.com', '@mail.ru', '@outlook.com', '@scam.gg']
        username = name.lower() + name_extra + random.choice(mails)
        password = ''.join(random.choice(chars) for i in range(8))
        r = requests.post(url, data={
            userField: username,
            passField: password
        })
        #print(r.status_code)
        if r.status_code != 200:
            run = 0
            print("SOMETHING GONE HORRIBLY WRONG!")
        print('Sending username %s and password %s' % (username, password))
