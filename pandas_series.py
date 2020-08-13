#!/usr/bin/env python
# coding: utf-8

# # 1. Use pandas to create a Series from the following data:

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])


# In[3]:


#a. Name the variable that holds the series fruits.
pd.core.series.Series
fruits


# In[4]:


#b. Run .describe() on the series to see what describe returns for a series of strings.
fruits.describe()


# In[5]:


#c. Run the code necessary to produce only the unique fruit names.
(pd.Series.unique(fruits))


# In[6]:


pd.unique(list(fruits)) 


# In[7]:


fruits.unique()


# In[8]:


#d. Determine how many times each value occurs in the series.
fruits.value_counts() 


# In[9]:


#e. Determine the most frequently occurring fruit name from the series.
fruits.mode()


# In[10]:


#f. Determine the least frequently occurring fruit name from the series.
fruits.value_counts().nsmallest(keep="all")


# In[11]:


#g. Write the code to get the longest string from the fruits series.
longest_string = max(fruits, key=len)
longest_string


# In[12]:


#h. Find the fruit(s) with 5 or more letters in the name.
fruits[fruits.str.len() >= 5]


# In[13]:


#i. Capitalize all the fruit strings in the series.
fruits.str.capitalize()


# In[14]:


#j. Count the letter "a" in all the fruits (use string vectorization)
fruits.str.count('a')


# In[15]:


#k. Output the number of vowels in each and every fruit.
fruits.str.count('[aeiou]')


# In[16]:


#l. Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.
fruits[fruits.apply(lambda x: x.count('o') >= 2)]


# In[17]:


#m. Write the code to get only the fruits containing "berry" in the name
fruits[fruits.str.find('berry') != -1]


# In[18]:


#n. Write the code to get only the fruits containing "apple" in the name
fruits[fruits.str.find('apple') != -1]


# In[19]:


#o. Which fruit has the highest amount of vowels?
fruits[max(fruits.str.count('[aeiou]'))]


# # 2. Use pandas to create a Series from the following data:

# In[20]:


numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])


# In[21]:


# What is the data type of the series?
numbers.dtype


# In[22]:


# Use series operations to convert the series to a numeric data type.
new_numbers = numbers.apply(lambda numbers: numbers.replace('$', '').replace(',', ''))
new_numbers.astype('float')


# In[23]:


float_series = numbers.str.replace('$', '').str.replace(',', '').astype('float')
float_series


# In[24]:


# What is the maximum value? The minimum?
new_numbers_max = max(float(i) for i in new_numbers) 
new_numbers_max


# In[25]:


new_numbers_min = min(float(i) for i in new_numbers) 
new_numbers_min


# In[26]:


# Bin the data into 4 equally sized intervals and show how many values fall into each bin.
pd.cut(float_series, 4).value_counts().sort_index()


# In[27]:


# Plot a histogram of the data. Be sure to include a title and axis labels.
pd.cut(float_series, 4).value_counts().sort_index(ascending=False).plot(kind='barh', width=1, ec='black')
plt.title('4 Bins of Numbers')
plt.xlabel('Count')
plt.ylabel('Data Set')
plt.show()


# # 3. Use pandas to create a Series from the following exam scores:

# In[28]:


exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])


# In[29]:


type(exam_scores)


# In[30]:


# What is the minimum exam score? The max, mean, median?


# In[31]:


exam_scores.min()


# In[32]:


exam_scores.max()


# In[33]:


exam_scores.mean()


# In[34]:


exam_scores.median()


# In[35]:


exam_scores.describe()


# In[36]:


# Plot a histogram of the scores.
exam_scores.plot.hist(ec='black')
plt.title('Exam Scores')
plt.xlabel('Grade Range')
plt.ylabel('Grade Frequency')
plt.show()


# In[37]:


# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.¶


# In[38]:


bin_edges = [0, 70, 75, 80, 90, 101]
bin_labels = ['F', 'D', 'C', 'B', 'A']
pd.cut(exam_scores, bins=bin_edges, labels=bin_labels).value_counts().sort_index()


# In[39]:


pd.cut(exam_scores, 
       bins=bin_edges, 
       labels=bin_labels).value_counts().sort_index().plot(kind='barh', 
                                                           color='thistle',
                                                           ec='black',
                                                           width=.8)
plt.title('Letter Grades')
plt.xlabel('Number of Students')
plt.ylabel('Letter Grade')
plt.show()


# In[40]:


# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.
curve = 100 - exam_scores.max()
curve


# In[41]:


curved_scores = exam_scores + curve
curved_scores


# In[42]:


bin_edges = [0, 70, 75, 80, 90, 101]

bin_labels = ['F', 'D', 'C', 'B', 'A']

pd.cut(curved_scores, bins=bin_edges, labels=bin_labels).value_counts().sort_index()


# In[43]:


pd.cut(curved_scores, 
       bins=bin_edges, 
       labels=bin_labels).value_counts().sort_index().plot(kind='barh', 
                                                           color='plum',
                                                           ec='black',
                                                           width=.8) 
plt.title('Curved Letter Grades')
plt.xlabel('Number of Students')
plt.ylabel('Letter Grade')
plt.show()


# # 4. Use pandas to create a Series from the following string:

# In[44]:


letters = ('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')


# In[45]:


letters_list = letters.replace('', ' ').strip().split(' ')


# In[46]:


letters = pd.Series(letters_list)


# In[47]:


type(letters)


# In[48]:


# What is the most frequently occuring letter? Least frequently occuring?
letters.value_counts()


# In[49]:


letters.value_counts().nlargest(n=1, keep='all')


# In[50]:


letters.value_counts().nsmallest(n=1, keep='all')


# In[51]:


# How many vowels are in the list?
letters.str.count('[aeiou]').sum()


# In[52]:


# How many consonants are in the list?
letters.str.count('[^aeiou]').sum()


# In[53]:


# Create a series that has all of the same letters, but uppercased
letters.str.upper()


# In[54]:


# Create a bar plot of the frequencies of the 6 most frequently occuring letters.
letters.value_counts().head(6).plot(kind='barh')
plt.title('Top 6 Letters')
plt.gca().invert_yaxis()
plt.show()


# ### 5. Complete the exercises from https://gist.github.com/ryanorsinger/f7d7c1dd6a328730c04f3dc5c5c69f3a, but use pandas Series for the data structure instead of lists and use Series subsetting/indexing and vectorization options instead of loops and lists.

# In[55]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

fruits = pd.Series(fruits)
numbers = pd.Series(numbers)


# In[56]:


# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
#list comprehension solution
#uppercased_fruits = [fruit.upper() for fruit in fruits]
#uppercased_fruits

uppercased_fruits = fruits.str.upper()
uppercased_fruits


# In[57]:


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
#list comprehension solution
#capitalized_fruits = [fruit.capitalize() for fruit in fruits]
#capitalized_fruits

capitalized_fruits = fruits.str.capitalize()
capitalized_fruits


# In[58]:


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
#fruits_with_more_than_two_vowels = [fruit for fruit in fruits if (
#   fruit.count("a") + 
#   fruit.count("e") + 
#   fruit.count("i") + 
#   fruit.count("o") + 
#   fruit.count("u")) > 2]
#fruits_with_more_than_two_vowels

fruits_with_more_than_two_vowels = fruits[fruits.str.count('[aeiou]') > 2]
fruits_with_more_than_two_vowels


# In[59]:


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
#fruits_with_only_two_vowels = [fruit for fruit in fruits if (
#   fruit.count("a") + 
#   fruit.count("e") + 
#   fruit.count("i") + 
#   fruit.count("o") + 
#   fruit.count("u")) == 2]
#fruits_with_only_two_vowels

fruits_list_with_vowels = fruits.str.count('[aeiouAEIOU]') ==2
fruits_with_only_two_vowels = fruits[fruits_list_with_vowels]
fruits_with_only_two_vowels


# In[60]:


# Exercise 5 - make a list that contains each fruit with more than 5 characters
#[fruit for fruit in fruits if (len(fruit) > 5)]

fruits[fruits.str.len() > 5]


# In[61]:


# Exercise 6 - make a list that contains each fruit with exactly 5 characters
#[fruit for fruit in fruits if (len(fruit) == 5)]

fruits[fruits.str.len() == 5]


# In[62]:


# Exercise 7 - Make a list that contains fruits that have less than 5 characters
#[fruit for fruit in fruits if (len(fruit) < 5)]

fruits[fruits.str.len() < 5]


# In[63]:


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
#[len(fruit) for fruit in fruits]

fruits.str.len()


# In[64]:


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
#fruits_with_letter_a = [fruit for fruit in fruits if "a" in fruit] 
#fruits_with_letter_a

fruits_with_letter_a = fruits[fruits.apply(lambda fruits: fruits.count('a') >= 1)]
fruits_with_letter_a


# In[65]:


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
#even_numbers = [number for number in numbers if number % 2 == 0]
#even_numbers

even_numbers = numbers[numbers.apply(lambda numbers: numbers % 2 == 0)]
even_numbers


# In[66]:


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
#odd_numbers = [number for number in numbers if number % 2 != 0]
#odd_numbers

odd_numbers = numbers[numbers.apply(lambda numbers: numbers % 2 == 1)]
odd_numbers


# In[67]:


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
#positive_numbers = [number for number in numbers if number > 0]
#positive_numbers

positive_numbers = numbers[numbers.apply(lambda numbers: numbers > 0)]
positive_numbers


# In[68]:


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
#negative_numbers = [number for number in numbers if number < 0]
#negative_numbers

negative_numbers = numbers[numbers.apply(lambda numbers: numbers < 0)]
negative_numbers


# In[69]:


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
#[number for number in numbers if number > 9 or number < -9]

numbers_two_digits = numbers[~numbers.between(-9,9)]
numbers_two_digits


# In[70]:


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
#numbers_squared = [number ** 2 for number in numbers]
#numbers_squared

numbers_squared = numbers ** 2
numbers_squared


# In[71]:


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
#odd_negative_numbers = [number for number in numbers if number < 0 and number % 2 != 0]
#odd_negative_numbers

odd_negative_numbers = numbers[(numbers % 2 != 0) & (numbers < 0)]
odd_negative_numbers


# In[72]:


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.
#numbers_plus_5 = [number + 5 for number in numbers]
#numbers_plus_5

numbers_plus_5 = numbers + 5
numbers_plus_5


# In[73]:


# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
#def is_prime(num):
#   prime_check = False
#   if num > 1:
#       for i in range(2, num):
#           if (num % i) == 0:
#               prime_check = False
#               break
#       else:
#           prime_check = True 
#   return prime_check
#primes= [number for number in numbers if is_prime(number)]
#primes

primes = list(numbers[numbers.apply(lambda n: all(n % i != 0 for i in range(2,n)) and n > 0)])
primes

