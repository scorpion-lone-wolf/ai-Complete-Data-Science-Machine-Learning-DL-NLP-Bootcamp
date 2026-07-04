import streamlit as st

# bold type text
st.title("title: This is a title")
st.header("header: This is a header")
st.subheader("subheader:This is a subheader")

# writing text file
st.text("This is a plain text `special` ")
st.write(
    "This is a plain text `special` _italic_  **bold**  [Google LInk](https://www.google.com)"
)  # this can output special character like bold, italic etc

st.divider()
# markdown
st.markdown("### Some code example")

# example of writing code
st.code(
    """
# python example
print("This is a basic python streamlit example course")
def hello():
    print("Hello ,World!")
print(hello())
""",
    language="python",
)
# Some message that we can send to user
st.success("This is a success message")
st.error("This is an error message")
st.warning("This is a warning message")
