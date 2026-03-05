import streamlit as st

import storygenerator


st.set_page_config(page_title="TinyStories Chat", page_icon=":open_book:")
st.title("Gibberish Childrens Stories")
st.caption("🤖 Chat interface powered by roneneldan/TinyStories-1M (!)")


if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    st.subheader("Generation settings")
    max_new_tokens = st.slider("Max new tokens", min_value=20, max_value=300, value=100, step=10)
    temperature = st.slider("Temperature", min_value=0.1, max_value=1.5, value=0.8, step=0.1)
    top_p = st.slider("Top-p", min_value=0.1, max_value=1.0, value=0.95, step=0.05)
    st.divider()
    st.caption("Set your Hugging Face token in env var `HF_reader`.")


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def build_model_prompt(messages: list[dict[str, str]]) -> str:
    lines = []
    for message in messages:
        lines.append(message["content"])
    return "\n".join(lines)


def stream_text(text: str):
    for token in text.split():
        yield token + " "


if user_prompt := st.chat_input("Start or continue a story..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.chat_message("user"):
        st.markdown(user_prompt)

    model_prompt = build_model_prompt(st.session_state.messages)

    with st.chat_message("assistant"):
        with st.spinner("Writing..."):
            try:
                full_response = storygenerator.generate_tinystory(
                    model_prompt,
                    max_new_tokens=max_new_tokens,
                    temperature=temperature,
                    top_p=top_p,
                )
            except Exception as exc:
                full_response = "I could not generate a response. Check model setup and token."
                st.error(f"Generation failed: {exc}")

        response = st.write_stream(stream_text(full_response))

    st.session_state.messages.append({"role": "assistant", "content": response})
