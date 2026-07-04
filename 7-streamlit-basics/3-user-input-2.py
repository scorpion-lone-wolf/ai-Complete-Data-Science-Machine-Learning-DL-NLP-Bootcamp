import streamlit as st

# slider
st.write("This is a slider")
st.slider(
    "Select a range", min_value=0, max_value=100, value=25, step=5
)  # 25 is the default value where slider will be present
st.divider()

# =========================================================================

# number input
number = st.number_input("Enter a number", min_value=0, max_value=100, value=0)
st.write("You selected", number)
st.divider()

# =========================================================================
# text input
name = st.text_input("Enter your name", placeholder="Enter your name")
if name:
    st.write(f"Hello {name}!")
st.divider()
# =========================================================================
# text input area
message = st.text_area("Enter your message", placeholder="Enter your message")

# date picker
date = st.date_input("Select a date")
if date:
    st.write(f"You selected {date}")

st.divider()

# =========================================================================
# time picker
time = st.time_input("Select a time")
if time:
    st.write(f"You selected {time}")

st.divider()
# =========================================================================
