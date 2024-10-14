import streamlit as st
import preprocessor

st.title("Upload WhatsApp Chat File")
st.markdown("Upload your **WhatsApp** chat export in `.txt` format for analysis.")

uploaded_file = st.file_uploader("Choose a file", type="txt")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    st.success("File Uploaded Successfully!")
    st.dataframe(df)
    st.session_state['df'] = df
else:
    st.warning("Please upload a WhatsApp chat file.")
