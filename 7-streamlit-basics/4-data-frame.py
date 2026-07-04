import streamlit as st
import pandas as pd

# adding some data in the form of dictionaries to dataframe
df = pd.DataFrame(
    {
        "First Column": [1, 2, 3, 4, 5],
        "Second Column": [1, 4, 9, 16, 25],
    }
)

st.dataframe(df)

# Editable dataframe
# ==========================================================================
# here you can edit the dataframe in the ui
editable_df = st.data_editor(df, num_rows="dynamic")
st.write("Updated Dataframe")
if editable_df is not None:
    st.dataframe(editable_df)
