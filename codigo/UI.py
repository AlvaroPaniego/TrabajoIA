import streamlit as st
import modelo_api as ma
st.set_page_config(page_title="Chat + Input UI", layout="wide")
st.markdown("""
<style>
.stChatMessageContent {
    color: black !important;
}

.stMarkdown p, .stMarkdown span, .stMarkdown {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Initialize session state
# ---------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "chat_input" not in st.session_state:
    st.session_state.chat_input = ""

if "chat_buffer" not in st.session_state:
    st.session_state.chat_buffer = ""

# ---------------------------------
# Callback to store message safely
# ---------------------------------
def store_and_clear_input():
    st.session_state.chat_buffer = st.session_state.chat_input
    st.session_state.chat_input = ""


# ---------------------------------
# Page Layout
# ---------------------------------
st.title("✨ AsistoMail")

col1, col2 = st.columns(2)

# ===========================================================
# LEFT SIDE — CHATBOT (now using correct Streamlit components)
# ===========================================================
with col1:
    st.subheader("🤖 Chatbot")

    # Chat Log
    chat_box = st.container(height=450, border=True)

    with chat_box:
        for role, message in st.session_state.chat_history:
            with st.chat_message("user" if role == "user" else "assistant"):
                st.write(message)

    # Input box
    st.text_input(
        "💬 Type a message:",
        key="chat_input",
        on_change=store_and_clear_input,
    )

    # Process new message
    if st.session_state.chat_buffer:
        msg = st.session_state.chat_buffer
        st.session_state.chat_history.append(("user", msg))

        # Bot reply
        bot_reply = f"Bot: {ma.chat_with_memory(msg)}"
        st.session_state.chat_history.append(("assistant", bot_reply))

        st.session_state.chat_buffer = ""     # Clear buffer
        st.rerun()


# ===========================================================
# RIGHT SIDE — TEXT AREA + FILE UPLOAD
# ===========================================================
with col2:
    st.subheader("📝 Text & File Input")

    # Dropdown menu
    tone = st.selectbox(
        "Seleccione el tono:",
        ["neutral", "brusco", "educado", "profesional"]
    )

    # File upload
    uploaded_file = st.file_uploader("Upload a file")
    # Action button
    if st.button("Aplicar tono"):
        st.success(f"Tono seleccionado: {tone}")
        #st.success(obtener_correo_usuario(uploaded_file.name))

    # Text area
    text_area_value = st.text_area("Enter your text:")  

    if uploaded_file:
        st.success(f"Uploaded: {uploaded_file.name}")
        file_name = uploaded_file.name
