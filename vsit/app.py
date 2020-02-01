from flask import Flask, render_template,request
import webbrowser
import pyrebase
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import webbrowser
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize


Config = {
    "apiKey": "AIzaSyAqGk4Z_2QAE0JSyvVNDkjhRUmrg1apot0",
    "authDomain": "vsit-2be9f.firebaseapp.com",
    "databaseURL": "https://vsit-2be9f.firebaseio.com",
    "projectId": "vsit-2be9f",
    "storageBucket": "vsit-2be9f.appspot.com",
    "messagingSenderId": "443551929217",
    "appId": "1:443551929217:web:83d9e1fe6429f56b5c4e80",
    "measurementId": "G-2M0SJERF9S"
}
firbase = pyrebase.initialize_app(Config)
db = firbase.database()


app = Flask(__name__)

@app.route('/')
def index():
   
    return render_template('index.html')

@app.route('/details')   

def details():
   
    place = "delhi"#input("Enter the name")
    ua={"User-Agent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
     
    url = "https://www.justdial.com/"+str(place)+"/Physiatrist-Doctors/nct-11105148"
    res=requests.get(url,headers=ua)
    soup = BeautifulSoup(res.content,'html.parser')
    list1=[]
    list4=[]
    name = soup.find_all(class_="lng_cont_name")
    available = soup.find_all(class_="distnctxt rsrtopn-1")
    addr=soup.find_all(class_='adWidth cont_sw_addr')
    list2=[]
    list3=[]
    for i in available:
        list4.append(i.get_text())    
    for i in name:
        list2.append(i.get_text())
    for i in range(len(addr)):
        list1.append(addr[i].get_text().strip())   
    urla2="https://www.justdial.com/Delhi/Dacc-Near-G3S-Cinema-Rohini/011PXX11-XX11-160607113128-G7M1_BZDET?xid=RGVsaGkgUGh5c2lhdHJpc3QgRG9jdG9ycw==&tab=book-appointment&reqbk=0"
    urla4="https://www.justdial.com/Delhi/Dr-Singh-Near-VD-Honda-Showroom-Dwarka-Sector-7/011PXX11-XX11-180602141117-A4D6_BZDET?xid=RGVsaGkgUGh5c2lhdHJpc3QgRG9jdG9ycw==&tab=book-appointment&reqbk=0"
    urla3="https://www.justdial.com/Delhi/Tulsi-Holistic-Clinic-Near-Chacha-Bhaturewala-Kamla-Nagar/011PXX11-XX11-090620173143-M3V7_BZDET?xid=RGVsaGkgUGh5c2lhdHJpc3QgRG9jdG9ycw==&tab=book-appointment&reqbk=0"
    urla5="https://www.justdial.com/Delhi/Ajay-Clinic-Near-Pili-Kothi-New-Ashok-Nagar/011PXX11-XX11-110822183522-R2W3_BZDET?tab=book-appointment&dept=&stb=2"
    urla6="https://www.justdial.com/Delhi/Dr-Rohit-Sharma-(Goyal-Hospital-Urology-Centre)-Near-Lajpat-Rai-Chowk-Krishna-Nagar/011PXX11-XX11-170804221516-X9J8_BZDET?xid=RGVsaGkgUGh5c2lhdHJpc3QgRG9jdG9ycw==&tab=book-appointment&reqbk=0"
    c = ""
    d= " "
    for i in range(0,len(list2)):
        c = list2[i]
        for j in range(0,len(c)):
            if c[j]=='(':
                break
            elif c[j]==" ":
                d=d+"-"
            else:
                d=d+c[j]
        list2[i]=d
        d = " "
    list5=[]

    list3=list2
    list5.append(urla2)
    list5.append(urla4)
    list5.append(urla3)
    list5.append(urla5)
    list5.append(urla6)
    return render_template('Details.html',name=list3,available = list4 , links=list5)
@app.route('/bot_chat')

def chat():
    return render_template('bot.html')
@app.route('/validate')

def validate():
    dict1={}
    Businesses = db.child("VSIT_files").get()
    for user in Businesses.each():
        userid = user.key()
        dict1 = user.val().copy()
        inventorydb = db.child(userid).get()
    list_record=[]
    db.child("VSIT_files").remove()

    for i in dict1.values():
        if i!="Record":
            list_record.append(i)

    list_value=[]
    for i in range(len(list_record)):
        if i==0 or i==1 or i==2:
            continue
        else:
            list_value.append(list_record[i])
    #print(list_value)

    sid = SentimentIntensityAnalyzer()

    for x in list_record:
        if x.count('.')>1:
            lines_list = tokenize.sent_tokenize(x)
            list_record.extend(lines_list)
            list_record.remove(x)

    positivity = 0
    output="You are not depressed. You can still try our games it is fun!"
    for x in list_record:
        ss = sid.polarity_scores(x)
        positivity+=ss['pos']
   
    if positivity <= 2.7:
        output="You seem to be depressed. We have medically certified games and motivational music to make you feel better. Still you can have a consultatio by visiting the contact section."

    return render_template('valid.html',positivity=positivity ,result=output) 

if __name__=="__main__":
    app.run()    