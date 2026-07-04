import streamlit as st

# some button and taking user input interactive way
if st.button("ClickMe"):
    st.write("Button Clicked")

st.divider()
# =========================================================================
# Radio button
choice = st.radio("Select an Option", ["Option1", "Option2", "Option3"], disabled=False)
if choice == "Option1":
    st.write("You selected Option1")
elif choice == "Option2":
    st.write("You selected Option2")
else:
    st.write("You selected Option3")

st.divider()
# =========================================================================
# Checkbox
if st.checkbox("Do you agree?"):
    st.write("You agreed")
st.divider()
# =========================================================================
# Selectbox and dropdown with options
st.selectbox("Select an Genre", ["Horror", "Comedy", "Drama"])

st.divider()
# =========================================================================
# multiple select and dropdown with options
st.multiselect("Select an Multiple Genre", ["Horror", "Comedy", "Drama"])
st.divider()
# =========================================================================
