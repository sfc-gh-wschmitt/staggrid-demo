import streamlit as st

import snowflake.snowpark as snowpark
st.write(snowpark.__version__)

st.write("Hello!")
st.write(st.__version__)

if st.button('clear me'):
    st.query_params.clear()

if st.button('add me'):
    st.query_params["my_key"] = True

if "my_key" in st.query_params and st.query_params["my_key"] == 'True':
    st.write("whooo hoo")



