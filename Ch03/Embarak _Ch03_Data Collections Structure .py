
# coding: utf-8

# # Chapter : Collections 

# In[1]:


# Create List 
List1 = [1, 24, 76]
print (List1)

colors=['red', 'yellow', 'blue']
print (colors)

mix=['red', 24, 98.6]
print (mix)

nested= [ 1, [5, 6], 7]
print (nested)

print ([])


# In[9]:


list1 = ['Egypt', 'chemistry', 2017, 2018];
list2 = [1, 2, 3, [4, 5] ];
list3 = ["a", 3.7, '330', "Omar"]

print (list1[2])
print (list2 [3:])
print (list3 [-3:-1])
print (list3[-3])


# In[50]:


courses=["OOP","Networking","MIS","Project"]
students=["Ahmed", "Ali", "Salim", "Abdullah", "Salwa"]
OOP_marks = [65, 85, 92]

OOP_marks.append(50)   # Add new element 
OOP_marks.append(77)# Add new element 
print (OOP_marks[ : ])  # Print list before updateing 

OOP_marks[0]=70   # update new element 
OOP_marks[1]=45   # update new element 
list1 = [88, 93]
OOP_marks.extend(list1)     # extend list with another list 
print (OOP_marks[ : ])  # Print list after updateing 


# In[28]:





# In[48]:


OOP_marks = [70, 45, 92, 50, 77, 45]
print (OOP_marks)

del OOP_marks[0]    # delete an element using del 
print (OOP_marks)

OOP_marks.remove (45)   # remove an element using remove() method 
print (OOP_marks)


OOP_marks.pop (2)   # remove an element using remove() method 
print (OOP_marks)


# In[42]:


len([5, "Omar", 3])  # find the list length.
[3, 4, 1] + ["0", 5, 6] # concatenate lists.
['Hi!'] * 4   # repeate an element in a list.
3 in [1, 2, 3]   # check if element in a list
for x in [1, 2, 3]: print (x) # traverse list elements 


# In[46]:


print (len([5, "Omar", 3]))          # find the list length.
print ([3, 4, 1] + ["Omar", 5, 6])   # concatenate lists.
print (['Eg!'] * 4)                  # repeate an element in a list.
print (3 in [1, 2, 3])              # check if element in a list
for x in [1, 2, 3]: print (x, end='  ') # traverse list elements 


# In[51]:


#Built-in Functions and Lists  
tickets = [3, 41, 12, 9, 74, 15]
print (tickets)
print (len(tickets))
print (max(tickets))
print (min(tickets))
print (sum(tickets))
print (sum(tickets)/len(tickets))


# In[58]:


#List sorting and Traversing 
seq=(41, 12, 9, 74, 3, 15)   # use sequence for creating a list
tickets=list(seq)  

print (tickets)
tickets.sort()
print (tickets)

print ("\nSorted list elements ")
for ticket in tickets:
    print (ticket)


# ## LISTS AND STRINGS

# In[63]:


# convert string to a list of characters
Word = 'Egypt'
List1 = list(Word)
print (List1)


# In[70]:


# we can break a string into words using the split method
Greeting= 'Welcome to Egypt'
List2 =Greeting.split()
print (List2)
print (List2[2])


# In[69]:


# use the delimiter
Greeting= 'Welcome-to-Egypt'
List2 =Greeting.split("-")
print (List2)

Greeting= 'Welcome-to-Egypt'
delimiter='-'
List2 =Greeting.split(delimiter)
print (List2)


# In[73]:


List1 = ['Welcome', 'to', 'Egypt']
delimiter = ' '
delimiter.join(List1)


# In[74]:


List1 = ['Welcome', 'to', 'Egypt']
delimiter = '-'
delimiter.join(List1)


# In[105]:


filesdata="From oembarak@hct.ac.ae Sat Jan 5 09:14:16 2016     mak.jon@ec.ac.ae Sat Jan 5 09:14:16 2011     From ossama.embarak@ar.ac.eg Sat Jan 5 09:14:16 2010                From usa.mak@gmail.com Jan 5 09:14:16 2015"
#print (filesdata)
for line in filesdata:
    #line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print (words[2])


# In[117]:


a = [1, 2, 3]
b = a
print (a)
print (b)


# In[118]:


a.append(77)
print (a)
print (b)


# In[119]:


b is a


# In[120]:


a = [1, 2, 3]
b = [1, 2, 3]
print (a)
print (b)


# In[121]:


a.append(77)
print (a)
print (b)


# In[122]:


b is a


# In[124]:


Students =["Ahmed", "Ali", "Salim", "Abdullah", "Salwa"]
def displaynames (x):
    for name in x:
        print (name)

displaynames(Students)  # Call the function displaynames


# # Dictionaries 

# In[36]:


Prices = {"Honda":40000, "Suzuki":50000, "Mercedes":85000, "Nissan":35000, "Mitsubishi":43000 }
print (Prices)


# In[37]:


Staff_Salary = { 'Omar Ahmed' : 30000 , 'Ali Ziad' : 24000, 'Ossama Hashim': 25000, 'Majid Hatem':10000}
print(Staff_Salary)
STDMarks={"Salwa Ahmed":50, "Abdullah Mohamed":80, "Sultan Ghanim":90}
print(STDMarks)


# In[38]:


STDMarks = dict()
STDMarks['Salwa Ahmed']=50
STDMarks['Abdullah Mohamed']=80
STDMarks['Sultan Ghanim']=90
print (STDMarks)


# In[39]:


STDMarks={"Salwa Ahmed":50, "Abdullah Mohamed":80, "Sultan Ghanim":90}
STDMarks['Salwa Ahmed'] = 85   # update current value of the key 'Salwa Ahmed'
STDMarks['Omar Majid'] = 74 # Add a new item to the dictionary 
print (STDMarks)


# In[40]:


STDMarks={"Salwa Ahmed":50, "Abdullah Mohamed":80, "Sultan Ghanim":90}
print (STDMarks)
del STDMarks['Abdullah Mohamed'] # remove entry with key 'Abdullah Mohamed'
print (STDMarks)
STDMarks.clear()     # remove all entries in STDMarks dictionary
print (STDMarks)
del STDMarks         # delete entire dictionary


# In[2]:


Staff_Salary = { 'Omar Ahmed' : 30000 , 'Ali Ziad' : 24000, 'Ossama Hashim': 25000, 'Majid Hatem':10000}
print('Salary package for Ossama Hashim is ', end='')
print(Staff_Salary['Ossama Hashim'])                    # access specific dictionary element


# In[3]:


# Define a function to return salary after dicount tax 5%
def Netsalary (salary):
    return salary - (salary * 0.05) # also could be retunr salary *0.95

#iterate all elements in a dcitionary 
print ("Name     " , '\t', "Net Salary" )
for key, value in Staff_Salary.items():
    print (key , '\t', Netsalary(value))


# In[43]:


Staff_Salary = { 'Omar Ahmed' : 30000 , 'Ali Ziad' : 24000, 'Ossama Hashim': 25000, 'Majid Hatem':10000}
STDMarks={"Salwa Ahmed":50, "Abdullah Mohamed":80, "Sultan Ghanim":90}


# In[52]:


def cmp(a, b):
    for key, value in a.items():
        for key1, value1 in b.items():
            return (key >key1) - (key < key1) 


# In[54]:


print (cmp(STDMarks,Staff_Salary) )
print (cmp(STDMarks,STDMarks) )
print (len(STDMarks) )
print (str(STDMarks) )
print (type(STDMarks) )


# In[ ]:





# In[71]:


Staff_Salary = { 'Omar Ahmed' : 30000 , 'Ali Ziad' : 24000, 'Ossama Hashim': 25000, 'Majid Hatem':10000}
STDMarks={"Salwa Ahmed":50, "Abdullah Mohamed":80, "Sultan Ghanim":90}
dic3 = Staff_Salary.copy()
Staff_Salary.clear()    # clear all elements in Staff_Salary dictionary 
print (Staff_Salary)   
print (dic3)

dict1= dict()
sequence=('Id' , 'Number' , 'Email')  
print (dict1.fromkeys(sequence)) 
print (dict1.fromkeys(sequence, '####')) 


# In[89]:


Staff_Salary = { 'Omar Ahmed' : 30000 , 'Ali Ziad' : 24000, 'Ossama Hashim': 25000, 'Majid Hatem':10000}
STDMarks={"Salwa Ahmed":50, "Abdullah Mohamed":80, "Sultan Ghanim":90}
print (Staff_Salary.get('Ali Ziad') )
print (STDMarks.items()) 
print (Staff_Salary.keys()) 

print()
STDMarks.setdefault('Ali Ziad') 
print (STDMarks)
print (STDMarks.update(dict1)) 
print (STDMarks)


# In[96]:


Staff_Salary = { 'Omar Ahmed' : 30000 , 'Ali Ziad' : 24000, 'Ossama Hashim': 25000, 'Majid Hatem':10000}
print ("\nSorted by key")
for k in sorted(Staff_Salary):
    print (k, Staff_Salary[k])


# In[97]:


Staff_Salary = { 'Omar Ahmed' : 30000 , 'Ali Ziad' : 24000, 'Ossama Hashim': 25000, 'Majid Hatem':10000}
print ("\nSorted by value")
for w in sorted(Staff_Salary, key=Staff_Salary.get, reverse=True):
  print (w, Staff_Salary[w])


# # Tuples 

# In[1]:


Names = ('Omar', 'Ali', 'Bahaa')
Marks = ( 75, 65, 95 )

print (Names[2])
print (Marks)
print (max(Marks))


# In[2]:


for name in Names:
    print (name)


# In[3]:


Marks[1]=66


# In[4]:


Names = ( 'Omar Ahmed', 'Ali Ziad' , 'Ossama Hashim', 'Majid Hatem')
print (Names)
Names.sort(reverse=True)
print (Names)


# In[9]:


MarksCIS=(70,85,90) 
print (MarksCIS)



# In[14]:



MarksCIS.sort(key=lambda x: int(x[0]))


# In[1]:


import operator 
MarksCIS = [(88,65),(70,90,85), (55,88,44)]
print (MarksCIS)  # original tuples
print (sorted(MarksCIS)) # direct sorting 


# In[2]:


print (MarksCIS)  # original tuples
#create a new sorted tuple 
MarksCIS2 = sorted(MarksCIS, key=lambda x: (x[0], x[1]))
print (MarksCIS2)


# In[3]:


print (MarksCIS)  # original tuples
MarksCIS.sort(key=lambda x: (x[0], x[1])) # sort in tuple 
print (MarksCIS)


# In[4]:


MarksCIS = (70, 85, 55)
MarksCIN = (90, 75, 60)
print ("The third mark in CIS is ", MarksCIS[2])
print ("The third mark in CIN is ", MarksCIN[2])


# In[5]:


MarksCIN = (90, 75, 60)
print (MarksCIN)
del MarksCIN
print (MarksCIN)


# In[6]:


MarksCIS = (88, 65, 70,90,85,45,78,95,55)
print ("\nForward slicing")
print (MarksCIS[1:4])
print (MarksCIS[:3])
print (MarksCIS[6:])
print (MarksCIS[4:6])

print ("\nBackward slicing")
print (MarksCIS[-4:-2])
print (MarksCIS[-3])
print (MarksCIS[-3:])
print (MarksCIS[ :-3])


# In[8]:


import operator 
MarksCIS = [(88,65),(70,90,85), (55,88,44)]
print (MarksCIS)  # original tuples
print (sorted(MarksCIS)) # direct sorting 


MarksCIS2 = sorted(MarksCIS, key=lambda x: (x[0], x[1]))

print (MarksCIS2)

MarksCIS.sort(key=lambda x: (x[0], x[1]))  # sorts in place
print (MarksCIS)


# In[ ]:


students = [
    ('John', 'A', 2),
    ('Zoro', 'C', 1),
    ('Dave', 'B', 3),
]
print(students)


# In[5]:


MarksCIS=(70,85,55)  
MarksCIN=(90,75,60)  
Combind=MarksCIS+MarksCIN  
print (Combind)


# # a series from ndarray with labels.

# In[8]:


import numpy as np
import pandas as pd
Series1 = pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd'])
print(Series1)
print(Series1.index)


# In[9]:


import numpy as np
import pandas as pd
Series2 = pd.Series(np.random.randn(4))
print(Series2)
print(Series2.index)


# In[10]:


print (" \n Series slicing ")
print (Series1[:3])
print ("\nIndex accessing")
print (Series1[[3,1,0]])
print ("\nSingle index")
x = Series1[0]
print (x)


# In[19]:


print ("\nSeries  Sample operations")
print ("\n Series values greater than the mean: %.4f" % Series1.mean())
print (Series1 [Series1> Series1.mean()])
print ("\n Series values greater than the Meadian:%.4f" % Series1.median())
print (Series1 [Series1> Series1.median()])
print ("\nExponential value ")
Series1Exp = np.exp(Series1)
print (Series1Exp)


# In[12]:


dict = {'m' : 2, 'y' : 2018, 'd' : 'Sunday'}
print ("\nSeries of non declared index") 
SeriesDict1 = pd.Series(dict)
print(SeriesDict1)

print ("\nSeries of declared index") 
SeriesDict2 = pd.Series(dict, index=['y', 'm', 'd', 's'])
print(SeriesDict2)


# In[13]:


print ("\nUse the get and set methods to access" 
        "a series values by index label\n")
SeriesDict2 = pd.Series(dict, index=['y', 'm', 'd', 's'])
print (SeriesDict2['y']) # Display the year
SeriesDict2['y']=1999    # change the year vlaue
print (SeriesDict2)      # Display all dictionary values 
print (SeriesDict2.get('y'))  # get specific value by its key


# In[14]:


print ("\n CREATE SERIES FORM SCALAR VALUE ") 
Scl = pd.Series(8., index=['a', 'b', 'c', 'd'])
print (Scl)


# In[18]:


SerX = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
print ("Addition"); 
print( SerX + SerX)
print ("Addition with non matched labels"); 
print (SerX[1:] + SerX[:-1])
print ("Multiplication"); 
print (SerX * SerX)
print ("Expponential"); 
print (np.exp(SerX))


# In[17]:


std = pd.Series([77,89,65,90], name='StudentsMarks') 
print (std.name)
std = std.rename("Marks")
print (std.name)


# In[4]:


#  read data from file and add it to dictionary for processing 
handle = open("Egypt.txt")
text = handle.read()
words = text.split()
#print (words) 
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1

print (counts)
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print ("\n bigword and  bigcount")
print (bigword, bigcount)


# In[14]:


print ((100, 1, 2) > (150, 1, 2))
print ((0, 1, 120) < (0, 3, 4))
print (( 'Javed', 'Salwa' ) > ('Omar', 'Sam'))
print (( 'Khalid', 'Ahmed') < ('Ziad', 'Majid'))


# In[5]:


import pandas as pd
dict1 = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(dict1)
df


# In[6]:


# set index for DataFrame 
pd.DataFrame(dict1, index=['d', 'b', 'a'])


# In[8]:


# Control the labels appearance of the DataFrame 
pd.DataFrame(dict1, index=['d', 'b', 'a'], columns=['two', 'three', 'one'])


# In[11]:


# without index 
ndarrdict = {'one' : [1., 2., 3., 4.],
   'two' : [4., 3., 2., 1.]}
pd.DataFrame(ndarrdict)


# In[12]:


# Assign index
pd.DataFrame(ndarrdict, index=['a', 'b', 'c', 'd'])


# In[18]:


import pandas as pd
import numpy as np
data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
data[:] = [(1,2.,'Hello'), (2,3.,"World")]
pd.DataFrame(data)


# In[16]:


pd.DataFrame(data, index=['First', 'Second'])


# In[17]:


pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[19]:


data2 = [{'A': 1, 'B': 2}, {'A': 5, 'B': 10, 'C': 20}]
pd.DataFrame(data2)


# In[20]:


pd.DataFrame(data2, index=['First', 'Second'])


# In[21]:


pd.DataFrame(data2, columns=['A', 'B'])


# In[22]:


pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
           ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
           ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
           ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
           ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})


# In[25]:


# DATAFRAME COLUMN SELECTION, ADDITION, DELETION 
ndarrdict = {'one' : [1., 2., 3., 4.],
   'two' : [4., 3., 2., 1.]}
df = pd.DataFrame(ndarrdict, index=['a', 'b', 'c', 'd'])
df


# In[26]:


df['three'] = df['one'] * df['two'] # Add column 
df['flag'] = df['one'] > 2          # Add column 
df


# In[27]:


df['Filler'] = 'HCT'
df['Slic'] = df['one'][:2]
df


# In[28]:


# Delet columns 
del df['two']          
Three = df.pop('three')
df


# In[29]:


df.insert(1, 'bar', df['one'])
df


# In[54]:


import numpy as np
import pandas as pd
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df = df.assign(C=lambda x: x['A'] + x['B'])
df = df.assign( D=lambda x: x['A'] + x['C'])
df


# In[55]:


df = df.assign( A=lambda x: x['A'] *2)
df


# In[56]:


df


# In[61]:


df['B']


# In[59]:


df.iloc[2]


# In[62]:


df[1:]


# In[65]:


df[df['C']>7]


# In[69]:


df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df2 = pd.DataFrame({"A": [7, 4, 6], "B": [10, 4, 15]})
print (df1)
print()
print(df2)


# In[70]:


df1+df2


# In[71]:


df1-df2


# In[72]:


df2 - df1.iloc[2]


# In[75]:


df2


# In[78]:


df2*2+1


# In[3]:


import pandas as pd
import numpy as np
P1 = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
                  major_axis=pd.date_range('10/05/2018', periods=5),
                  minor_axis=['A', 'B', 'C', 'D'])
P1


# In[4]:


data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
P2 = pd.Panel(data)
P2


# In[5]:


p3 = pd.Panel.from_dict(data, orient='minor')
p3


# In[26]:


df = pd.DataFrame({'Item': ['TV', 'Mobile', 'Laptop'],
                   'Price': np.random.randn(3)**2*1000})
df


# In[29]:


data = {'stock1': df, 'stock2': df}
panel = pd.Panel.from_dict(data, orient='minor')
panel['Item']


# In[30]:


wp['Price']


# In[33]:


import pandas as pd
import numpy as np
P1 = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
                  major_axis=pd.date_range('10/05/2018', periods=5),
                  minor_axis=['A', 'B', 'C', 'D'])
P1['Item1']


# In[34]:


P1.major_xs(P1.major_axis[2])


# In[35]:


P1.minor_axis


# In[36]:


P1.minor_xs('C')


# In[28]:


data = {'Omar': 2.5, 'Ali': 3.5, 'Osama': 3.0}
pd.Series(data)


# In[30]:


pd.Series(data, index = ['Omar', 'Ali', 'Osama'])


# In[31]:


data = {'Omar': [90, 50, 89], 
       'Ali': [78, 75, 73], 
       'Osama': [67, 85, 80]}
df1 = pd.DataFrame (data, index= ['Course1', 'Course2', 'Course3'])
df1


# In[32]:


df1['Omar']


# In[33]:


df1['Mean'] = (df1['Ali'] + df1['Omar'] + df1['Osama'])/3
df1

