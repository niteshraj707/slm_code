import sys
from PIL import Image
import streamlit as st
from transformers import pipeline

model_name = 'C:\\Users\\Public\\SLM_Model\\SLM_review_model_Main'

pipe = pipeline('sentiment-analysis', model=model_name, tokenizer=model_name)

st.title('SLM Sentiment analysis')

text = st.text_area("Enter some text")
#text = 'I really hate this'
if text:
    out = pipe(text)
    st.json(out)
    # Extract the label from the first item in the list
    label = out[0]['label']
    if label == 'LABEL_0':
        image = Image.open('1.png')
        st.image(image, caption='1 Star', use_column_width=True)
    elif label == 'LABEL_1':
        image = Image.open('2.png')
        st.image(image, caption='2 Star', use_column_width=True)
    elif label == 'LABEL_2':
        image = Image.open('3.png')
        st.image(image, caption='3 Star', use_column_width=True)
    elif label == 'LABEL_3':
        image = Image.open('4.png')
        st.image(image, caption='4 Star', use_column_width=True)
    elif label == 'LABEL_4':
        image = Image.open('5.png')
        st.image(image, caption='5 Star', use_column_width=True)