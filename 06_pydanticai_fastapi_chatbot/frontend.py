import streamlit as st
import httpx

# save message_history into session state
# want to save messages into session state


def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "message_history" not in st.session_state:
        st.session_state.message_history = []


# so that we can loop through them and display them in the frontend
# display bot answer


def display_chat_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# send in users question to API
def handle_user_input():
    # := is the walrus operator <->
    # prompt = st.chat_input("Talk to JokeBot")
    # if prompt:
    if prompt := st.chat_input("Talk to JokeBot"):
        # user prompt save to session state
        st.session_state.messages.append({"role": "user", "content": prompt})

        chat_response = httpx.post(
            "http://localhost:8000/chat",
            json={
                "question": prompt,
                "message_history": st.session_state.message_history,
            },
        )

        st.session_state.message_history = chat_response.json().get("message_history")

        bot_response = chat_response.json().get("response")

        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown(bot_response)

        st.session_state.messages.append({"role": "assistant", "content": bot_response})

def layout():
    st.markdown("# Chat with Ro Båt")
    st.markdown(
        "RO BÅT is a funny robot that can help you out with programming tasks. However he doesn't directly answer your question, usually he asks another question back."
    )
    display_chat_messages()
    handle_user_input()

    # st.write(st.session_state)


if __name__ == "__main__":
    init_session_state()
    layout()
