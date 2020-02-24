#!/usr/bin/env python
# coding: utf-8

# In[15]:


import random
import time
import sys

import SortingMethods as sm


# In[16]:


if __name__ == '__main__':
    sys.setrecursionlimit(10**6)


# In[3]:


length = int(input("How many values would you like to sort? "))


# In[4]:


a = 0
b = int(input("What is the highest value you would like in the array? "))


# In[13]:


print('\n', '='*68)


# In[5]:


nums = []
for i in range(length):
    nums.append(random.randint(a, b))


# In[6]:


alg = sm.SortingMethod(nums)


# In[7]:


t_bubblesort_0 = time.time()
alg.bubblesort()
t_bubblesort_1 = time.time()

bubblesort_time = t_bubblesort_1 - t_bubblesort_0
print(f"Bubble Sort ------ {round(bubblesort_time, 4)} seconds")


# In[8]:


t_selectionsort_0 = time.time()
alg.selectionsort()
t_selectionsort_1 = time.time()

selectionsort_time = t_selectionsort_1 - t_selectionsort_0
print(f"Selection Sort --- {round(selectionsort_time, 4)} seconds")


# In[9]:


t_insertionsort_0 = time.time()
alg.insertionsort()
t_insertionsort_1 = time.time()

insertionsort_time = t_insertionsort_1 - t_insertionsort_0
print(f"Insertion Sort --- {round(insertionsort_time, 4)} seconds")


# In[10]:


t_mergesort_0 = time.time()
alg.mergesort()
t_mergesort_1 = time.time()

mergesort_time = t_mergesort_1 - t_mergesort_0
print(f"Merge Sort ------- {round(mergesort_time, 4)} seconds")


# In[11]:


t_quicksort_0 = time.time()
alg.quicksort()
t_quicksort_1 = time.time()

quicksort_time = t_quicksort_1 - t_quicksort_0
print(f"Quick Sort ------- {round(quicksort_time, 4)} seconds")


# In[ ]:




