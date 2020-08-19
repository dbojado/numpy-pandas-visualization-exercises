#!/usr/bin/env python
# coding: utf-8

# In[1]:


#For the following exercises, you'll need to load several datasets using the pydataset library. (If you get an error when trying to run the import below, use pip to install the pydataset package.)


# In[2]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


from pydataset import data


# In[4]:


#When the instructions say to load a dataset, you can pass the name of the dataset as a string to the data function to load the dataset. You can also view the documentation for the data set by passing the show_doc keyword argument.

#mpg = data('mpg') # load the dataset and store it in a variable
# data('mpg', show_doc=True) # view the documentation for the dataset


# ## Problem 1

# In[5]:


#1. Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:


# In[6]:


data('mpg', show_doc=True)


# In[7]:


mpg = data('mpg')
mpg.head()


# In[8]:


# On average, which manufacturer has the best miles per gallon?
mpg['average_mileage'] = (mpg.cty + mpg.hwy) / 2
mpg.groupby('manufacturer').average_mileage.mean().sort_values(ascending=False).idxmax()


# In[9]:


# How many different manufacturers are there?
mpg.manufacturer.nunique()


# In[10]:


# How many different models are there?
mpg.model.nunique()


# In[11]:


# Do automatic or manual cars have better miles per gallon?
mpg['trans_category'] = np.where(mpg.trans.str.startswith('a'), 'auto', 'manual')
mpg.groupby('trans_category')[['cty', 'hwy']].mean()


# ## Problem 2

# In[12]:


#2. Joining and Merging


# In[13]:


# Copy the users and roles dataframes from the examples above. 


# In[14]:


users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


# In[15]:


roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


# In[16]:


# What do you think a right join would look like? An outer join? 


# In[17]:


right_join = pd.merge(users, 
                    roles, 
                    left_on='role_id', 
                    right_on='id', 
                    how='right').drop(columns='role_id').rename(columns={'id_x': 'id', 
                                                                         'name_x': 'employee',
                                                                         'id_y': 'role_id',
                                                                         'name_y': 'role'}
                                                                )
right_join


# In[18]:


outer_join = pd.merge(users, 
         roles, 
         left_on='role_id', 
         right_on='id', 
         how='outer').drop(columns='role_id').rename(columns={'id_x': 'id', 
                                                            'name_x': 'employee',
                                                            'id_y': 'role_id',
                                                            'name_y': 'role'}
                                                    )
outer_join


# In[19]:


# What happens if you drop the foreign keys from the dataframes and try to merge them?


# In[20]:


users_drop = users.drop(columns='role_id')
users_drop


# ## Problem 3

# In[21]:


#3. Getting data from SQL databases


# In[22]:


#a. Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.


# In[23]:


from env import host, username, password


# In[24]:


def get_db_url(db, username=username, host=host, password=password):
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'


# In[25]:


#b. Use your function to obtain a connection to the employees database.


# In[26]:


sql_query = 'SELECT * FROM employees'


# In[27]:


employees = pd.read_sql(sql_query, get_db_url('employees'))


# In[28]:


employees.to_csv('employees.csv')


# In[29]:


employees = pd.read_csv('employees.csv', index_col=0)
employees.head()


# In[30]:


#c. Once you have successfully run a query:


# In[31]:


# Intentionally make a typo in the database url. What kind of error message do you see?


# - You get this: 
#     "OperationalError: (pymysql.err.OperationalError) (1044, "Access denied for user 'darden_1037'@'%' to database 'titles'")"
# 

# In[32]:


# sql_query = 'SELECT * FROM titles'

# titles = pd.read_sql(sql_query, get_db_url('titles'))
# titles.head()


# In[33]:


# Intentionally make an error in your SQL query. What does the error message look like?


# - You get this:
#     "ProgrammingError: (pymysql.err.ProgrammingError) (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1")"

# In[34]:


# sql_query = 'SELECT # FORM titles'

# titles = pd.read_sql(sql_query, get_db_url('employees'))
# titles.head()


# In[35]:


#d. Read the employees and titles tables into two separate dataframes
sql_query = 'SELECT * FROM titles'
titles = pd.read_sql(sql_query, get_db_url('employees'))
titles.head()


# In[36]:


#e. Visualize the number of employees with each title.


# In[37]:


current_bool = titles.to_date == titles.to_date.max()


# In[38]:


current_employee_titles = titles[current_bool]


# In[39]:


current_title_values = current_employee_titles.title.value_counts()


# In[40]:


current_title_values.plot.barh(color='deepskyblue', 
                               ec='black', 
                               width=.8)

plt.title('Count of Current Employees Who Hold Each Title')
plt.xlabel('Number of Employees')

# reorder y-axis of horizontal bar chart
plt.gca().invert_yaxis()

plt.show()


# In[41]:


#f. Join the employees and titles dataframes together.


# In[42]:


employees.shape


# In[43]:


titles.shape


# In[44]:


all_emp_titles = employees.merge(titles, on='emp_no')
all_emp_titles.head()


# In[45]:


all_emp_titles.shape


# In[46]:


#g. Visualize how frequently employees change titles.


# In[47]:


changes = all_emp_titles.emp_no.value_counts()


# In[48]:


changes.value_counts().plot(kind='barh', 
                            color='deepskyblue', 
                            ec='black', 
                            width=.8)

plt.title('How Common is it for Employees to Change Titles?')
plt.ylabel('Number of Title Changes')
plt.yticks(ticks=[0,1,2], labels=['0 Changes', '1 Change', '2 Changes'])

# reorder y-axis of horizontal bar chart
plt.gca().invert_yaxis()

plt.show()


# In[49]:


#h. For each title, find the hire date of the employee that was hired most recently with that title.


# In[50]:


all_emp_titles.groupby('title').hire_date.max()


# In[51]:


#i. Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL and python/pandas code)


# In[52]:


dept_title_query = '''

                    SELECT t.emp_no, 
                    t.title, 
                    t.from_date, 
                    t.to_date, 
                    d.dept_name 
                    FROM departments AS d 
                    JOIN dept_emp AS de USING(dept_no) 
                    JOIN titles AS t USING(emp_no);

                    '''


# In[53]:


dept_titles = pd.read_sql(dept_title_query, get_db_url('employees'))


# In[54]:


current_titles = dept_titles[dept_titles.to_date == dept_titles.to_date.max()]


# In[55]:


current_titles_crosstab = pd.crosstab(current_titles.dept_name, current_titles.title)
current_titles_crosstab


# ## Problem 4

# In[56]:


#4. Use your get_db_url function to help you explore the data from the chipotle database. Use the data to answer the following questions:


# In[57]:


chipotle_sql_query = '''
                     SELECT *
                     FROM orders;
                     '''


# In[58]:


orders = pd.read_sql(chipotle_sql_query, get_db_url('chipotle'))
orders.head()


# In[59]:


orders.shape


# In[60]:


orders.info()


# In[61]:


# What is the total price for each order?


# In[62]:


orders['item_price'] = orders.item_price.str.replace('$', '').astype(float)
orders.info()


# In[63]:


order_totals = orders.groupby('order_id').item_price.sum()
order_totals.sample(10)


# In[64]:


# What are the most popular 3 items?


# In[65]:


top_three = orders.groupby('item_name').quantity.sum().sort_values(ascending=False).head(3)
top_three


# In[66]:


top_three.plot(kind='barh',
             color='deepskyblue', 
             ec='black', 
             width=.8)

plt.title('The Big Three at Chipotle')
plt.ylabel('Menu Item')

# reorder y-axis of horizontal bar chart
plt.gca().invert_yaxis()

plt.show()


# In[67]:


# Which item has produced the most revenue?


# In[68]:


orders.groupby('item_name').item_price.sum().sort_values(ascending=False).head(1)


# ## Extra Pandas Exercises and Resources

# In[69]:


#https://www.w3resource.com/python-exercises/pandas/index.php
#https://towardsdatascience.com/20-pandas-functions-that-will-boost-your-data-analysis-process-f5dfdb2f9e05
#https://github.com/guipsamora/pandas_exercises
#https://github.com/ajcr/100-pandas-puzzles


# ## More Practice!

# In[70]:


#For even more practice with pandas, you can do the exercises from the SQL module, but instead of using SQL to do the aggregation, sorting, joining, etc, use pandas. That is, read the data from all of the tables into pandas dataframes and manipulate the dataframes.

