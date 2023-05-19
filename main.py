import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1 ,col2=st.columns(2)

with col1:
    st.image("image/photo.png",width=500)


with col2:
    st.title("vanakam")

    content="""
    sincerely smitten, lies in hiding this fact from the woman you love,
     of feigning a casual detachment under all circumstances. What sadness 
     there is in this simple observation! What an accusation I am quite 
     serious. Look at those kids. The boys want to get the girls into bed
      so they can have their corks popped off their bottles and forth. 
      When a man blows his nose you don’t call it love. Why get all 
      misty-eyed when a man blows another part of his anatomy? As for 
      the girls, they’re either going along for the ride because they 
      can get the things they want from the boys, or else maybe they enjoy
       being in bed too. Thought I doubt it. I never knew an eighteen-year-old 
       boy who didn’t drop the egg off his spoon at the first fence."""

    st.info(content)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("image/" + row['image'])
        st.write(f"[source code]({row['url']})")



with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("image/" + row['image'])
        st.write(f"[source code]({row['url']})")

