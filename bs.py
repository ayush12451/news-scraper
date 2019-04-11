# -*- coding: utf-8 -*-
"""
Created on Tue Apr 09 23:48:14 2019

@author: Ayush
"""
from bs4 import BeautifulSoup 
import requests

def get_latest_news():
    #fetch webpage
    page=requests.get("https://www.gadgetsnow.com/?utm_source=toiweb&utm_medium=referral&utm_campaign=toiweb_hptopnav")
    soup = BeautifulSoup(page.content, 'html.parser')

    #find the division titled latest news
    l=soup.find("div",class_="latest_news")

    l3=[]

    #find all the links to the news
    for a in l.find_all('a', href=True):
        l3.append(a['href']) 

    #write these links to a text file
    f=open('news_link.txt','a')
    f.truncate(0)
    for line in l3:
        if line[0]=="/":
            temp="https://www.gadgetsnow.com"+line
            f.write(temp+"\n")
