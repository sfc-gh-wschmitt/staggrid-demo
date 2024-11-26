# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

from st_aggrid import AgGrid
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import pandas as pd



# Write directly to the app
st.title(f"st-aggrid Demo in SiS :balloon:")

df = pd.read_csv('./airline-safety.csv')

# Configure AgGrid
builder = GridOptionsBuilder.from_dataframe(df)
builder.configure_default_column(editable=True)  # Make all columns editable
builder.configure_pagination(paginationAutoPageSize=True)  # Enable pagination
builder.configure_side_bar()  # Add filter and sort sidebar
builder.configure_selection(selection_mode="multiple", use_checkbox=True)  # Enable multi-row selection

grid_options = builder.build()

# Create an editable data grid
response = AgGrid(
    df,
    gridOptions=grid_options,
    editable=True,
    update_mode=GridUpdateMode.VALUE_CHANGED,
    theme="streamlit",  # Available themes: 'streamlit', 'alpine', 'material'
)

# Reflect changes made in the grid
updated_df = pd.DataFrame(response["data"])
selected_rows = response["selected_rows"]

# Display updated DataFrame
st.write("### Updated DataFrame")
st.dataframe(updated_df)


# Display selected rows
st.write("### Selected Rows")
if not selected_rows.empty:  # Check if there are any selected rows
    selected_rows_df = pd.DataFrame(selected_rows)  # Convert to DataFrame
    st.dataframe(selected_rows_df)
else:
    st.info("No rows selected.")