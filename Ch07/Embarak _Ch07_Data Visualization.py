
# coding: utf-8

# # Chapter 7: Data Visualization  

# In[3]:


import pandas as pd

dataset = pd.read_csv("./Data/Salaries.csv")

rank = dataset['rank']
discipline =  dataset['discipline']
phd =  dataset['phd']
service =  dataset['service']
sex =  dataset['sex']
salary =  dataset['salary']

dataset.head()


# # Line plotting

# In[4]:


dataset.plot()


# In[5]:


dataset[["rank", "discipline","phd","service", "sex", "salary"]].plot()


# In[6]:


dataset[["phd","service"]].plot()


# # Visualize grouped data

# In[7]:


dataset1 = dataset.groupby(['service']).sum()
dataset1.sort_values("salary", ascending = False, inplace=True)
dataset1.head()


# In[8]:


dataset1["salary"].plot.bar()


# # Bar plotting

# In[9]:


dataset[[ 'phd', 'service' ]].head(10).plot.bar()


# In[10]:


dataset[['phd', 'service']].head(10).plot.bar(title="Ph.D. Vs Service\n 2018")


# In[11]:


dataset[['phd', 'service']].head(10).plot.bar(title="Ph.D. Vs Service\n 2018" , color=['g','red'])


# # Pie Chart

# In[12]:


dataset["salary"].head(10).plot.pie(autopct='%.2f')


# # Box Plotting

# In[13]:


dataset[["phd","salary"]].head(100).plot.box()


# In[14]:


dataset[["phd","service"]].plot.box()


# # Histogram

# In[15]:


dataset["salary"].head(20).plot.hist()


# In[ ]:


# A scatterplot


# In[3]:


# Exercises


# In[4]:


import matplotlib.pyplot as plt
plt.style.use('classic')
get_ipython().magic(u'matplotlib inline')
import numpy as np
import pandas as pd


# In[30]:


# Create temprature data
rng = np.random.RandomState(0)
season1 = np.cumsum(rng.randn(500, 6), 0)


# In[32]:


# Plot the data with Matplotlib defaults
plt.plot(season1)
plt.legend('ABCDEF', ncol=2, loc='upper left');


# In[33]:


import seaborn as sns
iris = sns.load_dataset("iris")
iris.head()
sns.pairplot(iris, hue='species', size=2.5);


# In[36]:


import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()


# In[37]:


tips['Tips Percentage'] = 100 * tips['tip'] / tips['total_bill']
grid = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
grid.map(plt.hist, "Tips Percentage", bins=np.linspace(0, 40, 15));


# In[39]:


import seaborn as sns
tips = sns.load_dataset('tips')
with sns.axes_style(style='ticks'):
    g = sns.factorplot("day", "total_bill", "sex", data=tips, kind="box")
    g.set_axis_labels("Bill Day", "Total Bill Amount");


# In[43]:


import seaborn as sns
tips = sns.load_dataset('tips')
with sns.axes_style('white'):
    sns.jointplot( "total_bill", "tip", data=tips, kind='hex')


# In[25]:


import seaborn as sns
planets = sns.load_dataset('planets')
planets.head()

