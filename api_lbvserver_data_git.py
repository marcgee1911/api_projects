#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from requests.auth import HTTPBasicAuth
import json

#functon to pull username from txt file on local machine
def get_username():
    f = open('c:/projects/ad_username.txt', 'r')
    my_username = f.read().strip()
    return my_username
    f.close()

#functon to pull password from txt file on local machine   
def get_passwd():
    f = open('c:/projects/ad_pausewd.txt', 'r')
    my_passwd = f.read().strip()
    return my_passwd
    f.close()

#assigning the username and password to a variable by calling upon the function
username = get_username()
passwd = get_passwd()

#assigning the variable url to the URL of the API
url =  "https://1.2.3.40/nitro/v1/stat/lbvserver"


myResponse = requests.get(url,auth=HTTPBasicAuth((username), (passwd)), verify=False)

jData = json.loads(myResponse.content)

for key in jData:
    print (str(key) + " : " + str(jData[key]))      



# In[ ]:




