#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Use the iris database to answer the following quesitons:


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


iris = sns.load_dataset('iris')
iris.dtypes


# In[4]:


#1. What does the distribution of petal lengths look like?


# In[5]:


iris 


# ## distplot( ) function:
# - Draws a histogram and fits/plots a gaussian kernel density estimate (KDE)
# 

# In[6]:


sns.distplot(iris.petal_length)


# In[7]:


sns.distplot(iris.petal_length, kde=True)


# In[8]:


sns.distplot(iris.petal_length, kde=False)


# In[9]:


sns.kdeplot(iris.petal_length, shade=True)


# In[10]:


sns.jointplot(iris.petal_length, iris.sepal_width, kind="kde")


# In[11]:


#2. Is there a correlation between petal length and petal width?


# In[12]:


sns.relplot(x='petal_width', y='petal_length', hue="species", data=iris)
plt.title("Petal length vs Petal width")


# In[13]:


#3. Would it be reasonable to predict species based on sepal width and sepal length?


# In[14]:


iris.species.nunique()


# In[15]:


sns.relplot(x='sepal_width', y='sepal_length', hue="species", data=iris)


# In[16]:


sns.relplot(x='sepal_width', y='species', hue="species", data=iris)


# In[17]:


sns.relplot(x='sepal_length', y='species', hue="species", data=iris)


# In[18]:


#4. Which features would be best used to predict species?


# - Petal length and petal width

# In[19]:


sns.relplot(x='petal_width', y='petal_length', hue="species", data=iris)


# In[20]:


sns.pairplot(iris, hue="species")


# In[21]:


#1. Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?
# Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

from pydataset import data
anscombe = sns.load_dataset('anscombe')
anscombe.dtypes


# In[22]:


anscombe = sns.load_dataset('anscombe')
anscombe.head()


# In[23]:


anscombe = data('anscombe')
data('anscombe', show_doc = True)


# In[68]:


datasets = anscombe.groupby('dataset')
datasets.describe()


# In[66]:


sns.relplot(x='x', y='y', hue="y", data=anscombe)


# In[28]:


sns.relplot(x='x',y='y',hue='dataset',col='dataset',data=anscombe)
plt.tight_layout();


# In[32]:


#2. Load the InsectSprays dataset and read it's documentation. Create a boxplot that shows the effectiveness of the different insect sprays.


# In[33]:


from pydataset import data


# In[34]:


insect_sprays = data('InsectSprays')
insect_sprays.head()


# In[35]:


insect_sprays.spray.nunique()


# In[36]:


data('InsectSprays', show_doc = True)


# In[37]:


sns.boxplot(data=insect_sprays, y='count', x='spray')
plt.title('Effectiveness of Different Insect Sprays')
plt.xlabel('Insect Sprays')
plt.ylabel('Number of Observed Insects')
plt.show()


# In[38]:


#3. Load the swiss dataset and read it's documentation. Create visualizations to answer the following questions:


# In[39]:


swiss = data('swiss')
swiss.head()


# In[40]:


data('swiss', show_doc=True)


# In[41]:


# Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes catholic)


# In[42]:


sns.distplot(swiss.Catholic)


# In[43]:


catholic_bool = lambda x: x > 50
swiss['is_catholic'] = swiss.Catholic.apply(catholic_bool)
swiss.head()


# In[44]:


# Does whether or not a province is Catholic influence fertility?


# In[45]:


sns.relplot(x='Catholic',y='Fertility',hue='is_catholic',data=swiss)
plt.title('Does being Catholic influence fertility?')


# In[46]:


# What measure correlates most strongly with fertility?


# In[47]:


sns.regplot(x='Agriculture',y='Fertility',data=swiss)


# In[48]:


sns.regplot(x='Examination',y='Fertility',data=swiss)


# In[49]:


sns.regplot(x='Education',y='Fertility',data=swiss)


# In[50]:


sns.regplot(x='Catholic',y='Fertility',data=swiss)


# In[51]:


sns.regplot(x='Infant.Mortality',y='Fertility',data=swiss)


# In[52]:


#4. Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.


# In[53]:


from env import host, username, password
url = (f'mysql+pymysql://{username}:{password}@{host}/chipotle')


# In[54]:


chipotle = pd.read_sql('SELECT * FROM orders', url)
chipotle.head()


# In[55]:


pop_items = chipotle.groupby('item_name').quantity.agg('sum')
pop_items.sort_values(ascending=False)


# In[56]:


money = chipotle.assign(price = chipotle['item_price'].str.replace('$','').astype(float))
money


# In[57]:


rev_items = money.groupby('item_name').price.agg('sum')
rev_items.sort_values(ascending=False)


# In[58]:


pop_and_rev = pd.merge(pop_items, rev_items, left_on = 'item_name', right_on = 'item_name', how = 'inner')
sorted_chipotle = pop_and_rev.sort_values('quantity', ascending=False)
top_chipotle_items = sorted_chipotle.head(4)
top_chipotle_items


# In[59]:


plt.figure(figsize=(8,4))
plt.title('Revenue for Top 4 Items at Chipotle')
sns.barplot(x=pop_and_rev.index, y='price', data=sorted_chipotle)
plt.xlabel('Item Name')
plt.ylabel('Revenue')


# In[60]:


#5. Load the sleepstudy data and read it's documentation. Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant line showing the average change in reaction time.


# In[61]:


sleep = data('sleepstudy')
data('sleepstudy', show_doc=True)


# In[62]:


avg_sleep = pd.DataFrame(sleep.groupby('Days').Reaction.agg('mean'))
plt.plot(avg_sleep.index, avg_sleep.Reaction, linewidth=5)


# In[63]:


sleep.shape


# In[64]:


sleep.describe()


# In[65]:


plt.figure(figsize=(15,10))
sns.lineplot(x='Days', y='Reaction',hue='Subject', data=sleep, palette='muted', alpha=.47)
sleep_avg = sns.lineplot(x='Days',y='Reaction',data=sleep, linewidth=3, color='blue')
plt.title('Sleep Deprivation Study')
plt.xlabel('Days')
plt.ylabel('Reaction Time in ms')
plt.legend()
plt.show()

