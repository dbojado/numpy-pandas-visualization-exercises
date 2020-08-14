#!/usr/bin/env python
# coding: utf-8

# In[1]:


#For several of the following exercises, you'll need to load several datasets using the pydataset library. 
#If you get an error when trying to run the import below, use pip to install the pydataset package.


# In[2]:


from pydataset import data


# In[3]:


#When the instructions say to load a dataset, you can pass the name of the dataset as a string to the data function to load the dataset. You can also view the documentation for the data set by passing the show_doc keyword argument.


# In[4]:


# data('mpg', show_doc=True) # view the documentation for the dataset
# mpg = data('mpg') # load the dataset and store it in a variable


# In[5]:


#All the datasets loaded from the pydataset library will be pandas dataframes.


# # Problem #1

# In[6]:


import pandas as pd


# In[7]:


#1. Copy the code from the lesson to create a dataframe full of student grades.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from pydataset import data

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})


# In[8]:


df


# In[9]:


#a. Create a column named passing_english that indicates whether each student has a passing grade in reading.

df.english >= 70
df['passing_english'] = df.english >= 70
(df['passing_english'] == False).sum()


# In[10]:


#b. Sort the english grades by the passing_english column. How are duplicates handled?

df.sort_values(by='passing_english')


# In[11]:


#c. Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)

df.sort_values(by=['passing_english', 'name'])


# In[12]:


#d. Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.

df.sort_values(by=['passing_english', 'english'])


# In[13]:


#e. Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

totals = df.iloc[:, 1:4].sum(axis=1)
df['overall_average'] = round((totals / 3), 0).astype(int)
df


# # Problem #2

# In[14]:


#2. Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

data('mpg', show_doc=True)


# In[15]:


mpg = data('mpg')


# In[16]:


# How many rows and columns are there?

mpg.shape


# In[17]:


# What are the data types of each column?

mpg.dtypes


# In[18]:


# Summarize the dataframe with .info and .describe

mpg.info()


# In[19]:


mpg.describe()


# In[20]:


# Rename the cty column to city.

mpg.rename(columns={'cty': 'city'}, inplace=True)
mpg.head(1)


# In[21]:


# Rename the hwy column to highway.

mpg.rename(columns={'hwy': 'highway'}, inplace=True)
mpg.head(1)


# In[22]:


# Do any cars have better city mileage than highway mileage?

bool_series = mpg.city > mpg.highway
mpg[bool_series]
bool_series.sum()


# In[23]:


# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.

mpg = mpg.assign(mileage_difference = mpg.highway - mpg.city)
mpg.head()


# In[24]:


# Which car (or cars) has the highest mileage difference?

bool_series = mpg.mileage_difference == mpg.mileage_difference.max()
mpg[bool_series][['manufacturer', 'model', 'mileage_difference']]


# In[25]:


# Which compact class car has the lowest highway mileage? The best?

bool_series = mpg['class'] == 'compact'
compacts = mpg[bool_series]
compacts.sort_values(by='highway').head(1) 


# In[26]:


compacts.sort_values(by='highway').tail(1)


# In[27]:


# Create a column named average_mileage that is the mean of the city and highway mileage.

mpg['average_mileage'] = (mpg.city + mpg.highway) / 2
mpg.head(2)


# In[28]:


# Which dodge car has the best average mileage? The worst?

bool_series = mpg.manufacturer == 'dodge'
dodges = mpg[bool_series]
dodges.sort_values(by='average_mileage').tail(1)


# In[29]:


dodges.sort_values(by='average_mileage').head(1)


# # Problem #3

# In[30]:


#3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

data('Mammals', show_doc=True)
mammals = data('Mammals')
mammals.head()


# In[31]:


# How many rows and columns are there?

mammals.shape


# In[32]:


# What are the data types?

mammals.dtypes


# In[33]:


# Summarize the dataframe with .info and .describe

mammals.info()


# In[34]:


mammals.describe()


# In[35]:


plt.hist(mammals.weight, bins=20, color='orange', edgecolor='black')

plt.title('Weight of Mammals in kg')
plt.xlabel('kg')
plt.ylabel('Count')

plt.show()


# In[36]:


plt.hist(mammals.speed, bins=15, color='dodgerblue', edgecolor='black')

plt.title('Full Sprint Speed of Mammals in km')
plt.xlabel('km')
plt.ylabel('Count')

plt.show()


# In[37]:


# What is the the weight of the fastest animal?
mammals.loc[mammals.speed.idxmax()].weight


# In[38]:


# What is the overall percentage of specials?
total_specials = mammals.specials.sum()
total_mammals = len(mammals)
overall_percentage_of_specials = round(total_specials / total_mammals * 100,2)
print(f'{overall_percentage_of_specials}%')


# In[39]:


# How many animals are hoppers that are above the median speed? What percentage is this?
median_speed = mammals.speed.median() 
median_speed


# In[40]:


bool_series = (mammals.speed > median_speed) & (mammals.hoppers == True)
fast_hoppers = mammals[bool_series]


# In[41]:


percentage_of_hoppers = round((len(fast_hoppers) / len(mammals)) * 100,2)
print(f'{percentage_of_hoppers}%')

