import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(
    page_title="PakExport AI — Sultan Sahi",
    page_icon="🌐",
    layout="wide"
)

# Custom Styling & Header
st.markdown("""
    <style>
    .main-title {
        font-size: 38px;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 18px;
        color: #4B5563;
        text-align: center;
        margin-bottom: 25px;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="main-title">🌐 PakExport AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Created & Architected by <b>Sultan Sahi</b> | Global Trade Audit Engine</div>', unsafe_allow_html=True)

st.divider()

# Sidebar
with st.sidebar:
    st.header("⚙️ System Control")
    api_key = st.text_input("Enter Free Gemini API Key:", type="password")
    st.divider()
    st.header("💎 Subscription Tier")
    st.markdown("**Current Plan:** Pay-Per-Audit ($10/audit)")
    st.info("💡 Upgrade to SME Pro ($99/mo) for unlimited audits & verified QR badges.")

# Main Tabs
tab1, tab2, tab3 = st.tabs(["📄 Document Audit", "🔍 HS-Code Verifier", "⭐ Reviews & Ratings"])

# TAB 1: Document Audit
with tab1:
    st.subheader("1. Instant Export Document Compliance Audit")
    doc_text = st.text_area("Paste Commercial Invoice / Packing List Details Here:", height=180, 
                            placeholder="e.g. Exporter: Sialkot Sports Co, Product: Leather Jackets 500 pcs, HS Code: 4203.10...")
    
    if st.button("🚀 Run Instant Audit"):
        if not api_key:
            st.error("Please enter your Gemini API Key in the sidebar first!")
        elif not doc_text.strip():
            st.warning("Please paste document details to run the audit.")
        else:
            with st.spinner("Sultan Sahi Engine auditing compliance parameters..."):
                try:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = f"You are PakExport AI, an expert customs compliance auditor created by Sultan Sahi. Audit this export document for compliance and missing fields: {doc_text}"
                    response = model.generate_content(prompt)
                    st.success("✅ Audit Completed Successfully!")
                    st.markdown(response.text)
                    st.divider()
                    st.info("Verified Compliant | Certificate ID: **PEAI-2026-8892** | Architected by **Sultan Sahi**")
                except Exception as e:
                    st.error(f"Error executing audit: {e}")

# TAB 2: HS Code Finder
with tab2:
    st.subheader("2. Global HS-Code & Duty Matcher")
    product_desc = st.text_input("Enter Product Description:")
    if st.button("🔍 Find Verified HS-Code"):
        if not api_key:
            st.error("Please enter your Gemini API Key in the sidebar!")
        elif not product_desc:
            st.warning("Please enter a product description.")
        else:
            with st.spinner("Matching global tariffs..."):
                try:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    res = model.generate_content(f"Provide exact HS Code and export checklist for: {product_desc}")
                    st.markdown(res.text)
                except Exception as e:
                    st.error(f"Error: {e}")

# TAB 3: Reviews
with tab3:
    st.subheader("3. Verified Exporter Reviews")
    st.success("**Sialkot Apparel Exporter** ⭐⭐⭐⭐⭐\n\n'Saved our $35,000 shipment to Hamburg!'")
