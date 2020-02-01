import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import webbrowser
import re
#import pyrebase
#from flask import Flask , render_template , request



def find_phy(url,ua,url1):
    res=requests.get(url,headers=ua)
    soup = BeautifulSoup(res.content,'html.parser')
    list1=[]
    name = soup.find_all(class_="lng_cont_name")
    available = soup.find_all(class_="distnctxt rsrtopn-1")
    addr=soup.find_all(class_='adWidth cont_sw_addr')
    list2=[]
    for i in name:
        list2.append(i.get_text())
    for i in range(len(addr)):
        list1.append(addr[i].get_text().strip())   
    #list1 = ['Near G3S Cinema, R..\t\t\t\t|', 'VD Honda, Dwarka S..\t\t\t\t|', 'Chacha Bhaturewala..\t\t\t\t|', 'Club Road, Punjabi..\t\t\t\t|', 'Main Road, New Ash..\t\t\t\t|', 'Rajiv Chowk, Gurga..\t\t\t\t|', 'Vikas Marg, Chitra..\t\t\t\t|', 'Lajpat Rai Chowk, ..\t\t\t\t|', 'Block A, Dilshad G..\t\t\t\t|', 'Sector VI, Vaishal..\t\t\t\t|']
    b=""
    c=""
    for i in range(0,len(list1)):
        b=list1[i]
        for j in range(0,len(b)):
            if b[j]=="," or b[j]==".":
                break
            else:
                c=c+b[j]
        list1[i]=c
        c=""
    for i in range(0,len(list1)):
        b= list1[i]
        for j in range(0,len(b)):
            if b[j]==" ":
                c=c+"-"
            else:
                c=c+b[j]
        list1[i]=c
        c=""
    print(list1)
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
    print(list2)
    #appointment = soup.find_all('a',attrs={'class':'bookap green-btn result_loader_0 big_dn'})
   
    #https://www.justdial.com/Mumbai/Dr-Dhara-Kothari-Feet-%20Road/033PXX33-XX33-180601112432-I6P8_BZDET?xid=S29sa2F0YSBQaHlzaWF0cmlzdCBEb2N0b3Jz&tab=book-appointment&reqbk=0
    
    for i in range(len(available)):
        print(name[i].get_text())
        print(available[i].get_text())
        print("\n ")
 
    

    #print(con.attr)
    #for descr in soup.find_all('span', attrs={'class':'mobilesv'}):
        #print(descr)

   

if __name__ == "__main__":

    place = input("Enter the name")
    ua={"User-Agent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}

    url = "https://www.justdial.com/"+str(place)+"/Physiatrist-Doctors/nct-11105148"
    url1=url
    find_phy(url,ua,url1)
