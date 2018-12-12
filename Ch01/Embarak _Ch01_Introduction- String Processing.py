
# coding: utf-8

# In[3]:


var1 = 'Welcome to Dubai'
var2 = "Python Programming"

print ("var1[0]:", var1[0])
print ("var2[1:5]:", var2[1:5])


# In[5]:


st1="Hello"
st2=' World'
fullst=st1 + st2
print (fullst)


# In[11]:


# looking inside strings 
fruit = 'banana'
letter= fruit[1]
print (letter)

index=3
w = fruit[index-1]

print (w)
print (len(fruit))


# In[14]:


# Convert string to int 
str3 = '123'
str3= int (str3)+1 
print (str3)


# In[15]:


# Read and convert data 
name=input('Enter your name: ')
age=input('Enter your age: ')
age= int(age) + 1

print ("Name:%s"% name ,"\t Age:%d"% age)


# In[30]:


# Looking through string 
fruit ='banana'
index=0
while index< len(fruit):
    letter = fruit [index]
    print (index, letter )
    index=index+1


# In[31]:


print ("\n Implementing iteration with continue")
while True:
    line = input('Enter your data>')  
    if line[0]=='#':
        continue
    if line =='done':
        break
    print (line )
print ('End!')


# In[32]:


print ("\nPrinting in reverse order")
index=len(fruit)-1
while index>=0 :
    letter = fruit [index]
    print (index, letter )
    index=index-1


# In[33]:


Country='Egypt'
for letter in Country:
    print (letter)


# In[2]:


# Looking and counting 
word='banana'
count=0
for letter in word:
    if letter =='a':
        count +=1
print ("Number of a in ", word, "is :", count )


# In[3]:


# Slicing Strings 
s="Welcome to Higher Colleges of Technology"
print (s[0:4])
print (s[6:7])
print (s[6:20])
print (s[:12])
print (s[2:])
print (s [:])
print (s)


# In[43]:


var1 =' Higher Colleges of Technology '
var2='College'
var3='g'

print ( var2 in var1)
print ( var2 not in var1)


# In[29]:


var1 =' Higher Colleges of Technology '
var2='College'
var3='g'

print (var1.upper())
print (var1.lower())
print ('WELCOME TO'.lower()) 
print (len(var1))
print  (var1.count(var3, 2, 29)  )  # find how many g letters in var1
print ( var2.count(var3) )


# In[33]:


print (var1.endswith('r'))
print (var1.startswith('O'))
print (var1.find('h', 0, 29))

print (var1.lstrip())  # It removes all leading whitespace of a string in var1  
print (var1.rstrip()) # It removes all trailing whitespace of a string in var1  
print (var1.strip())
print ('\n')
print (var1.replace('Colleges', 'University'))


# In[39]:


# Parsing and Extracting strings  
Maindata = 'From ossama.embarak@hct.ac.ae Sunday Jan 4 09:30:50 2017'
atpost = Maindata.find('@')
print ("\n<<<<<<<<<<<<<<>>>>>>>>>>>>>")
print (atpost)
print (Maindata[ :atpost])
data = Maindata[ :atpost]
name=data.split(' ')
print (name)
print (name[1].replace('.', ' ').upper())
print ("\n<<<<<<<<<<<<<<>>>>>>>>>>>>>")


# In[41]:


# Another way to split strings 
Maindata = 'From ossama.embarak@hct.ac.ae Sunday Jan 4 09:30:50 2017'
name= Maindata[ :atpost].replace('From','').upper()
print (name.replace('.',' ').upper().lstrip())
print ("\n<<<<<<<<<<<<<<>>>>>>>>>>>>>")
sppos=Maindata.find(' ', atpost)
print (sppos)
print (Maindata[ :sppos])
host = Maindata [atpost + 1 : sppos ]
print (host)
print ("\n<<<<<<<<<<<<<<>>>>>>>>>>>>>")


# # EXERCISES AND ANSWERS 

# In[47]:


var1 ='HCT'
index=0 
while index< len(var1):
    letter = var1[index]
    print (letter)
    index+=1


# In[48]:


var1 ='HCT'
index=0 
while len(var1)> index:
    letter = var1[index]
    print (letter)
    index+=1


# In[54]:


strvar1 = 'X-DSPAM-Confidence: 0.8475'
post = strvar1.find(':')
numer=float(strvar1[post+1:])
print (numer )

