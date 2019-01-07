#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


# In[137]:


data.head()


# In[148]:


data2 = data.dropna()
data2.shape


# In[240]:


import numpy as np

def lc(x):
    return str(x).lower()

data3 = data2.iloc[:, 9:].apply(np.vectorize(lc))
data3.head()


# In[151]:


data3a = data3.iloc[:, ::2]
data3b = data3.iloc[:, 1::2]
#data3a.tail()
#data3b.tail()


# In[241]:


def unique_list(df):
    ulist = []
    for column in df.columns:
        for item in list(df[column].unique()):
            if item not in ulist:
                ulist.append(item)
    return ulist

print(unique_list(data3a))
print(unique_list(data3b))


# In[172]:


dict1 = {'never': 0, 'once in a while': 1, 'a lot': 2, 'most of the time': 3}
dict2 = {'never do it': 0, 'does not help': 1, 'helps a little': 2, 'helps a lot': 3, 'help a lot': 4}

data4a = data3a.replace(dict1)
data4b = data3b.replace(dict2)


# In[234]:


data5a = data4a.values.flatten()
data5b = data4b.values.flatten()

l26 = list(range(1,27))
nl26 = l26 * len(data4a)

data7a = pd.DataFrame({'question': nl26, 'response': data5a, 'cat': 'frequency'})
data7b = pd.DataFrame({'question': nl26, 'response': data5b, 'cat': 'helpfulness'})


# In[238]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", palette="muted")

fig, ax = plt.subplots(figsize = (20,5))
sns.violinplot(x='question', y='response', hue='cat', data=data8, split=True)
#sns.swarmplot(x='question', y='response', hue='cat', data=data8)

#data4a.boxplot(labels=list(map(str, list(range(26)))))


# In[113]:


# Count distinct values for each column, and concatenate all.
df_list = []
freq_list = []
help_list = []
for i2 in range(9, data.shape[1]):
    if i2 % 2 == 1:
        freq_list.append(data.groupby(data.columns[i2]).size())
    else:
        help_list.append(data.groupby(data.columns[i2]).size())

freqcount = pd.concat(freq_list, axis=1, sort=False).transpose()
helpcount = pd.concat(help_list, axis=1, sort=False).transpose()

helpcount


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 1, figsize=(20, 10))
axs[0].plot(freqcount, marker="X")
axs[1].plot(helpcount, marker="X")
#plt.xlabel("Question No.")
#plt.ylabel("Count")
axs[0].set_xlabel("Question No.")
axs[0].set_ylabel("Count (Frequency)")
axs[0].legend(freqcount, loc="upper right")
axs[1].set_xlabel("Question No.")
axs[1].set_ylabel("Count (Helpfulness)")
axs[1].legend(helpcount, loc="upper right")

plt.show()


# In[ ]:




