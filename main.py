#Import necessary libraries
import streamlit as st
from langchain import PromptTemplate
from langchain import LLMChain
import os

# Set up API key for Google(Using Google Models-Gemini Pro)

os.environ['GOOGLE_API_KEY']  = "AIzaSyBnIwWYuPOuizPW-q8PMoDrcVJv8vYUs2I"
from langchain_google_genai import ChatGoogleGenerativeAI
gemini_model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-exp")

#Create prompt template for generating tweets
tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate(input_variables=["number", "topic"], template=tweet_template)
tweet_chain = tweet_prompt | gemini_model


st.header("Tweet Generator - Aniket")

st.subheader("Generate tweets using Generative AI")

topic = st.text_input("Topic")

number = st.number_input("Number of tweets", min_value=1, max_value=10, value = 1, step = 1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(tweets.content)
