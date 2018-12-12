
# coding: utf-8

# # Chapter 5: Data Gathering and Cleaning  

# In[46]:


import numpy as np
np.random.randn(5, 3)


# In[47]:


import pandas as pd
import numpy as np

dataset = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['stock1', 'stock2', 'stock3'])
dataset.rename(columns={"one":'stock1',"two":'stock2', "three":'stock3'}, inplace=True)
dataset = dataset.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (dataset)


# In[48]:


print (dataset['stock1'].isnull())


# In[49]:


print (dataset)
dataset.fillna(0)


# In[50]:


# Fill missing values forward 
print (dataset)
dataset.fillna(method='pad')


# In[51]:


print (dataset)
dataset.dropna()


# In[52]:


print (dataset)
dataset.replace(np.nan, 0 )


# # Read CSV files 

# In[53]:


import pandas as pd
sales = pd.read_csv("Sales.csv")
print ("\n\n<<<<<<< First  5 records <<<<<<<\n\n" )
print (sales.head())


# In[54]:


print ("\n\n<<<<<<< Last  5 records <<<<<<<\n\n" )
print (sales.tail())


# In[55]:


#import pandas as pd
salesNrows = pd.read_csv("Sales.csv", nrows=4)
salesNrows


# In[56]:


salesNrows.rename(columns={"SALES_ID":'ID',"SALES_BY_REGION":'REGION'}, inplace=True)
salesNrows


# # Find unique values 

# In[57]:


print (len(salesNrows['JANUARY'].unique()))
print (len(salesNrows['REGION'].unique()))
print (salesNrows['JANUARY'].unique())


# In[58]:


#[0, 1, 2] or ['SALES_ID' , 'SALES_BY_REGION',  'JANUARY'] 
salesNrows = pd.read_csv("Sales.csv", nrows=4, usecols=[0, 1, 6])
salesNrows


# In[60]:


# Read specific fields of data [0, 1, 2] or 
#['SALES_ID' , 'SALES_BY_REGION',  'JANUARY'] 
salesNrows = pd.read_csv("Sales.csv", nrows=4, 
            usecols=['SALES_ID' , 'SALES_BY_REGION',  'FEBRUARY', 'MARCH'])
salesNrows


# In[61]:


sales = pd.read_csv("Sales.csv", nrows=7, 
        na_values =["n.a.", "not avilable"])
mydata = sales.head(7)
mydata


# In[62]:


sales = pd.read_csv("Sales.csv", nrows=7, 
        na_values =["n.a.", "not avilable", -1])
mydata = sales.head(7)
mydata


# # Data Integration
# ## Read Data 

# In[63]:


import pandas as pd

a = pd.read_csv("1. Export1_Columns.csv")
b = pd.read_csv("1. Export2_Columns.csv")


# In[64]:


a.head()


# In[65]:


b.head()


# In[66]:


a.head()


# In[67]:


b.drop('2014', axis=1, inplace=True)
columns = ['2013', '2012']
b.drop(columns, inplace=True, axis=1)
b.drop(b.columns[[3]], axis=1, inplace=True)
b.head()


# In[68]:


mergedDataSet = a.merge(b, on="Country Name")
mergedDataSet.head()


# In[69]:


dataX = a.merge(b)
dataX.head()


# # Merge two data sets using Index 
# ### Rows Union 

# In[70]:


Data1 = a.head()
Data1=Data1.reset_index()
Data1


# In[71]:


Data2 = a.tail()
Data2=Data2.reset_index()
Data2


# In[72]:


# stack the DataFrames on top of each othe
VerticalStack = pd.concat((Data1, Data2), axis=0)
VerticalStack


# # Read Jason data

# In[73]:


import json
data = '''{
"name" : "Ossama",
"phone" : {
"type" : "intl",
"number" : "+971 50 244 5467"
},
"email" : {
"hide" : "No"
}
}'''
info = json.loads(data)
print ('Name:',info["name"])
print ('Hide:',info["email"]["hide"])


# In[74]:


input = '''[
{ "id" : "001",
"x" : "5",
"name" : "Ossama"
} ,
{ "id" : "009",
"x" : "10",
"name" : "Omar"
}
]'''
info = json.loads(input)
print ('User count:', len(info))
for item in info:
    print ('\nName', item['name'])
    print ('Id', item['id'])
    print ('Attribute', item['x'])


# ## Read Jason from the cloud 

# In[91]:


import urllib.request
import json


with urllib.request.urlopen("http://python-data.dr-chuck.net/comments_244984.json") as url:
    uh = url.read()

print ('Retrieving', url)

data = uh
print ('Retrieved',len(data),'characters')

try: 
    js = json.loads(str(data))
except: 
    js = None
    
print (json.dumps(js, indent=4))


# In[99]:


from urllib.request import urlopen
import json
req = urlopen("http://python-data.dr-chuck.net/comments_244984.json")
json = json.loads(req.read())
print (json)
print (json['comments'])


# In[100]:


sum=0
counter=0
for i in range(len(json["comments"])):
    counter+=1
    Name = json["comments"][i]["name"]
    Count = json["comments"][i]["count"]
    sum+=int(Count)
    print (Name," ", Count)

print ("\nCount: ", counter)
print ("Sum: ", sum)


# In[101]:


import json
with open('comments.json') as json_data:
    jasondta = json.load(json_data)
    print(jasondta)


# In[102]:


sum=0
counter=0
for i in range(len(jasondta["comments"])):
    counter+=1
    Name = jasondta["comments"][i]["name"]
    Count = jasondta["comments"][i]["count"]
    sum+=int(Count)
    print (Name," ", Count)

print ("\nCount: ", counter)
print ("Sum: ", sum)


# # Read and process HTML tags 

# In[103]:


import urllib.request
with urllib.request.urlopen("http://python-data.dr-chuck.net/known_by_Rona.html") as url:
    strhtml = url.read()
#I'm guessing this would output the html source code?
print(strhtml[:700])


# In[104]:


import urllib
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://python-data.dr-chuck.net/known_by_Rona.html')
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')

print(html_doc[:700])
print("\n")
print (soup.title)
print(soup.title.string)
print(soup.a.string)


# In[106]:


for x in soup.find_all('b'): 
    print(x.string)


# In[107]:


import urllib
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://python-data.dr-chuck.net/known_by_Rona.html')
html_doc = response.read()
print (html_doc[:300])
soup = BeautifulSoup(html_doc, 'html.parser')

print ("\n")
counter=0
for link in soup.findAll("a"):
    print(link.get("href"))
    if counter<10: 
        counter+=1
        continue 
    else: break 


# In[108]:


htmldata="""<html>
  <head>
   <title>
    The Dormouse's story
   </title>
  </head>
  <body>
   <p class="title">
    <b>
     The Dormouse's story
    </b>
   </p>
   <p class="story">
    Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>
    ,
    <a class="sister" href="http://example.com/lacie" id="link2">
     Lacie
    </a>
    and
    <a class="sister" href="http://example.com/tillie" id="link2">
     Tillie
    </a>
    ; and they lived at the bottom of a well.
   </p>
   <p class="story">
    ...
   </p>
  </body>
 </html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup.prettify())


# In[109]:


soup.title


# In[110]:


soup.title.name


# In[111]:


soup.title.string


# In[112]:


soup.title.parent.name


# In[113]:


soup.p


# In[114]:


soup.p['class']


# In[115]:


soup.a


# In[116]:


soup.find_all('a')


# In[117]:


soup.find(id="link2")


# In[118]:


for link in soup.find_all('a'):
    print(link.get('href'))


# In[119]:


print(soup.get_text())


# In[120]:


htmldata="""<html>
  <head>
   <title>
    Python Book Verion 2018
   </title>
  </head>
  <body>
   <p class="title">
    <b>
     Author Name: Ossama Embarak
    </b>
   </p>
   <p class="story">
    Python techniques for gathering and cleaning data
    <a class="sister" 

href="https://leanpub.com/AgilePythonProgrammingAppliedForEveryone" 

id="link1">
     Data Cleaning
    </a>
    , Data Processing and Visulization
    <a class="sister" href="http://www.lulu.com/shop/ossama-

embarak/agile-python-programming-applied-for-

everyone/paperback/product-23694020.html" id="link2">
     Data Visualization
    </a>
   
   </p>
   <p class="story">
   @July 2018
   </p>
  </body>
 </html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup.prettify())


# In[121]:


print(soup.get_text())


# In[128]:


xmldata = """
    <?xml version="1.0"?>
    <data>
        <student name="Omar">
            <rank>2</rank>
            <year>2017</year>
            <GPA>3.5</GPA>
            <concentration name="Networking" Semester="7"/>
        </student>
        <student name="Ali">
            <rank>3</rank>
            <year>2016</year>
            <GPA>2.8</GPA>
            <concentration name="Security" Semester="6"/>
        </student>
        <student name="Osama">
            <rank>1</rank>
            <year>2018</year>
            <GPA>3.7</GPA>
            <concentration name="App Development" Semester="8"/>
        </student>
    </data>
""".strip()


# In[129]:


from xml.etree import ElementTree as ET
stuff = ET.fromstring(xmldata)
lst = stuff.findall('student')

print ('Students count:', len(lst))
for item in lst:
    print ("\nName:", item.get("name"))
    print ('concentration:', item.find("concentration").get("name"))
    print ('Rank:', item.find('rank').text)
    print ('GPA:', item.find("GPA").text)


# In[131]:


value = ET.fromstring(xmldata).find('response/result/value')
if value:
    print ('Found value:', value.text)

