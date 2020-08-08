import requests
from bs4 import BeautifulSoup
import time

today = time.strftime('%m/%d').lstrip('0')
def pttNBA(url):
    resp =requests.get(url)
    if resp.status_code !=200:
        print('URL 爆了:'+url)
        return
    soup = BeautifulSoup(resp.text,'html5lib')
    paging =soup.find('div','btn-group btn-group-paging').find_all('a')[1]['href']
    articles =[]
    rents=soup.find_all('div','r-ent')
    back=0
    for rent in rents:
        title   =rent.find('div','title').text.strip()
        count   =rent.find('div','nrec').text.strip()
        date    =rent.find('div','meta').find('div','date').text.strip()
        article = '%s %s:%s' % (today,count,title)

        try:
            if today ==date and int(count) >=30:
                articles.append(article) 
            elif today==date and int(count)<30:
                back=back+1
        except:
            if today ==date and count =='爆':
                articles.append(article)    
        
        
        
    if len(articles)!= 0:
        for article in articles:
            print(article)
        pttNBA('https://www.ptt.cc' + paging)
    elif len(articles)== 0 and back != 0:
        pttNBA('https://www.ptt.cc' + paging)
        back=back-1
    else:
        return 
    
pttNBA('https://www.ptt.cc/bbs/NBA/index6502.html')  

