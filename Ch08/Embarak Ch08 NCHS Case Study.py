
# coding: utf-8

# # Embarak Ch08 Case Study --> NCHS Case Study

# <p> <h4> <strong> Prepared by:</strong> </h4> <h4> Ossama Embarak </h4> </p>

# In[2]:


import pandas as pd
data = pd.read_csv("NCHS.csv")
data.head(3)


# #### <font color ='red'> See how many rows and how many columns  

# In[3]:


data.shape   # 15028 rows and 6 columns 


# #### <font color ='red'> Remove all rows with na cases

# In[4]:


data = data.dropna()
data.shape 


# ##### What are the unique causes of death in this data set?

# In[5]:


data.head(2)


# In[7]:


causes =  data["Cause Name"].unique()
causes


# #### Remove 'All Causes' from the Cause death Name column 

# In[8]:


data = data[data["Cause Name"] !="All Causes"]
causes =  data["Cause Name"].unique()
causes


# In[9]:


len(causes)


# #### Find the unique causes of “State”,

# In[10]:


data.head(3)


# In[11]:


state = data["State"].unique()
state


# In[12]:


data1 = data[data["State"] !="United States"]

state = data1["State"].unique()
state


# In[13]:


len(state)


# ### What were the total number of deaths in the United States from 1999 to 2015?

# In[14]:


data.head(0)


# In[15]:


data["Deaths"].sum()


# ### What is the trend of number of deaths per year?

# In[16]:


dyear= data.groupby(["Year"]).sum()
dyear


# In[18]:


dyear["Deaths"].plot(title="Death per year \n 1999-2015")


# #### Which 10 states had the highest number of deaths in all years?

# In[19]:


data1 = data[data["State"] !="United States"]
dataset2 = data1.groupby("State").sum()
dataset2.sort_values("Deaths", ascending=False , inplace = True)
dataset2.head(10)


# In[20]:


dataset2["Deaths"].head(10).plot.bar(title="Top ten states with highest death number \n 1999-2015 ")


# ## 6.	What were the top causes of deaths in the United States during this period?

# In[21]:


dataset1 = data[data["Cause Name"] !="All Causes"]
dataset2 = dataset1.groupby("Cause Name").sum()
dataset2.sort_values("Deaths", ascending=False , inplace = True)
dataset2.head(10)


# In[22]:


dataset2["Deaths"].head(10).plot.bar(title="Top ten casues of death in USA \n 1999-2015 ")


# #### Analyze guns deaths in the US

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='white', color_codes=True)
get_ipython().magic(u'matplotlib inline')


# In[2]:


dataset = pd.read_csv('Death data.csv', index_col=0)
print(dataset.shape)
dataset.index.name = 'Index'
dataset.columns = map(str.capitalize, dataset.columns)
dataset.head(5)


# In[5]:


# Organizing the data by the year, then by month:
dataset_Gun = dataset
dataset_Gun.sort_values(['Year', 'Month'], inplace=True)


# #### Annual U.S. suicide gun deaths 2012-2014, by gender

# In[6]:


dataset_Gun.Sex.value_counts(normalize=False)


# In[8]:


dataset_byGender = dataset_Gun.groupby('Sex').count()
dataset_byGender


# In[29]:


dataset_Gun.Sex.value_counts(normalize=False).plot.bar(title='Annual U.S.\suicide gun deaths \n 2012-2014, by gender')


# In[30]:


dataset_byGender = dataset_Gun.groupby(['Sex']).count()
dataset_byGender


# In[31]:


dataset_byGender.plot.bar(title='Annual U.S. suicide gun deaths \n 2012-2014, by gender')


# ### Average annual death toll from guns in the United States from 2012 to 2014, by race

# In[12]:


dataset_byRace = dataset
(dataset_byRace.Race.value_counts(ascending=False) *100/100000)


# In[13]:


(dataset_byRace.Race.value_counts(ascending=False) *100/100000).plot.bar(title=' Percentage of Average annual\death toll from guns in the United States \nfrom 2012 to 2014, by race')


# In[34]:


dataset_byRace.Race.value_counts(normalize=False)
dataset_byRace.Race.value_counts(normalize=False).plot.bar(title='Annual U.S.\suicide gun deaths \n 2012-2014, by Race')


# #### 3.	Rate of gun deaths in the U.S. per 100,000 population 2012-2014, by race.

# In[35]:


dataset_byRace = dataset
print (dataset_byRace.shape)
dataset_byRace.head(2)


# In[36]:


dataset_byRace = dataset
(dataset_byRace.Race.value_counts(ascending=False) *100/100000)


# In[37]:


(dataset_byRace.Race.value_counts(ascending=False) *100/100000).plot.bar(title='Rate of\gun deaths in the U.S. per 100,000 population \n2012-2014, by race')


# 4.	 Annual number of gun deaths in the United States on average from 2012 to 2014, by cause

# In[18]:


dataset_byRace.Intent.value_counts(sort =True , ascending=False) 


# In[17]:


dataset_byRace.Intent.value_counts(sort=True).plot.bar(title='Annual number\of gun deaths in the United States on average \n from 2012 to 2014, by cause')


# 5.	Average annual death toll from guns in the United States from 2012 to 2014, by cause

# In[40]:


dataset_byRace.Intent.value_counts(ascending=False) *100/100000


# In[21]:


(dataset_byRace.Intent.value_counts(ascending=False) *100/100000).plot.bar(title='The 100k Percentage of gun deaths tools in the U.S.\n2012-2014, by cause')


# 6.	Percentage of annual suicide gun deaths in the United States from 2012 to 2014, by year

# In[42]:


dataset_byRace.Year.value_counts(ascending=True) *100/100000


# In[22]:


(dataset_byRace.Year.value_counts(ascending=True) *100/100000).plot.bar(title='Percentage of annual suicide gun deaths in the United States \nfrom 2012 to 2014, by year')

