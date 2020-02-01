import pyrebase
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
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

firbase = pyrebase.initialize_app(Config)
db = firbase.database()

#db.("place").remove()
dict1={}
Businesses = db.child("VSIT_files").get()
for user in Businesses.each():
  userid = user.key()
  dict1 = user.val().copy()
  #print(user.val())
  inventorydb = db.child(userid).get()
list_record=[]


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
for x in list_record:
    ss = sid.polarity_scores(x)
#    print(x)
#    print(type(ss))
#    print(ss['pos'])
    positivity+=ss['pos']
print(positivity)
if positivity <= 2.7:
    print("You seem to be depressed. Have a consultation!")

#db.child("VSIT_files").remove()
#name.child("Rishav").get()
#paitent = name.val()
#print(paitent.values())
#places = place.values()
