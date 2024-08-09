import streamlit as st
from llm import gen_shopName_Products

st.title("Sports Shop Name Generator")
sport = st.sidebar.selectbox("Pick a Sport",("Cricket","Rugby","Football"))

    
if sport:
    response = gen_shopName_Products(sport)
    st.header(response['name'].strip())
    menu_items = response['products'].strip().split(',')
    st.write("Menu Items")
    for item in menu_items:
        st.write('-', item)

if __name__ == "__main__":
    print(gen_shopName_Products('Rugby'))         