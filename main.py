#!/usr/bin/env python
# coding: utf-8

# # To-do-list Project
# 
# ## Goal:
# To create an easy to use tool to organize daily, weekly, and monthly activities

# ### Problems to solve:
# - Run functions from the command line
# - Pass a date as input to a function
# - Take date and turn it into the name of a list

# In[2]:


import pandas as pd
import numpy as np
import sys
from collections import defaultdict


# In[3]:


date_taks = defaultdict(list)

def add_one_time_task(day, task):
    date_taks[day].append(task)
    print(date_taks[day])


# In[ ]:


if sys.argv[1] in ['TASK','Task','task']:
    day = sys.argv[2]
    task = sys.argv[3]
    add_one_time_task(day, task)

