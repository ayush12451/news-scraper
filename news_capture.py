from bs4 import BeautifulSoup
import requests
from bs import get_latest_news

# call the function to create a file containing a list of links
get_latest_news()

f=open("news_link.txt",'r')
f2=open("news.txt",'a')
f2.truncate(0) #clears the previous content from the file

for line in f:
    
    page = requests.get(line.rstrip()) #rstrip removes \n from the string
    soup = BeautifulSoup(page.content,'html.parser')
    l = soup.find('div',class_='Normal')
    #encode function decodes the html text
    f2.write(l.get_text().encode('utf-8').strip())
    f2.write("\n\n next news:\n\n")
f.close()
f2.close()
