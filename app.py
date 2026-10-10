import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Professional Prompt Enhancer", page_icon="✨", layout="wide")

st.title("✨ Professional Prompt Enhancer App")
st.write("Apne simple notes ko high-detail professional AI prompt mein convert karein.")

with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Google Gemini API Key enter karein:", type="password")
    st.markdown("[Free Gemini API Key yahan se lein](https://aistudio.google.com/)")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 Input Rough Outline")
    user_input = st.text_area("Yahan apna text likhein:", height=300, placeholder="Misal ke tor par: Page 7 - Letter A trace and match with apple, ball, cat...")

with col2:
    st.markdown("### 🚀 Enhanced Professional Prompt")
    output_placeholder = st.empty()

if st.button("Enhance Prompt ✨", type="primary"):
    if not api_key:
        st.error("Pehle sidebar mein Google Gemini API Key enter karein.")
    elif not user_input.strip():
        st.warning("Input box mein text likhein.")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # Master System Prompt based on Preschool Standards
            system_prompt = """
            You are an expert AI Prompt Engineer and Educational Materials Designer specializing in preschool workbooks, worksheets, tracing letters, and children's activity books.
            
            YOUR TASK: Take raw notes, rough text outlines, or basic instructions provided by the user, and transform them into a complete, professional, production-ready AI image generation prompt.
            
            STRICT RULES & FORMATTING TO FOLLOW IN THE GENERATED PROMPT:
            1. Layout Architecture: Ensure clear hierarchical sections (Header with title and instructions, Upper tracing section with dot guidelines/directional arrows, Lower matching/activity columns with generous whitespace).
            2. Typography & Text: Specify clean, large, bold, rounded sans-serif fonts with correct spelling, proper alignment, and no extra/malformed letters.
            3. Style & Aesthetics: Clean preschool workbook design with crisp black outlines, rounded forms, consistent stroke weight, and simple cheerful illustrations. Strict black and white for economical home/classroom printing (no gray shading, no color fills, no gradients, no watermarks, no logos).
            4. Negative Constraints: Explicitly rule out illegible text, crowded spacing, overlapping elements, colored fills, gray shadows, and decorative clutter.
            
            Expand the user's rough notes into a detailed, structured prompt maintaining these precise professional standards.
            """
            
            full_prompt = f"{system_prompt}\n\nUser Input:\n{user_input}"
            
            # Set to gemini-3.8-flash as required
            model = genai.GenerativeModel('gemini-3.8-flash')
            
            with st.spinner("AI aapke prompt ko preschool standards ke mutabiq enhance kar raha hai... Please wait ✨"):
                response = model.generate_content(full_prompt)
            
            with col2:
                st.code(response.text, language="text")
                st.success("Prompt kamyabi se enhance ho gaya!")
        except Exception as e:
            st.error(f"Error aa gaya: {str(e)}")
