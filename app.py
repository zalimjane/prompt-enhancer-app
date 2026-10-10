import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(
    page_title="EduPrompt Studio Pro | AI Worksheet Generator",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional SaaS Dashboard Styling via Custom CSS
st.markdown("""
    <style>
    /* Main Background & Font */
    .main {
        background-color: #f4f6f9;
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Banner Styling */
    .hero-banner {
        background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .hero-banner h1 {
        color: white;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .hero-banner p {
        color: #e0e7ff;
        font-size: 1.1rem;
        margin-bottom: 0;
    }

    /* Card Containers */
    .card-container {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
    }

    /* Custom Primary Buttons */
    .stButton>button {
        width: 100%;
        background-color: #4f46e5;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.75rem;
        border: none;
        box-shadow: 0 2px 4px rgba(79, 70, 229, 0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #4338ca;
        color: white;
        box-shadow: 0 4px 8px rgba(79, 70, 229, 0.3);
    }

    /* Sidebar Customization */
    sidebar-content {
        background-color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Header Banner
st.markdown("""
    <div class="hero-banner">
        <h1>🎓 EduPrompt Studio Pro</h1>
        <p>Transform raw preschool notes into print-ready, high-detail professional AI image generation prompts instantly.</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar Configuration Dashboard
with st.sidebar:
    st.image("https://img.icons8.com/color/96/education.png", width=70)
    st.header("⚙️ Studio Control")
    
    # API Key persistence input
    api_key = st.text_input("Google Gemini API Key:", type="password", key="api_key_input", placeholder="AIzaSy...")
    st.markdown("[Get your Free Gemini API Key 🔑](https://aistudio.google.com/)")
    
    st.markdown("---")
    st.markdown("### 📚 Quick Worksheet Presets")
    preset_choice = st.selectbox(
        "Choose a Template:", 
        ["Custom Writing...", "Trace and Match: Letter A", "Count and Match: Numbers", "Alphabet Formation Practice"]
    )
    
    st.markdown("---")
    st.markdown("### 📊 Studio Stats")
    st.metric(label="Engine Status", value="Online ⚡", delta="Gemini 3.8-Flash")
    st.metric(label="Print Standards", value="Strict B&W", delta="Print-Ready")

# Handle preset text insertion logic
default_text = ""
if preset_choice == "Trace and Match: Letter A":
    default_text = "Page 7 — Activity\nHeading: Trace and Match: Letter A\nInstruction: Trace the letters, then draw a line to match each letter to its picture.\nShow: Uppercase A and lowercase a with directional arrows. Match A to apple, B to ball, C to cat."
elif preset_choice == "Count and Match: Numbers":
    default_text = "Page 6 — Practice and Review\nHeading: Count and Match\nInstruction: Count the objects and match them to the correct number.\nShow: 3 rows with clear black-and-white objects (apples, pencils, stars)."
elif preset_choice == "Alphabet Formation Practice":
    default_text = "Page 4 — Tracing Worksheet\nHeading: Alphabet Formation\nInstruction: Trace the dotted letter guidelines.\nShow: 3 rows of dotted letters with starting dots and directional arrows."

# Main Dashboard Workspace (Two Column Layout)
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 📥 Input Rough Outline")
    user_input = st.text_area(
        "Enter your raw notes or outline:", 
        value=default_text, 
        height=380, 
        placeholder="Type your outline here (e.g. Page 5 - Coloring book object outlines)..."
    )

with col2:
    st.markdown("### 🚀 Enhanced Professional Prompt")
    output_placeholder = st.empty()
    # Initial empty state box for UI polish
    output_placeholder.info("Awaiting input... Click 'Enhance Prompt Now' below to generate.")

st.markdown("---")

# Action Button & Execution Logic
if st.button("Enhance Prompt Now ✨", type="primary"):
    if not api_key:
        st.error("⚠️ Please enter your Google Gemini API Key in the sidebar configuration first.")
    elif not user_input.strip():
        st.warning("⚠️ Please provide rough outline notes in the input box.")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # Master System Prompt for Preschool Worksheets & Layouts
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
            
            # Using the required model name
            model = genai.GenerativeModel('gemini-3.8-flash')
            
            with st.spinner("⚡ AI is engineering your professional print-ready worksheet prompt..."):
                response = model.generate_content(full_prompt)
            
            with col2:
                st.success("✨ Prompt successfully enhanced!")
                st.code(response.text, language="text")
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
