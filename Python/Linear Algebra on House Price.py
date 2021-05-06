#!/usr/bin/env python
# coding: utf-8

# In[25]:


'''
Vectorized Code on the Total Price of a house 
Find out the total price
Total Price = $10,190 (upfont paymnent) + $223 per square feet * house size (square feet)
'''
import numpy as np
HouseSize = np.array([[1,693],[1,656],[1,1060],[1,487],[1,1275]])
HousePrice = np.array([[10190],[223]])
print(HouseSize)
print('')
print(HousePrice)
print('')
print(np.matmul(HouseSize , HousePrice))
print('')
Sum = np.sum( HouseSize @ HousePrice )
print("Total price for the 5 houses are " + str(Sum))


# In[ ]:




