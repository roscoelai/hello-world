#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Read data from file into a DataFrame.
import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw() # Prevent pop-up window

filetype_list = (
    ("Excel files", "*.xls"), 
    ("Excel files", "*.xlsx"), 
    ("Excel files", "*.xlsm"), 
    ("Tab-delimited text files", "*.txt"), 
    ("CSV files", "*.csv"), 
    ("all files", "*.*"))

file_path = filedialog.askopenfilename(initialdir = "F:/", filetypes = filetype_list)

if file_path.endswith(("xlsx", "xls", "xlsm")):
    data = pd.read_excel(file_path)
    print("File read: {0}".format(file_path))
elif file_path.endswith("txt"):
    data = pd.read_csv(file_path, delimiter='\t')
    print("File read: {0}".format(file_path))
elif file_path.endswith("csv"):
    data = pd.read_csv(file_path)
    print("File read: {0}".format(file_path))
elif len(file_path) == 0:
    print("No file selected.")
else:
    print("File format not supported (yet).")

del file_path


# In[24]:


data.head()


# In[93]:


# How many entries are there?
non_na_count_list = list(data.isnull().count() - data.isnull().sum())

# find the mode.
from statistics import mode

#data_mode = max(set(non_na_count_list), key=non_na_count_list.count)
data_mode = mode(non_na_count_list)
data_mode


# In[26]:


data2 = data[:data_mode]
data2.tail()


# In[27]:


# Number of columns that are completely empty.
len(data2.columns[data2.isna().sum() == data_mode])


# In[29]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

plt.plot(data2['Visit Start Time'], data2['Visit End Time'], 'bo')
plt.xlabel("Start Time")
plt.ylabel("End Time")
plt.show()


# In[34]:


snack_list = ['MnM Weight/g (Difference)', 
              'Potato Chips Weight/g (Difference)', 
              'Raisins Weight/g (Difference)', 
              'Ritz Crackers Weight/g (Difference)', 
              'Water A Weight/g (Difference)', 
              'Water B Weight/g (Difference)', 
              'Water C Weight/g (Difference)', 
              'Ribena A Weight/g (Difference)', 
              'Ribena B Weight/g (Difference)', 
              'Ribena C Weight/g (Difference)']

data3 = data2[snack_list]


# In[42]:


data3.hist(bins = 20, figsize = (20,10))


# In[88]:


snack_list_1 = ['MnM Weight/g (Difference)', 
                'Potato Chips Weight/g (Difference)', 
                'Raisins Weight/g (Difference)', 
                'Ritz Crackers Weight/g (Difference)']

snack_list_2 = ['Water A Weight/g (Difference)', 
                'Water B Weight/g (Difference)', 
                'Water C Weight/g (Difference)', 
                'Ribena A Weight/g (Difference)', 
                'Ribena B Weight/g (Difference)', 
                'Ribena C Weight/g (Difference)']

data3a = data3[snack_list_1]
data3b = data3[snack_list_2]


# In[94]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 1, figsize=(20, 10))
axs[0].boxplot(data3a.dropna().T, labels = snack_list_1)
axs[1].boxplot(data3b.T, labels = snack_list_2)
axs[0].set_ylabel("Weight difference (g)")
axs[1].set_ylabel("Weight difference (g)")


# In[87]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize = (12,4))
sns.violinplot(data=data3a.dropna(), inner="quartile")

