# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

from st_aggrid import AgGrid
import pandas as pd


# Write directly to the app
st.title(f"st-aggrid Demo in SiS :balloon:")

df = pd.read_csv('./airline-safety.csv')
AgGrid(df)