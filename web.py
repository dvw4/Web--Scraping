import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

home_url = 'https://finance.yahoo.com/most-active'   #The URL Address of the webpage we will scrape,
response = requests.get(home_url)     #requests.get()
response.status_code    #Here we are checking the Status code, -> 200-299 will mean that the request was successful
page_contents = response.text
len(page_contents)   #The `len` fucnction tells us the length of the response object
doc = BeautifulSoup(page_contents, 'html.parser')  #Now 'doc' contains entire html in parsed format
title = doc.find('title')
title
tr_parent1 = doc.find_all('tr',{'class':'simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv2BgColor)'}) #apple
tr_parent2 = doc.find_all('tr',{'class':'simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv1BgColor) '}) # amd class
len(tr_parent1) + len(tr_parent2)
td_child1 = tr_parent1[1].find_all('td')
td_child1
symbol = td_child1[0].find('a').text.strip()
name = td_child1[1].text.strip()
Priceintrday= td_child1[2].text.strip()
change =  td_child1[3].text.strip()
volume =  td_child1[5].text.strip()
print("Symbol:", format(symbol))
print("Name:", format(name))
print("Price(Intraday):", format(Priceintrday))
print("Change:", format(change))
print("Volume:", format(volume))
 

def parse_document(tr_tag):
   
   td_tag = tr_tag.find_all('td')
   symbol = td_tag[0].find('a').text.strip()
   name = td_tag[1].text.strip()
   price = td_tag[2].text.strip()
   change = td_tag[3].text.strip()
   volume = td_tag[5].text.strip().replace(',', '')
   print(symbol)   
   print("Symbol:", format(symbol))
   print("Name:", format(name))
   print("Price(Intraday):", format(price))
   print("Change:", format(change))
   print("Volume:", format(volume))
   stocks = {}
   
   for i in range(5):
      stocks["Symbol"]= symbol
      stocks["Name"] = name
      stocks["Price"] = price
      stocks["Change"] = change
      stocks["Volume"] = volume
   print(stocks)
   myClient=MongoClient(username='dvw4',password='dvw4',authSource='dvw4')
   dlist = myClient.list_database_names()
   try:
      # The ismaster command is cheap and does not require auth.
      myClient.admin.command('ismaster')
      print("Connection Completed")
   except ConnectionFailure:  print("Server not available")
  
   rec = myClient["dvw4"]
   collection = rec["Stocks"]
   collection.insert_one(stocks)

  
a = 10
for i in range(5):

	parse_document(tr_parent1[i])


