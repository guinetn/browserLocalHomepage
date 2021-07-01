# streamlit

Open-source app framework built specifically for Machine Learning and Data Science projects.

Streamlit makes it easy for you to visualize, mutate, share data: deploy, record screencast
create beautiful data web applications using Streamlit

>pip install streamlit
>streamlit hello                 <------- demos
>streamlit run first_app.py

https://streamlit.io/
https://docs.streamlit.io/en/stable/api.html
https://docs.streamlit.io/en/stable/api.html#display-text

a Python library used to build fast web applications without having any knowledge about frontend languages/frameworks. 
Project was developed to help Data Science practitioners easily showcase their data science projects.

All Streamlit applications can be run using the native CLI. 
>streamlit run app.py

Streamlit library has a bunch of inbuilt methods that can display text, parse markup language styles and build UI widgets. Thus, it enables the seamless creation of layouts for your web application.

widgets on Streamlit:
st.radio 
st.button
st.checkbox
st.slider
st.selectbox

st.title('My first app')



Uploading Images


Display DataFrames
st.write(pandas_df) 
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


Display Graphs
st.plotly_chart
st.pyplot
st.altair_chart
st.vega_lite_chart
st.bokeh_chart


first_app.py
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

>streamlit run first_app.py
>streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py


## more

- [Streamlit app in 1 min](https://www.youtube.com/watch?v=iPj6QKMd8qA)

streamlit run streamlit-helloworld-in-1-minute.py

```
import streamlit as st

st.write("""
# Hello world!
This is my **first** *app*!
""")
```