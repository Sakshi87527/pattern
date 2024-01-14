#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(1,4+1,1):
    for k in range(1,(3-1)+1,1):
        print("", end='')
    for j in range(1,i+1):
        print("*",end='')
    print()


# In[2]:


for i in range(1,6,1):
    for j in range(1,i+1,1):
        print("*", end=' ')
    print("\n")


# In[5]:


for i in range(5,0,-1):
    
    for j in range(1,i+1,1):
        print("*", end=' ')
    print("\n")


# In[6]:


for i in range(1,5,1):
    for k in range(1,5-i,1):
        print(" ",end=' ')
    for j in range(1,i+1,1):
        print("*",end=' ')
    print("\n")


# In[7]:


for i in range(4,0,-1):
    for k in range(1,5-i,1):
        print(" ",end=' ')
    for j in range(1,i+1,1):
        print("*",end=' ')
    print("\n")


# In[ ]:




