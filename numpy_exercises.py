#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Use the following code for the questions below:
import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# In[2]:


#1. How many negative numbers are there?
negative_numbers = a < 0
len(a[negative_numbers])


# In[3]:


#2. How many positive numbers are there?
positive_numbers = a > 0
len(a[positive_numbers])


# In[4]:


#3. How many even positive numbers are there?
positive_even_numbers = (a > 0) & (a % 2 == 0)
len(a[positive_even_numbers])


# In[5]:


#4. If you were to add 3 to each data point, how many positive numbers would there be?
positive_numbers = (a + 3) > 0
len(a[positive_numbers])


# In[6]:


#5. If you squared each number, what would the new mean and standard deviation be?
a.mean() ** 2


# In[7]:


a.std() ** 2


# In[8]:


#6. A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.
a - a.mean()


# In[9]:


#7. Calculate the z-score for each data point. Recall that the z-score is given by:
# Z = x − μ / σ
(a - a.mean()) / a.std()


# In[10]:


#8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.


# In[11]:


import numpy as np
# Life w/o numpy to life with numpy


# # Setup 1

# In[12]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[13]:


# Use python's built in functionality/operators to determine the following:


# In[14]:


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
def sum_of_a(nums):
    sum_list = 0
    for num in nums:
        sum_list = sum_list + num
    return sum_list
print(sum_of_a(a))


# In[15]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a.sum()


# In[16]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
def min_of_a(nums):
    num_list = []
    for num in nums:
        num_list.append(num)
    return min(num_list)
print(min_of_a(a))


# In[17]:


a.min()


# In[18]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
def max_of_a(nums):
    num_list = []
    for num in nums:
        num_list.append(num)
    return max(num_list)
print(max_of_a(a))


# In[19]:


a.max()


# In[20]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
def mean_of_a(nums):
    sum_num = 0
    for num in nums:
        sum_num = sum_num + num           
        avg = sum_num / len(nums)
    return avg
print(mean_of_a(a))


# In[21]:


a.mean()


# In[22]:


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
def product_of_a(nums):
    total = 1
    for num in nums:
        total *= num
    return (total)
print(product_of_a(a))


# In[23]:


a.prod() 


# In[24]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
def squares_of_a(nums):
    square_list = []
    for num in nums:
        square_list.append(num**2)
    return (square_list)
print(squares_of_a(a))


# In[25]:


a**2 


# In[26]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
def odds_in_a(nums):
    num_list = []
    for num in nums:
        if num % 2 != 0:
            num_list.append(num)
    return (num_list)
print(odds_in_a(a))


# In[27]:


a[a % 2 == 1]


# In[28]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
def evens_in_a(nums):
    num_list = []
    for num in nums:
        if num % 2 == 0:
            num_list.append(num)
    return (num_list)
print(evens_in_a(a))


# In[29]:


a[a % 2 == 0]


# # Setup 2

# In[30]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...


# In[31]:


# Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.


# In[32]:


b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])


# In[33]:


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
print(sum_of_b)


# In[34]:


b.sum()


# In[35]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) 
print(min_of_b)


# In[36]:


b.min()


# In[37]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
print(max_of_b)


# In[38]:


b.max()


# In[39]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
print(mean_of_b)


# In[40]:


b.mean()


# In[41]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
print(product_of_b)


# In[42]:


b.prod()


# In[43]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
print(squares_of_b)


# In[44]:


b**2


# In[45]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
print(odds_in_b)


# In[46]:


b[b % 2 == 1]


# In[47]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
print(evens_in_b)


# In[48]:


b[b % 2 == 0]


# In[49]:


# Exercise 9 - print out the shape of the array b.
b.shape


# In[50]:


# Exercise 10 - transpose the array b.
b.transpose() 


# In[51]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.reshape(1,6)


# In[52]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape((6,1)) 


# # Setup 3

# In[53]:


c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# In[54]:


# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.


# In[55]:


# Exercise 1 - Find the min, max, sum, and product of c.


# In[56]:


c.min()


# In[57]:


c.max()


# In[58]:


c.sum()


# In[59]:


c.prod()


# In[60]:


# Exercise 2 - Determine the standard deviation of c.


# In[61]:


c.std()


# In[62]:


# Exercise 3 - Determine the variance of c.


# In[63]:


sum(sum((c - c.mean())**2 / 9))


# In[64]:


np.var(c)


# In[65]:


# Exercise 4 - Print out the shape of the array c.


# In[66]:


c.shape


# In[67]:


# Exercise 5 - Transpose c and print out transposed result.


# In[68]:


c.transpose() 


# In[69]:


# Exercise 6 - Get the dot product of the array c with c. 


# In[70]:


np.dot(c,c)


# In[71]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261


# In[72]:


sum(sum(c * c.transpose()))


# In[73]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


# In[74]:


c.prod() * c.transpose().prod()


# # Setup 4

# In[75]:


d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])


# In[76]:


# Exercise 1 - Find the sine of all the numbers in d


# In[77]:


np.sin(d)


# In[78]:


# Exercise 2 - Find the cosine of all the numbers in d


# In[79]:


np.cos(d)


# In[80]:


# Exercise 3 - Find the tangent of all the numbers in d


# In[81]:


np.tan(d)


# In[82]:


# Exercise 4 - Find all the negative numbers in d


# In[83]:


negative_numbers = d < 0
(d[negative_numbers])


# In[84]:


# Exercise 5 - Find all the positive numbers in d


# In[85]:


positive_numbers = d > 0
(d[positive_numbers])


# In[86]:


# Exercise 6 - Return an array of only the unique numbers in d.


# In[87]:


np.unique(d)


# In[88]:


# Exercise 7 - Determine how many unique numbers there are in d.


# In[89]:


len(np.unique(d))


# In[90]:


# Exercise 8 - Print out the shape of d.


# In[91]:


d.shape


# In[92]:


# Exercise 9 - Transpose and then print out the shape of d.


# In[93]:


d.transpose().shape


# In[94]:


# Exercise 10 - Reshape d into an array of 9 x 2


# In[95]:


d.reshape(9,2)


# In[96]:


#9. For even more practice, clone https://github.com/rougier/numpy-100, make your own repo called numpy-100, and then commit and push your solutions to your own repo.

