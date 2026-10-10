import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Professional Prompt Enhancer Studio", page_icon="✨", layout="wide")

# Custom CSS for Professional Dashboard Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #4f46e5;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #4338ca;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("✨ Professional Prompt Enhancer & Layout Studio")
st.markdown("Preschool worksheets aur educational materials ke liye high-detail AI prompts tayaar karne ka professional dashboard.")

# Session State Initialization for API Key persistence
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

with st.sidebar:
    st.header("⚙️ Configuration")
    user_api_key = st.text_input("Google Gemini API Key enter karein:", type="password", value=st.session_state["api_key"])
    if user_api_key:
        st.session_state["api_key"] = user_api_key
    st.markdown("[Free Gemini API Key yahan se lein](https://aistudio.google.com/)")
    
    st.markdown("---")
    st.markdown("### 📚 Quick Worksheet Presets")
    preset_choice = st.selectbox(
        "Sample Template Select Karein:", 
        ["Apni marzi ka likhein...", "Trace and Match: Letter A", "Count and Match: Numbers", "Alphabet Formation Practice"]
    )

api_key = st.session_state["api_key"]

# Handle preset text insertion
default_text = ""
if preset_choice == "Trace and Match: Letter A":
    default_text = "Page 7 — Activity\nHeading: Trace and Match: Letter A\nInstruction: Trace the letters, then draw a line to match each letter to its picture.\nShow: Uppercase A and lowercase a with directional arrows. Match A to apple, B to ball, C to cat."
elif preset_choice == "Count and Match: Numbers":
    default_text = "Page 6 — Practice and Review\nHeading: Count and Match\nInstruction: Count the objects and match them to the correct number.\nShow: 3 rows with clear black-and-white objects (apples, pencils, stars)."
elif preset_choice == "Alphabet Formation Practice":
    default_text = "Page 4 — Tracing Worksheet\nHeading: Alphabet Formation\nInstruction: Trace the dotted letter guidelines.\nShow: 3 rows of dotted letters with starting dots and directional arrows."

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 📥 Input Rough Outline")
    user_input = st.text_area("Yahan apne rough notes ya instructions likhein:", value=default_text, height=350, placeholder="Misal ke tor par: Page 5 - Coloring book object outlines...")

with col2:
    st.markdown("### 🚀 Enhanced Professional Prompt")
    output_container = st.container()

st.markdown("---")

if st.button("Enhance Prompt Now ✨", type="primary"):
    if not api_key:
        st.error("Pehle sidebar mein Google Gemini API Key enter karein.")
    elif not user_input.strip():
        st.warning("Input box mein text likhein.")
    else:
        try:
            genai.configure(api_key=api_key)
            
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
            
            # Using the correct model name recommended by Google API
            model = genai.GenerativeModel('gemini-3.8-flash')
            
            with st.spinner("⚡ AI prompt ko professional standards ke mutabiq enhance kar raha hai..."):
                response = model.generate_content(full_prompt)
            
            with col2:
                st.success("Prompt kamyabi se enhance ho gaya!")
                st.code(response.text, language="text")
        except Exception as e:
            st.error(f"Error aa gaya: {str(e)}")
