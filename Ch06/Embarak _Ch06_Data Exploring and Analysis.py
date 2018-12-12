
# coding: utf-8

# # Chapter 6: Data Exploring Analysis

# In[5]:


import pandas as pd
import numpy as np
data = np.array(['O','S','S','A'])
S1 = pd.Series(data)   # without adding index 
S2 = pd.Series(data,index=[100,101,102,103]) # with adding index 
print (S1)
print ("\n")
print (S2)


# ### Create series from dictionary

# In[6]:


import pandas as pd
import numpy as np
data = {'X' : 0., 'Y' : 1., 'Z' : 2.}
SERIES1 = pd.Series(data)
print (SERIES1)


# In[7]:


import pandas as pd
import numpy as np
data = {'X' : 0., 'Y' : 1., 'Z' : 2.}
SERIES1 = pd.Series(data,index=['Y','Z','W','X'])
print (SERIES1)


# In[9]:


# Use sclara to create a series 
import pandas as pd
import numpy as np
Series1 = pd.Series(7, index=[0, 1, 2, 3, 4])
print (Series1)


# ### Accessing Data from Series 

# In[18]:


import pandas as pd
Series1 = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

print ("Example 1:Retrieve the first element")
print (Series1[0] ) 
print ("\nExample 2:Retrieve the first three element")
print (Series1[:3])   

print ("\nExample 3:Retrieve the last three element")
print(Series1[-3:])

print ("\nExample 4:Retrieve a single element")
print (Series1['a'])

print ("\nExample 5:Retrieve multiple elements")
print (Series1[['a','c','d']])


# In[5]:





# In[20]:


import pandas as pd
import numpy as np
my_series1 = pd.Series([5, 6, 7, 8, 9, 10])
print ("my_series1\n", my_series1)
print ("\n Series Analysis\n ")
print ("Series mean value : ", my_series1.mean())  # find mean value in a series 
print ("Series max value : ",my_series1.max())   # find max value in a series 
print ("Series min value : ",my_series1.min())   # find min value in a series 
print ("Series standred deviation value : ",my_series1.std())   # find standred deviation of a series 


# In[11]:


my_series1.describe()


# In[17]:


my_series_11 = my_series1
print (my_series1)
my_series_11.index = ['A', 'B', 'C', 'D', 'E', 'F']
print (my_series_11)
print (my_series1)


# In[21]:


my_series_11 = my_series1.copy()
print (my_series1)
my_series_11.index = ['A', 'B', 'C', 'D', 'E', 'F']
print (my_series_11)
print (my_series1)


# In[23]:


'F' in my_series_11


# In[27]:


temp = my_series_11 < 8 
temp


# In[35]:


len(my_series_11)


# In[28]:


temp = my_series_11[my_series_11 < 8 ] * 2
temp


# In[37]:


def AddSeries(x,y):
    for i in range (len(x)):
        print (x[i] + y[i])


# In[39]:


print ("Add two series\n") 
AddSeries (my_series_11, my_series1)


# In[40]:


import pandas as pd
import numpy as np
my_series2 = np.random.randn(5, 10)
print ("\nmy_series2\n", my_series2)


# In[49]:


import matplotlib.pyplot as plt
plt.plot(my_series2)
plt.ylabel('index')
plt.show()


# In[54]:


from numpy import *
import math
import matplotlib.pyplot as plt

t = linspace(0, 2*math.pi, 400)
a = sin(t)
b = cos(t)
c = a + b


# In[50]:


plt.plot(t, a, 'r') # plotting t, a separately 
plt.plot(t, b, 'b') # plotting t, b separately 
plt.plot(t, c, 'g') # plotting t, c separately 
plt.show()


# ### create Data frame from lisits 

# In[19]:


import pandas as pd
data = [10,20,30,40,50]
DF1 = pd.DataFrame(data)
print (DF1)


# In[22]:


import pandas as pd
data = [['Ossama',25],['Ali',43],['Ziad',32]]
DF1 = pd.DataFrame(data,columns=['Name','Age'])
print (DF1)


# In[21]:


import pandas as pd
data = [['Ossama',25],['Ali',43],['Ziad',32]]
DF1 = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print (DF1)


# In[ ]:


Create data frame from dictionaries 


# In[24]:


import pandas as pd
data = {'Name':['Omar', 'Ali', 'Mohammed', 'Ossama'],'Age':[30,25,44,4237]}
DF1 = pd.DataFrame(data)
print (DF1)


# In[26]:


import pandas as pd
data = {'Name':['Omar', 'Ali', 'Mohammed', 'Ossama'],'Age':[30,25,44,4237]}
DF1 = pd.DataFrame(data, index=['Employee1','Employee2','Employee3','Employee4'])
print (DF1)


# In[3]:


import pandas as pd
data = [{'Test1': 10, 'Test2': 20},{'Test3': 30, 'Project': 20, 'Final': 20}]
df = pd.DataFrame(data)
print (df)


# In[13]:


import pandas as pd
data = [{'Test1': 10, 'Test2': 20},{'Test1': 30, 'Test2': 20, 'Project': 20}]

#With three column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['First', 'Second'], columns=['Test2', 'Project' , 'Test1'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['First', 'Second'], columns=['Project', 'Test_1','Test2'])
print (df1)
print ("\n")
print (df2)


# In[16]:


import pandas as pd

data = {'Test1' : pd.Series([70, 55, 89], index=['Ahmed', 'Omar', 'Ali']),
      'Test2' : pd.Series([56, 82, 77, 65], index=['Ahmed', 'Omar', 'Ali', 'Salwa'])}

df1 = pd.DataFrame(data)
print (df1)


# In[51]:


import pandas as pd

data = {'Test1' : pd.Series([70, 55, 89], index=['Ahmed', 'Omar', 'Ali']),
      'Test2' : pd.Series([56, 82, 77, 65], index=['Ahmed', 'Omar', 'Ali', 'Salwa'])}
df1 = pd.DataFrame(data)
print (df1['Test2'])   # Column selection
print("\n")
print (df1[:])   # Column selection


# In[46]:


df1.iloc[:, [1,0 ]]


# In[39]:


df1[0:4:1]


# In[66]:


# add a new Column 
import pandas as pd
data = {'Test1' : pd.Series([70, 55, 89], index=['Ahmed', 'Omar', 'Ali']),
      'Test2' : pd.Series([56, 82, 77, 65], index=['Ahmed', 'Omar', 'Ali', 'Salwa'])}
df1 = pd.DataFrame(data)
print (df1)
df1['Project'] = pd.Series([90,83,67, 87],index=['Ali','Omar','Salwa', 'Ahmed'])
print ("\n")
df1['Average'] = round((df1['Test1']+df1['Test2']+df1['Project'])/3, 2)

print (df1)


# In[70]:


import pandas as pd
data = {'Test1' : pd.Series([70, 55, 89], index=['Ahmed', 'Omar', 'Ali']),
      'Test2' : pd.Series([56, 82, 77, 65], index=['Ahmed', 'Omar', 'Ali', 'Salwa'])}
print (df1)
df2 = df1
print ("\n")
print (df2)


# In[71]:


# Delete a column in data frame using del function
print ("Deleting the first column using DEL function:")
del df2['Test2']
print (df2)

# Delete a column in data frame  using pop function
print ("\nDeleting another column using POP function:")
df2.pop('Project')
print (df2)


# In[72]:


print (df1)


# In[73]:


print (df2)


# In[83]:


# add a new Column 
import pandas as pd
data = {'Test1' : pd.Series([70, 55, 89], index=['Ahmed', 'Omar', 'Ali']),
      'Test2' : pd.Series([56, 82, 77, 65], index=['Ahmed', 'Omar', 'Ali', 'Salwa'])}
df1 = pd.DataFrame(data)
df1['Project'] = pd.Series([90,83,67, 87],index=['Ali','Omar','Salwa', 'Ahmed'])
print ("\n")
df1['Average'] = round((df1['Test1']+df1['Test2']+df1['Project'])/3, 2)
print (df1)

print ("\n")
df2= df1.copy()   # copy df1 into df2 using copy() method 
print (df2)
#delete columns using del and pop methods 
del df2['Test2']
df2.pop('Project')
print ("\n")
print (df1)
print ("\n")
print (df2)


# In[106]:


# add a new Column 
import pandas as pd
data = {'Test1' : pd.Series([70, 55, 89], index=['Ahmed', 'Omar', 'Ali']),
      'Test2' : pd.Series([56, 82, 77, 65], index=['Ahmed', 'Omar', 'Ali', 'Salwa'])}
df1 = pd.DataFrame(data)
df1['Project'] = pd.Series([90,83,67, 87],index=['Ali','Omar','Salwa', 'Ahmed'])
print ("\n")
df1['Average'] = round((df1['Test1']+df1['Test2']+df1['Project'])/3, 2)
print (df1)
print ("\nselect  iloc function to retrieve  row number 2")
print (df1.iloc[2])   
print ("\nslice rows")
print (df1[2:4] )        


# In[108]:


print (df1)


# In[ ]:


import pandas as pd
data = {'Test1' : pd.Series([70, 55, 89], index=['Ahmed', 'Omar', 'Ali']),
      'Test2' : pd.Series([56, 82, 77, 65], index=['Ahmed', 'Omar', 'Ali', 'Salwa']),
      'Project' : pd.Series([87, 83, 90, 67], index=['Ahmed', 'Omar', 'Ali', 'Salwa']),
      'Average' : pd.Series([71, 73.33, 85.33, 66], index=['Ahmed', 'Omar', 'Ali', 'Salwa'])}

data = pd.DataFrame(data)
print (data)
print("\n")
df2 = pd.DataFrame([[80, 70, 90, 80]], columns = ['Test1','Test2','Project','Average'], index=['Khalid'])
data = data.append(df2)
print (data)


# In[138]:


print (data)
print ('\n')
data = data.drop('Omar')
print (data)


# In[74]:


import pandas as pd
data = {'Age' : pd.Series([30, 25, 44, ], index=['Ahmed', 'Omar', 'Ali']),
      'Salary' : pd.Series([25000, 17000, 30000, 12000], index=['Ahmed', 'Omar', 'Ali', 'Salwa']),
      'Height' : pd.Series([160, 154, 175, 165], index=['Ahmed', 'Omar', 'Ali', 'Salwa']),
      'Weight' : pd.Series([85, 70, 92, 65], index=['Ahmed', 'Omar', 'Ali', 'Salwa']),
      'Gender' : pd.Series(['Male', 'Male', 'Male', 'Female'], index=['Ahmed', 'Omar', 'Ali', 'Salwa'])}

data = pd.DataFrame(data)
print (data)
print("\n")
df2 = pd.DataFrame([[42, 31000, 170, 80, 'Female']], columns = ['Age','Salary','Height','Weight', 'Gender']
                   , index=['Mona'])
data = data.append(df2)
print (data)


# In[63]:


data.describe()


# In[64]:


data.describe(include='all')


# In[66]:


data.Salary.describe()


# In[67]:


data.describe(include=[np.number])


# In[68]:


data.describe(include=[np.object])


# In[70]:


data.describe(exclude=[np.number])


# In[71]:


data


# In[75]:


OptimalWeight = data['Height']- 100
OptimalWeight


# In[93]:


unOptimalCases =  data['Weight'] <= OptimalWeight  
unOptimalCases


# ## Create Panel

# In[141]:


np.random.randn(4, 3)


# In[143]:


# creating an empty panel
import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
Paneldf = pd.Panel(data)
print (Paneldf)


# In[94]:


data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)


# In[95]:


p


# In[97]:


p['Item1'].describe()


# In[104]:


import pandas as pd
data1 = {'Age' : pd.Series([30, 25, 44, ], index=['Ahmed', 'Omar', 'Ali']),
      'Salary' : pd.Series([25000, 17000, 30000, 12000], index=['Ahmed', 'Omar', 'Ali', 'Salwa']),
      'Height' : pd.Series([160, 154, 175, 165], index=['Ahmed', 'Omar', 'Ali', 'Salwa']),
      'Weight' : pd.Series([85, 70, 92, 65], index=['Ahmed', 'Omar', 'Ali', 'Salwa']),
      'Gender' : pd.Series(['Male', 'Male', 'Male', 'Female'], index=['Ahmed', 'Omar', 'Ali', 'Salwa'])}

data2 = {'Age' : pd.Series([24, 19, 33,25  ], index=['Ziad', 'Majid', 'Ayman', 'Ahlam']),
      'Salary' : pd.Series([17000, 7000, 22000, 21000], index=['Ziad', 'Majid', 'Ayman', 'Ahlam']),
      'Height' : pd.Series([170, 175, 162, 177], index=['Ziad', 'Majid', 'Ayman', 'Ahlam']),
      'Weight' : pd.Series([77, 84, 74, 90], index=['Ziad', 'Majid', 'Ayman', 'Ahlam']),
      'Gender' : pd.Series(['Male', 'Male', 'Male', 'Female'], index=['Ziad', 'Majid', 'Ayman', 'Ahlam'])}


# In[105]:


data = {'Group1' :data1, 
        'Group2' :data2}
p = pd.Panel(data)


# In[106]:


p['Group1'].describe()


# In[107]:


p['Group1']['Salary'].describe()


# In[147]:


# creating an empty panel
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
Paneldf = pd.Panel(data)
print (Paneldf['Item1'])
print ("\n")
print (Paneldf['Item2'])


# In[149]:


print (Paneldf.major_xs(1))


# In[150]:


print (Paneldf.minor_xs(1))


# ## Data anlysis 

# In[11]:


import pandas as pd
import numpy as np
Number = [1,2,3,4,5,6,7,8,9,10]
Names = ['Ali Ahmed','Mohamed Ziad','Majid Salim','Salwa Ahmed', 'Ahlam Mohamed', 'Omar Ali', 'Amna Mohammed',
        'Khalid Yousif', 'Safa Humaid', 'Amjad Tayel']

City = ['Fujairah','Dubai','Sharjah', 'AbuDhabi','Fujairah','Dubai','Sharjah', 'AbuDhabi','Sharjah','Fujairah']
columns = ['Number', 'Name', 'City' ]
dataset= pd.DataFrame({'Number': Number , 'Name': Names, 'City': City}, columns = columns )
Gender= pd.DataFrame({'Gender':['Male','Male','Male','Female', 'Female', 'Male', 'Female','Male', 
                                'Female', 'Male']})
Height = pd.DataFrame(np.random.randint(120,175, size=(12, 1)))
Weight = pd.DataFrame(np.random.randint(50,110, size=(12, 1)))

dataset['Gender']= Gender
dataset['Height']= Height
dataset['Weight']= Weight
dataset.set_index('Number')


# In[186]:


print ( dataset.describe()) # Summary statistics for numerical columns


# In[187]:


print (dataset.mean()) # Returns the mean of all columns


# In[188]:


print (dataset.corr()) # Returns the correlation between columns in a DataFrame


# In[189]:


print (dataset.count()) # Returns the number of non-null values in each DataFrame column


# In[190]:


print (dataset.max()) # Returns the highest value in each column


# In[191]:


print (dataset.min()) # Returns the lowest value in each column


# In[192]:


print (dataset.median()) # Returns the median of each column


# In[193]:


print (dataset.std()) # Returns the standard deviation of each column


# ### Grouping 

# print (dataset)

# In[3]:


dataset.groupby('City')['Gender'].count()


# In[4]:


print (dataset.groupby('City').groups)


# In[5]:


print (dataset.groupby(['City','Gender']).groups)


# In[7]:


grouped = dataset.groupby('Gender')

for name,group in grouped:
    print (name)
    print (group)
    print ("\n")


# In[9]:


grouped = dataset.groupby('Gender')
print (grouped.get_group('Female'))


# In[18]:


# Aggregation
grouped = dataset.groupby('Gender')
print (grouped['Height'].agg(np.mean))
print ("\n")
print (grouped['Weight'].agg(np.mean))
print ("\n")
print (grouped.agg(np.size))
print ("\n")
print (grouped['Height'].agg([np.sum, np.mean, np.std]))


# In[19]:


### Transformations


# In[ ]:


dataset = dataset.set_index(['Number'])
print (dataset)


# In[26]:





# In[28]:



grouped = dataset.groupby('Gender')
score = lambda x: (x - x.mean()) / x.std()*10
print (grouped.transform(score))


# ### Filtration

# In[30]:


print (dataset.groupby('City').filter(lambda x: len(x) >= 3))

