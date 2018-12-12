
# coding: utf-8

# # Chapter 1 Getting Started with Python

# In[47]:


get_ipython().magic(u'pinfo help')


# In[4]:


age,mark,code=10,75,"CIS2403"
print (age)  
print (mark)  
 print (code) 


# In[5]:


TV=15
Mobile=20
Tablet = 30

total = TV + 
        Mobile + 
        Tablet
print (total)


# In[6]:


TV=15
Mobile=20
Tablet = 30

total = TV +         Mobile +         Tablet
print (total)


# In[7]:


days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print (days)


# In[8]:


sms1 = 'Hellow World'
sms2 = "Hellow World"
sms3 = """ Hellow World"""
sms4 = """ Hellow 
    World"""

print (sms1)
print (sms2)
print (sms3)
print (sms4)


# In[9]:


TV=15; name="Nour"; print (name); print ("Welcome to\nDubai Festivale 2018")


# In[10]:


name = input("Enter your name ")
age = int (input("Enter your age"))

print ("\nName=", name); print ("\nAge=", age)


# ### 1.2 Declaring Variable and Assigning Values

# In[11]:


age = 11
name ="Nour"
tall=100.50 


# In[12]:


print (age)
print (name)
print (tall)


# In[13]:


age= mark = code =25  
print (age)  
print (mark)  
print (code)  


# In[14]:


age,mark,code=10,75,"CIS2403"
print (age)  
print (mark)  
print (code) 


# In[16]:


# Expressions 
x=0.6
x=3.9 * x * (1-x)
print (round(x, 2))


# In[18]:


# Python single line comment


# In[19]:


''' This 
        Is 
        Multipline comment'''


# In[20]:


print ("pi=%s"%"3.14159")


# In[1]:


print("The value of %s is = %02f" % ("pi", 3.14159))


# In[21]:


print ("Your name is %s, and your height is %.2f while your weight is %.2d" % 
       ('Ossama', 172.156783, 75.56647))


# In[23]:


print ("Hi %(Name)s, your height is %(height).2f" %{'Name':"Ossama", 
                                                    'height': 172.156783})


# In[24]:


x = "price is"
print ("{1} {0} {2}".format(x, "The", 1920.345))


# In[34]:


class A():x=9
w=A()
print ("{0} {1[2]} {2[test]} {3.x}".format("This", ["a", "or", "is"], 
                                           {"test": "another"},w))
print ("{1[1]} {0} {1[2]} {2[test]} {3.x}".format("This", 
                            ["a", "or", "is"], {"test": "another"},w))


# In[42]:


import time 
localtime = time.asctime(time.localtime(time.time()))
print ("Formatted time :", localtime)
print (time.localtime())
print (time.time())


# In[45]:


import calendar 
calendar.prcal(2018)


# In[46]:


########### End 


# In[48]:


print (13//5)


# In[50]:


print (13<5)
print (13>5)
print (13<=5)
print (2>=5)
print (13==5)
print (13!=5) 


# In[56]:


x=10
print (x)
x=10; x/=2
print (x)
x=10; x+=7
print (x)
x=10; x-=5
print (x)
x=10; x*=5
print (x)
x=13; x%=5
print (x)
x=10; x**=3
print(x)
x=10; x//=2
print(x)


# In[57]:


x=10>5 and 4>20  
print (x)

x=10>5 or 4>20   
print (x)  

x=not(10<4)  
print (x) 


# In[45]:


print (13/5) 


# In[46]:


print (13%5) 


# In[47]:


print (2**3) 


# In[7]:





# In[10]:


#single line comment  
  
'''This is 
multiline comment'''  


# In[5]:


# Expressions 
x=0.6
x=3.9 *x *(1-x)  
print (round( x,2) )


# In[10]:


largest = None
print ('Before:', largest)
for val in [30, 45, 12, 90, 74, 15]:
    if largest is None or val > largest :
        largest = val
        print ('Loop:', val, largest)
print ('Largest:', largest)


# 
# # Pandas and other libraries

# In[34]:


#Create series from array using pandas and numpy
import pandas as pd
import numpy as np
data = np.array([90,75,50,66])
s = pd.Series(data,index=['A','B','C','D'])
print (s)


# In[36]:


print (s[1])


# In[37]:


#Create series from dictionary using pandas and numpy
import pandas as pd
import numpy as np
data = {'Ahmed' : 92, 'Ali' : 55, 'Omar' : 83}
s = pd.Series(data,index=['Ali','Ahmed','Omar'])
print (s)


# In[38]:


print (s[1:])


# # DataFrame

# In[39]:


import pandas as pd
data = [['Ahmed',35],['Ali',17],['Omar',25]]
DataFrame1 = pd.DataFrame(data,columns=['Name','Age'])
print (DataFrame1)


# In[40]:


DataFrame1[1:]


# In[41]:


import pandas as pd
data = {'Name':['Ahmed', 'Ali', 'Omar', 'Salwa'],'Age':[35,17,25,30]}
dataframe2 = pd.DataFrame(data, index=[100, 101, 102, 103])
print (dataframe2)


# In[42]:


dataframe2[:2]


# In[43]:


dataframe2['Name']


# # Panel

# In[44]:


# creating a panel
import pandas as pd
import numpy as np
data = {'Temprature Day1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Temprature Day2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print (p['Temprature Day1'])


# # 1.6.3 PYTHON LAMBDAS, AND THE NUMPY LIBRARY. 

# In[46]:


result = lambda x, y : x * y
result(2,5)


# In[47]:


result(4,10)


# In[65]:


def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
Temp = (15.8, 25, 30.5,25)

F = list ( map(fahrenheit, Temp))
C = list ( map(celsius, F))
print (F)
print (C)


# In[72]:


Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
for x in Fahrenheit:
    print(x)


# In[79]:


fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2==0, fib)
for x in result:
    print(x)


# In[81]:


f = lambda a,b: a if (a > b) else b
reduce(f, [47,11,42,102,13])


# In[82]:


reduce(lambda x,y: x+y, [47,11,42,13])


# In[83]:


a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
np.add(a,b) 


# In[84]:


np.subtract(a,b) #Same as a-b


# # Series 

# In[6]:


import pandas as pd
animals = ["Lion", "Tiger", "Bear"]
pd.Series(animals)


# In[5]:


marks = [95, 84, 55, 75]
pd.Series(marks)


# In[11]:


# Create series from dictionary where indices are the dictionary keys 
quiz1 = {"Ahmed":75, "Omar": 84, "Salwa": 70}
q = pd.Series(quiz1)
q


# In[13]:


# query series  
q.loc['Ahmed']


# In[20]:


q['Ahmed']


# In[19]:


q.iloc[2]


# In[21]:


q[2]


# In[25]:


# implement numpy operation on a series 
s = pd.Series([70,90,65,25, 99])
s


# In[27]:


total =0
for val in s:
    total += val
print (total)


# In[28]:


import numpy as np
total = np.sum(s)
print (total)


# In[29]:


# add new values to series 
s = pd.Series ([99,55,66,88])
s.loc['Ahmed'] = 85
s


# In[32]:


# Append Series 
test = [95, 84, 55, 75]
marks = pd.Series(test)
s = pd.Series ([99,55,66,88])
s.loc['Ahmed'] = 85
s
NewSeries = s.append(marks)
NewSeries


# # 1.6.6 RUN BASIC INFERENTIAL STATISTICAL ANALYSES. 

# In[37]:


import numpy as np
x = np.random.binomial(20, .5, 10000)
print((x>=15).mean())


# In[ ]:


sb.regplot(x = "Total Bill", y = "Bill's Tips", data = df)


# # Regression

# In[65]:


import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('tips')
sb.regplot(x = "total_bill", y = "tip", data = df)
plt.xlabel('Total Bill')
plt.ylabel('Bill Tips')

plt.show()


# In[39]:


df


# # Python - Chi-Square Test

# In[41]:


from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
fig,ax = plt.subplots(1,1)

linestyles = [':', '--', '-.', '-']
deg_of_freedom = [1, 4, 7, 6]
for df, ls in zip(deg_of_freedom, linestyles):
  ax.plot(x, stats.chi2.pdf(x, df), linestyle=ls)

plt.xlim(0, 10)
plt.ylim(0, 0.4)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Chi-Square Distribution')

plt.legend()
plt.show()


# # correlation

# In[42]:


import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')

 
#without regression
sns.pairplot(df, kind="scatter")
plt.show()


# In[46]:


from scipy.stats import binom
import seaborn as sb

data_binom = binom.rvs(n=20,p=0.8,loc=0,size=1000)
ax = sb.distplot(data_binom,
                  kde=True,
                  color='blue',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')


# In[58]:


import pandas as pd

d = {'Name':pd.Series(['Ahmed','Omar','Ali','Salwa','Majid','Othman','Gameel',
   'Ziad','Ahlam','Zahrah','Ayman','Alaa']),
   'Age':pd.Series([34,26,25,27,30,54,23,43,40,30,28,46]),
   'Height':pd.Series([114.23,173.24,153.98,172.0,153.20,164.6,183.8,163.78,172.0,164.80,174.10,183.65])}

#Create a DataFrame
df = pd.DataFrame(d)

# Calculate the standard deviation
print (df.std())


# In[59]:


print (df.describe())


# In[60]:


print ("Mean Values in the Distribution")
print (df.mean())
print ("*******************************")
print ("Median Values in the Distribution")
print (df.median())
print ("*******************************")
print ("Mode Values in the Distribution")
print (df['Height'].mode())


# ### 1.5	EXERCISES 

# In[2]:


# Store input numbers:  
num1 = input('Enter first number: ')  
num2 = input('Enter second number: ')      
 
sumval = float(num1) + float(num2)  # Add two numbers 
minval = float(num1) - float(num2) # Subtract two numbers   
mulval = float(num1) * float(num2) # Multiply two numbers   
divval = float(num1) / float(num2)  #Divide two numbers  

# Display the sum  
print('The sum of {0} and {1} is {2}'.format(num1, num2, sumval))    
# Display the subtraction  
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, minval))  
# Display the multiplication  
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mulval))  
# Display the division  
print('The division of {0} and {1} is {2}'.format(num1, num2, divval))  


# In[3]:


# A. write a python script to prompt the user to enter the triangle first side (a), 
#second side (b) and third side (c) lengths. Then calculate the semi-perimeter (s). 
#calculate the triangle area and display the result to the user. 
#Area of a triangle = (s*(s-a)*(s-b)*(s-c))-1/2. 
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
s = (a + b + c) / 2  # calculate the semi-perimeter  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area) 


# In[7]:


import random 
a = int(input('Enter the starting value : '))  
b = int(input('Enter the end value : '))  
print(random.randint(a,b))  
random.sample(range(a, b), 3)


# In[9]:


# convert kilometers to miles 
kilometers = float(input('Enter the distance in kilometers: '))  
# conversion factor  
Miles = kilometers * 0.62137   
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,Miles)) 


# In[11]:


# convert convert Celsius to Fahrenheit
Celsius = float(input('Enter temperature in Celsius: '))  
# conversion factor  
Fahrenheit = (Celsius * 1.8) + 32  
print('%0.2f Celsius is equal to %0.2f Fahrenheit' %(Celsius,Fahrenheit)) 


# ## End Chapter 1
