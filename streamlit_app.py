import streamlit as st

# Display text
'Hello world'

# Display a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3], 'col2': [4,5,6]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Display the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

y = np.random.normal(0, 1, size=1000)
fig, ax = plt.subplots()
ax.hist(y, bins=20)

fig  # 👈 Display a Matplotlib chart
