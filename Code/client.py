#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

def get_article_price(article,color,week):
    #define parameters and url
    parameters = {'article':article,'color':color,'week':week}
    #api_url = "https://jsonplaceholder.typicode.com/todos"
    api_url = "http://127.0.0.1:5000/price"
    try:
        #get the response
        response = requests.get(api_url,parameters)
        print(response.url)
        #if the request succeeded
        if(response.status_code == 200):
            print(response.json())
        else:
            print("An error occurred")
    except:
        print("An exception occurred")
    
get_article_price(1,2,1)

