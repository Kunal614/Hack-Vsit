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
print(list_value)    

  
#db.child("VSIT_files").remove()
#name.child("Rishav").get()
#paitent = name.val()
#print(paitent.values())
#places = place.values()

