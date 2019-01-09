#!/usr/bin/env python
# coding: utf-8

# <b><u>General Procedure</u></b>
# <br>1. Load data from a chosen file.
# <br>2. General survey of data structure.
# <br>-- <u>Useful methods:</u>
# <br>---- df.shape()
# <br>---- df.head(), df.tail(), or df.sample()
# <br>---- df.describe()
# <br>3. Look for missing values, or drop non-used columns.
# <br>-- <u>Missing values:</u>
# <br>---- Look for rows or columns which are mostly empty.
# <br>---- Delete those entire rows or columns, after making a suitable judgement.
# <br>---- The remaining missing values may have to be imputed, or discarded.
# <br>------ Will not deal with them at this point.
# <br>-- <u>Drop non-used columns:</u>
# <br>---- If done first, some problems may not even manifest.
# <br>---- However, this would require human input.

# <u>Advantage of automated data-cleaning:</u>
# <br>- If data cleaning process is robust, aberrations in raw data may be tolerated.
# <br>- Less effort/stress required in the data collection/entry process.
# <br>- Increased speed becomes possible.
# <br>- Of course, it would be nice to have a pristine database as well.
# <br>- The ideal would thus be a two-pronged (hammer-anvil) approach.

# In[1]:


# Read data from file into a DataFrame.
import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw() # Prevent pop-up window

filetype_list = (
    ("CSV files", "*.csv"), 
    ("Excel files", "*.xls"), 
    ("Excel files", "*.xlsx"), 
    ("Excel files", "*.xlsm"), 
    ("Text files (Tab-delimited)", "*.txt"), 
    ("all files", "*.*"))

file_path = filedialog.askopenfilename(initialdir = "F:/", filetypes = filetype_list)

if file_path.endswith(".xls", 0, len(file_path) - 1):
    data = pd.read_excel(file_path)
    print("File read: {0}".format(file_path))
elif file_path.endswith(".txt"):
    data = pd.read_csv(file_path, delimiter='\t')
    print("File read: {0}".format(file_path))
elif file_path.endswith(".csv"):
    data = pd.read_csv(file_path)
    print("File read: {0}".format(file_path))
elif len(file_path) == 0:
    print("No file selected.")
else:
    print("File format not supported (yet).")

del file_path


# In[2]:


print("Number of rows: {0}\nNumber of columns: {1}".format(data.shape[0], data.shape[1]))
data.sample(3)


# The data should be loaded to memory now. Yippee!
# <br>
# <br>What should we do next?
# <br>-- <u>Option 1:</u> Truncate table
# <br>---- Recommended to simplify the problem from the get-go.
# <br>---- Disadvantage: Decision making required early.
# <br>-- <u>Option 2:</u> Deal with missing values
# <br>---- Only the sub-case of removing entire rows or columns.
# <br>---- May require decision making as well.
# <br>---- *Sigh* I guess the situation really favors Option 1.
# <br>-- <u>Option 3:</u> Standardize values
# <br>---- The technical challenge here is to preserve the missing values.
# <br>---- If NaN gets converted to a string, there may be problems, or further processing may be required to reverse this.
# <br>
# <br>Let's go with Option 1.
# <br>Here's the next question:
# <br>-- Which columns should we drop?
# <br>-- Seems like we can drop columns 2 to 9.

# In[3]:


data14 = data.drop(data.columns[1:9], axis=1)
print("Number of rows: {0}\nNumber of columns: {1}".format(data14.shape[0], data14.shape[1]))
data14.sample(3)


# We now look for missing values where we can confidently drop entire rows or columns.
# <br>It would be simple if an entire row or column were NaNs, but the real world is seldom ideal.
# <br>Thus, we need criteria to decide when an entire row or column is unusable.
# <br>e.g. if most of the values in the row/column were NaNs.
# <br>"Most of the" would need a more precise definition.
# <br>
# <br>We start by looking at the subset of the table where missing values exist.

# In[4]:


row_has_na = data14.isna().any(axis=1)
col_has_na = data14.isna().any()
data14[row_has_na].loc[:, col_has_na]


# In[5]:


# What is the mode number of rows with NaN?
# This is likely the number of rows that can be safely dropped.

#print(data.isna().sum(), end='\n\n')
na_mode = data.isna().sum().mode()[0]
print("Mode: {0}".format(na_mode))
print("Most columns have {0} rows with missing values. This might be the number of unusable rows.\n".format(na_mode))
print("How many columns have {0} or more rows with missing values?".format(na_mode))

na_threshold = data.isna().sum()[data.isna().sum() >= na_mode].count()
print("{0} columns have {1} or more rows with missing values.".format(na_threshold, na_mode))
print("We will thus consider having {0} NaNs sufficient justification to discard an entire row.".format(na_threshold))
print("We will consider this relatively strict criteria to avoid discarding useful information.")
print("Let's have a look at these entries before discarding them.")


# In[6]:


data14[data14.isna().sum(axis=1) >= na_threshold]


# In[7]:


data15 = data14.drop(data14[data14.isna().sum(axis=1) >= na_threshold].index)
print("Number of rows: {0}\nNumber of columns: {1}".format(data15.shape[0], data15.shape[1]))
data15.sample(3)


# In[8]:


# Let's have a look at the NaNs left.

row_has_na_15 = data15.isna().any(axis=1)
col_has_na_15 = data15.isna().any()
data15[row_has_na_15].loc[:, col_has_na_15]


# <b>What should we do now?</b>
# <br>- Impute?
# <br>- Encode (might have to standardize first)?
# <br>- Drop rows?
# <br>- Drop columns?
# <br>
# <br>Standardization will convert NaN to 'nan'.
# <br>It will still be possible to encode 'nan' to a special value.
# <br>
# <br>Let's list all the unique values in the table.
# <br>We'll ignore the first column.

# In[9]:


set(data15.iloc[:, 1:].values.flatten())


# Text case is causing issues.
# <br>There should be 8 unique values: 4 for frequency, 4 for helpfulness.
# <br>How would anyone know there should be 8? Here's one case where human input may be required.
# <br>
# <br>What should we do?
# <br>Here are the options:
# <br>-- <u>Option 1:</u> Convert the entire table to lower (or upper) case.
# <br>---- This would be more straightforward.
# <br>---- Disadvantage:
# <br>------ NaN would be connverted to 'nan'.
# <br>------ May lose track of missing values.
# <br>------ Can include 'nan' in encoding dictionary and assign a special value.
# <br>-- <u>Option 2:</u> Create an encoding dictionary that accounts for all variations.
# <br>---- Don't really know how to approach this, yet.
# <br>---- This would be an interesting exercise.

# In[17]:


import numpy as np

def lcase(val):
    try:
        if len(val):
            return str(val).lower()
    except:
        return val

data16 = data15.apply(np.vectorize(lcase))
print("The number of NaNs is {0}.".format(data16.isna().sum().sum()))
print("Notice the 4 cases of NaNs have disappeared.")
print("Whether or not this is a good thing remains to be seen.")
print("We continue cleaning...")


# In[113]:


set(data16.iloc[:, 1:].values.flatten())


# In[215]:


data16b = data16.drop(data16.columns[0], axis=1)
data16c = data16b.replace({'help a lot': 'helps a lot'})
set(data16c.values.flatten())


# In[158]:


data16c_freq = data16c.filter(like='frequency')
data16c_help = data16c.filter(like='helpfulness')

def df_count_unique(df):
    cols = []
    for col in df.columns:
        cols.append(df[col].groupby(df[col]).count())
    return pd.concat(cols, axis=1, sort=False)

data16d_freq = df_count_unique(data16c_freq)
data16d_help = df_count_unique(data16c_help)


# In[212]:


data16d_freq.T.plot(kind='bar', figsize=(20, 5))


# In[213]:


data16d_help.T.plot(kind='bar', figsize=(20, 5))


# Much better.
# <br>-- However, 'help a lot' and 'helps a lot' are considered different.
# <br>-- Need to handle this during encoding.
# <br>-- <b>Update:</b> Might as well just handle it immediately.
# <br>-- What follows are just more fanciful plots.

# In[29]:


encode_dict = {'nan': 0, 
               'never': 1, 
               'once in a while': 2, 
               'a lot': 3, 
               'most of the time': 4, 
               'never do it': 1, 
               'does not help': 2, 
               'helps a little': 3, 
               'help a lot': 4, 
               'helps a lot': 4}

data17 = data16.replace(encode_dict)

# Split the DataFrame.
data17_id = data17.filter(like='ID')
data17_freq = data17.filter(like='frequency')
data17_help = data17.filter(like='helpfulness')
print(data17_id.shape, data17_freq.shape, data17_help.shape)


# In[82]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(20, 5))
sns.violinplot(data=data17_freq, scale='count')


# In[39]:


fig, ax = plt.subplots(figsize=(20, 5))
sns.boxenplot(data=data17_help)


# In[221]:


(data17.iloc[:, 1:].sum().sort_values(ascending=False) - 194).plot(kind='bar', figsize=(20, 5))


# <b>Transforming structure of data for plotting</b>
# <br>-- In particular, flattening.
# <br>-- Try out df.stack() and df.unstack() for pivoting.

# In[40]:


# Manual stacking.

data18_freq = data17_freq.values.flatten()
data18_help = data17_help.values.flatten()

list_26 = list(range(1,27))
nlist_26 = list_26 * len(data17)

data19_freq = pd.DataFrame({'question': nlist_26, 'response': data18_freq, 'cat': 'frequency'})
data19_help = pd.DataFrame({'question': nlist_26, 'response': data18_help, 'cat': 'helpfulness'})


# In[42]:


data20 = pd.concat([data19_freq, data19_help])


# In[52]:


sns.jointplot(data20['question'], data20['response'], kind='hex')


# In[76]:


sns.catplot(x='question', y='response', hue='cat', data=data20, kind='bar', height=6, aspect=2)


# In[85]:


sns.set(style="whitegrid", palette="muted")
fig, ax = plt.subplots(figsize = (20,5))
sns.violinplot(x='question', y='response', hue='cat', data=data20, split=True, inner='quartile')


# In[94]:


# Save as Excel file.

from datetime import datetime

dt = datetime.now().strftime('%Y%m%d_%H%M')

writer = pd.ExcelWriter('output {0}.xlsx'.format(dt))
data20.to_excel(writer,'Sheet1')
writer.save()


# # Separator
# <br>-- Everything below here is old.

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




