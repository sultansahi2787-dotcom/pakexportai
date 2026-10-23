import streamlit as st
from google import generativeai as genai
import fpdf
import tempfile
import os

# Page Configuration
st.set_page_config(
    page_title="PakExport AI — Sultan Sahi",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling & Professional UI
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        font-weight: 500;
        margin-bottom: 20px;
    }
    .badge {
        background-color: #EFF6FF;
        color: #1D4ED8;
        padding: 6px 12px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.9rem;
        border: 1px solid #BFDBFE;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar - System Control & Configuration
st.sidebar.markdown("### ⚙️ System Control")
api_key_input = st.sidebar.text_input("Enter Free Gemini API Key:", type="password")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏢 Enterprise Credentials")
st.sidebar.info("**Platform Creator:** Sultan Sahi\n\n**SCCI Membership:** A-96532\n\n**Location:** Sialkot, Pakistan")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💎 Subscription Tier")
st.sidebar.success("**Current Plan:** Global SME Pro (Active)\n\n*Unlimited Audits & Verified QR Badges*")

# Main Header Section
st.markdown('<p class="main-header">🌐 PakExport AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Created & Architected by Sultan Sahi | Global Trade Audit Engine</p>', unsafe_allow_html=True)
st.markdown('<span class="badge">Sialkot Chamber of Commerce & Industry (SCCI) Verified Exporter Hub</span>', unsafe_allow_html=True)

st.markdown("---")

# Tabs for Navigation
tab1, tab2, tab3 = st.tabs(["📋 Document Audit", "🔍 HS Code Verifier", "📞 Direct B2B Inquiry"])

# Initialize Gemini API if key is provided
if api_key_input:
    genai.configure(api_key=api_key_input)
    model = genai.GenerativeModel('gemini-2.5-flash')
else:
    model = None

with tab1:
    st.markdown("### 1. Instant Export Document Compliance Audit")
    st.markdown("Paste your Commercial Invoice or Packing List details below for automated compliance review.")
    
    doc_text = st.text_area("Document Details (Exporter, Buyer, Products, Quantities, HS Codes, Prices):", height=150, placeholder="e.g. Exporter: Sahi Royal Company, Sialkot. Product: Cotton Tracksuits 500 pcs, Destination: USA...")

    if st.button("🚀 Run Instant Audit"):
        if not api_key_input:
            st.error("Please enter your Gemini API Key in the sidebar first!")
        elif not doc_text.strip():
            st.error("Please paste your export document details.")
        else:
            with st.spinner("Analyzing document compliance against international trade standards..."):
                try:
                    prompt = f"Act as an expert international trade and customs compliance auditor. Review the following export document details and provide a professional audit report covering compliance, potential risks, and recommendations:\n\n{doc_text}"
                    response = model.generate_content(prompt)
                    audit_result = response.text
                    
                    st.success("Audit Completed Successfully!")
                    st.markdown("### 📊 Audit Report")
                    st.markdown(audit_result)
                    
                    # PDF Generation Function
                    pdf = fpdf.FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size=12)
                    pdf.cell(200, 10, txt="PakExport AI - Official Trade Audit Report", ln=True, align='C')
                    pdf.cell(200, 10, txt="Architected by Sultan Sahi (SCCI Reg: A-96532)", ln=True, align='C')
                    pdf.ln(10)
                    
                    # Clean text for PDF encoding
                    clean_text = audit_result.encode('latin-1', 'replace').decode('latin-1')
                    pdf.multi_cell(0, 10, txt=clean_text)
                    
                    temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
                    pdf.output(temp_pdf.name)
                    
                    with open(temp_pdf.name, "rb") as f:
                        st.download_button(
                            label="📥 Download Official Audit Report (PDF)",
                            data=f,
                            file_name="PakExport_Audit_Report.pdf",
                            mime="application/pdf"
                        )
                except Exception as e:
                    st.error(f"An error occurred: {e}")

with tab2:
    st.markdown("### 2. HS Code & Tariff Verifier")
    st.markdown("Verify product classifications for sportswear, apparel, and leather goods.")
    hs_query = st.text_input("Enter product description (e.g., Leather jackets, cotton hoodies, footballs):")
    if st.button("🔍 Verify HS Code"):
        if not api_key_input:
            st.error("Please enter your Gemini API Key in the sidebar.")
        elif not hs_query.strip():
            st.error("Please enter a product description.")
        else:
            with st.spinner("Searching global trade tariffs..."):
                try:
                    prompt = f"Provide standard international HS Codes and customs guidelines for the following product manufactured in Sialkot, Pakistan: {hs_query}"
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

with tab3:
    st.markdown("### 📞 Connect with Sahi Royal Company")
    st.markdown("Ready to place bulk orders or request custom samples (Low MOQs 20-50 pcs)?")
    st.markdown("""
        * **Owner & CEO:** Sultan Sahi
        * **Business:** Sahi Royal Company (Sportswear, Apparel & Leather Goods Manufacturer)
        * **SCCI Membership:** 9026527 / A-96532
        * **Direct WhatsApp Support:** [Click here to chat on WhatsApp Business](https://wa.me/)
    """)
