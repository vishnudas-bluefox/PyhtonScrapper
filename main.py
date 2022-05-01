# importing libraries 
import requests
from bs4 import BeautifulSoup
import json

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
    def check(url):
        print("Starting....\n")
        article={}
        datas=[]
        try:
            print("Trying to connect phase one network")
            r = requests.get(url,headers=headers)
            soup = BeautifulSoup(r.content,'html.parser')
            print("Connected to phase one...\n Collecting the data.....\n")
        except Exception as Error :
            print("we cant connect now to the website check the connection and try again()...:)..")
            print(Error)

        # each section of article 
        for i in soup.find_all('div',class_="mb-10"):
            # saving temp data 
            temp=[]
            title = ""
            title_link=""
            img_link=""


            # scrapping title and Links
            try:
                for j in i.find_all("a",class_="block mb-4 text-2xl text-black loop-item__title font-happy hover:text-black focus:text-black hover:underline focus:underline"):
                    temp.append(j.text)
                    try:
                        title_link=j['href']
                    except Exception as Error:
                        print("\nWe cant seek the title url...")
                        print(Error)
                        title_link=None
                title=' '.join(temp)
            except Exception as Error:
                print("\nscarpping title not gone well...")
                print(Error)
                title=None

            # scarppint the image 
            try:
                for j in i.find_all("img") :
                   img_link=j["src"]
            except Exception as Error:
                print("\nScrapping image not gone well...")
                print(Error)
                img_link=None
            # scrapping time and para ()
            TP=notifi.timeandpara(title_link)

            # create dictionary with all the collected data 
            article['Title']=title
            article['TitleLink']=title_link
            article['ImageLink']=img_link
            article['Time']=TP[0]
            article['Paragraph']=TP[1]           

            datas.append(article)

        # converts to json and prints it

        # we can convert this datas to output as txt file or dynamic data 
        j=json.dumps(datas,indent=2)
        print("\nDatas converted to JSON and printin it.....\n\n")
        print(j)


    # function to get data from from each title page and retrive para and time stamp 
    def timeandpara(url):
        try:
            print("\nPhase two starts executing....")
            r = requests.get(url,headers=headers)
            soup = BeautifulSoup(r.content,'html.parser')
            print("\nPahse two connected.....")
        except Exception as Error:
            print("\nThere was error in phase two execution...\nPlease try again or check you have stable network connection.....")
            print(Error)

        # find the posted date and time
        try:
            for i in soup.find_all('time'):
                time = i.text
                break;
        except Exception as Error:
            print("\nFinding time in second phase not gone well \n We assigning None to it")
            print(Error)
        # find the first para of the ariticle 
        try:
            for i in soup.find_all('p'):
                para =i.text
                break;
        except Exception as Error:
            print("\nWe can't seek paragraph in article please retry...")
            print(Error)
            para =None

        # return the values 
        return time,para

notifi.check(url)