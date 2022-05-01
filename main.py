# importing libraries 
import requests
from bs4 import BeautifulSoup


# website 
url = "https://www.freethink.com/articles"

# passing headers 
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}

class notifi:
    def article():
        article=[0]
        datas=[]
    def check():
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.content,'html.parser')
        

        # each section of article 
        for i in soup.find_all('div',class_="mb-10"):
            print("\n")
            temp=[]
            # saving temp data 

            title = ""
            img_link=""
            # scrapping title 
            for j in i.find("a",class_="block mb-4 text-2xl text-black loop-item__title font-happy hover:text-black focus:text-black hover:underline focus:underline"):
                temp.append(j.text)
            title=' '.join(temp)

            # scarppint the image 
            
            for j in i.find_all("img") :
                img_link=j["src"]


            # scarpping  the links
            

            # print temp data 



            # print("Title: ",title,"\nImage Link: ",img_link)
        
        
notifi.check()