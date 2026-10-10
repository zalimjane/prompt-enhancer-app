import streamlit as st
import openai

st.set_page_config(page_title="Professional Prompt Enhancer", page_icon="✨", layout="wide")

st.title("✨ Professional Prompt Enhancer App")
st.write("Apne simple notes ko high-detail professional AI prompt mein convert karein.")

with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("OpenAI API Key enter karein:", type="password")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 Input Rough Outline")
    user_input = st.text_area("Yahan apna text likhein:", height=300)

with col2:
    st.markdown("### 🚀 Enhanced Professional Prompt")

if st.button("Enhance Prompt ✨", type="primary"):
    if not api_key:
        st.error("Pehle sidebar mein OpenAI API Key enter karein.")
    elif not user_input.strip():
        st.warning("Input box mein text likhein.")
    else:
        openai.api_key = api_key
        system_prompt = """
        You are an expert AI Prompt Engineer and Layout Designer specializing in Educational Materials, Preschool Worksheets, and Graphic Design.
        YOUR TASK: Take raw notes, rough text outlines, or basic instructions provided by the user, and expand them into a complete, professional, production-ready AI image/layout prompt.
        """
        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.3
            )
            with col2:
                st.code(response.choices[0].message.content, language="text")
                st.success("Prompt enhance ho gaya!")
        except Exception as e:
            st.error(f"Error: {str(e)}")
