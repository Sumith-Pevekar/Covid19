from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="logo.ico",
        timeout=100
    )
def getdata(url):
    r=requests.get(url)
    return r.text

if __name__ =='__main__':
    while(True):
        myHtmlData=getdata('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        myDataStr=''
        for tr in soup.find_all('tbody')[9].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList=myDataStr.split("\n\n")

        states=['Andaman and Nicobar Islands','Andhra Pradesh','Bihar','Chandigarh','Chhattisgarh','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Karnataka',
                'Kerala','Ladakh','Madhya Pradesh','Maharashtra','Manipur','Mizoram','Odisha','Puducherry','Punjab','Rajasthan','Tamil Nadu','Telengana','Uttarakhand','Uttar Pradesh',
                'West Bengal']

        for item in itemList[0:27]:
            dataList=item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle='Indian Cases of Covid-19'
                nText= f"State:{dataList[1]}\nIndian Nationals:{dataList[2]}\nForeign Nationals:{dataList[3]}\nCured:{dataList[4]}  Deaths:{dataList[5]}"
                notifyMe(nTitle,nText)
        time.sleep(360000)
