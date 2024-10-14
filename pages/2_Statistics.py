import streamlit as st
import helper

st.title("Chat Statistics")

if 'df' in st.session_state:
    df = st.session_state['df']

    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.selectbox("Show Analysis for", user_list)

    if st.button("Show Statistics"):
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

        st.subheader(f"Statistics for {selected_user}")
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Messages", num_messages)
        col2.metric("Total Words", words)
        col3.metric("Media Shared", num_media_messages)
        col4.metric("Links Shared", num_links)
else:
    st.error("Please upload the chat data on the Home page first.")
