# Streamlit-Magic

Magic command is a feature in Streamlit that allows you to write almost anything (markdown, numbers, DataFrames, charts) without having to type an explicit command at all. Just put the thing you want to show on its own line of code, and it will appear in your app.

In a nutshell, the magical thing about magic commands is that there is no commands at all! Just by using variables or literal values and it is magically recognized by Streamlit and displayed in the app.

Also, magic is smart enough to ignore docstrings. That is, it ignores the strings at the top of files and functions.

If you prefer to call Streamlit commands more explicitly, you can always turn magic off in your ~/.streamlit/config.toml with the following setting:
```
[runner]
magicEnabled = false
```

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-magic/)

## Code
Here's how to use `st.write`:
```python
import streamlit as st

# 1. Display text
'Hello world'

# 2. Display a title and some text to the app:
'''
# This is the document title
This is some _markdown_.
'''

# 3. Display the dataframe
import pandas as pd
df = pd.DataFrame({'col1': [1,2,3], 'col2': [4,5,6]})
df 

# 4. Display the string 'x' and then the value of x
x = 10
'x', x

# 5. Display Matplotlib chart
import matplotlib.pyplot as plt
import numpy as np

y = np.random.normal(0, 1, size=1000)
fig, ax = plt.subplots()
ax.hist(y, bins=20)

fig
```

