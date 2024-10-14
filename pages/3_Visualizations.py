import streamlit as st
import matplotlib.pyplot as plt
import helper
import plotly.express as px

st.title("Visualize Chat Data")

if 'df' in st.session_state:
    df = st.session_state['df']
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.selectbox("Visualize for", user_list)

    st.subheader(f"Visualizations for {selected_user}")

    st.write("---")
    # Wordcloud
    st.write("### Wordcloud")
    df_wc = helper.create_wordcloud(selected_user, df)
    fig, ax = plt.subplots()
    ax.imshow(df_wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)

    st.write("---")
    # Emoji Analysis
    st.write("### Emoji Analysis")
    emoji_df = helper.emoji_helper(selected_user, df)
    fig2 = px.pie(emoji_df.head(), values=1, names=0, title="Top Emojis Used")
    st.plotly_chart(fig2)

