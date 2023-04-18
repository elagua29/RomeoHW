import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud, STOPWORDS
import glob, nltk, os, re
from nltk.corpus import stopwords
import nltk as nltk
nltk.download('stopwords')

st.markdown('''
# Analyzing Shakespeare Texts
''')

# Sidebar
st.sidebar.header('Word Cloud Settings')
max_word = st.sidebar.slider("Max Words",min_value=10, max_value=200, value=100, step=10)
size_word = st.sidebar.slider("Size of Largest Word",min_value=50, max_value=350, value=60, step=10)
image_width = st.sidebar.slider("Image Width",min_value=100, max_value=800, value=400, step=10)
random_state = st.sidebar.slider("Random State",min_value=20, max_value=100, value=20, step=10)

remove_stop_words = st.sidebar.checkbox("Remove Stop Words?",value=True)

st.sidebar.header("Word Count Settings")
min_word = st.sidebar.slider("Minimum count of words",min_value=5, max_value=100, value=40, step=10)

# Create a dictionary (not a list)
books = {" ":" ","A Mid Summer Night's Dream":"data/summer.txt","The Merchant of Venice":"data/merchant.txt","Romeo and Juliet":"data/romeo.txt"}
import nltk
nltk.download('punkt')

## Select text files
image = st.selectbox("Choose a text file", books.keys())

## Get the value
image = books.get(image)

if image != " ":
    stopwords = set(STOPWORDS)
    raw_text = open(image,"r").read().lower()
    nltk_stop_words = stopwords.words('english')

    if remove_stop_words:
        stop_words = set(nltk_stop_words)
        stop_words.update(['us', 'one', 'though','will', 'said', 'now', 'well', 'man', 'may',
        'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
        'put', 'seem', 'asked', 'made', 'half', 'much',
        'certainly', 'might', 'came','thou'])
        # These are all lowercase

    tokens = nltk.word_tokenize(raw_text)


# tokenize dataset

tab1, tab2, tab3 = st.tabs(['Word Cloud', 'Bar Chart', 'View Text'])

with tab1:
    
if image != " ":
    stopwords = set(STOPWORDS)
    raw_text = open(image,"r").read().lower()
    nltk_stop_words = stopwords.words('english')

    if remove_stop_words:
        stop_words = set(nltk_stop_words)
        stop_words.update(['us', 'one', 'though','will', 'said', 'now', 'well', 'man', 'may',
        'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
        'put', 'seem', 'asked', 'made', 'half', 'much',
        'certainly', 'might', 'came','thou'])
           

with tab2:
    st.write('This is my second tab')

with tab3:
    if image != " ":
        raw_text = open(image,"r").read().lower()
        st.write(raw_text)







