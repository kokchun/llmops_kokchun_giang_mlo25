import streamlit as st


# save message_history into session state
# want to save messages into session state

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []


# so that we can loop through them and display them in the frontend
# send in users question to API
# display bot answer

def layout():
    st.markdown("# Chat with Ro Båt")
    st.markdown(
        "RO BÅT is a funny robot that can help you out with programming tasks. However he doesn't directly answer your question, usually he asks another question back."
    )
    st.write(st.session_state)


if __name__ == "__main__":
    layout()
