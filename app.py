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

# Background & Custom CSS (Port / Sea Shipment Theme)
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.85)), 
                          url('https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .main-header {
        font-size: 2.5rem;
        color: #FFFFFF;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .sub-header {
        font-size: 1.2rem;
        color: #E2E8F0;
        font-weight: 500;
        margin-bottom: 20px;
    }
    .card {
        background: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 20px;
        color: #1E293B;
    }
    .pricing-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #3B82F6;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Pre-configured Backend API Key Setup
BACKEND_GEMINI_KEY = os.getenv("GEMINI_API_KEY", "YOUR_DEFAULT_API_KEY_HERE")
if BACKEND_GEMINI_KEY != "YOUR_DEFAULT_API_KEY_HERE":
    genai.configure(api_key=BACKEND_GEMINI_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
else:
    model = None

# Sidebar - Subscription & HBL Payment Integration
st.sidebar.markdown("### 💎 Subscription Tiers")

st.sidebar.markdown("""
<div style="background:#f8fafc; padding:10px; border-radius:8px; color:#1e293b; margin-bottom:10px;">
    <b>1. Starter Tier</b><br>📅 Monthly Access<br>💵 <b>$29 / month</b>
</div>
<div style="background:#f8fafc; padding:10px; border-radius:8px; color:#1e293b; margin-bottom:10px;">
    <b>2. Professional Tier</b><br>📅 6 Months Access<br>💵 <b>$149 / 6 months</b>
</div>
<div style="background:#f8fafc; padding:10px; border-radius:8px; color:#1e293b; margin-bottom:10px;">
    <b>3. Enterprise Global Tier</b><br>📅 Annual Unlimited<br>💵 <b>$249 / year</b>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💳 Linked HBL Account")
st.sidebar.info(
    "**Bank Name:** Habib Bank Limited (HBL)\n\n"
    "**Account Title:** Sultan Sahi\n\n"
    "**Account No:** `11317900687003`"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👤 Platform Architect")
st.sidebar.success("**Sultan Sahi**\n\nGlobal Trade & Logistics Portal")

# Main Header Section
st.markdown('<p class="main-header">🌐 PakExport AI Portal</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Architected & Managed by Sultan Sahi | International Trade & Shipment Verification Engine</p>', unsafe_allow_html=True)

st.markdown("---")

# Tabs for Navigation
tab1, tab2, tab3 = st.tabs(["📋 Document Audit", "💳 Subscription & HBL Linking", "📞 Direct Contact"])

with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🔍 Instant Export Document Compliance Audit")
    st.markdown("Paste your Commercial Invoice, Packing List, or Bill of Lading details below for instant AI review.")
    
    doc_text = st.text_area("Document Details:", height=150, placeholder="Paste your invoice details here...")

    if st.button("🚀 Run Instant Audit"):
        if not model:
            st.error("System backend API key is not configured. Please set up the default API key in environment variables.")
        elif not doc_text.strip():
            st.error("Please paste your export document details.")
        else:
            with st.spinner("Analyzing document compliance against global export standards..."):
                try:
                    prompt = f"Act as an expert international trade and customs compliance auditor. Review the following export document details and provide a professional audit report:\n\n{doc_text}"
                    response = model.generate_content(prompt)
                    audit_result = response.text
                    
                    st.success("Audit Completed Successfully!")
                    st.markdown("### 📊 Audit Report")
                    st.markdown(audit_result)
                    
                    # PDF Generation
                    pdf = fpdf.FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size=12)
                    pdf.cell(200, 10, txt="PakExport AI - Official Trade Audit Report", ln=True, align='C')
                    pdf.cell(200, 10, txt="Architected by Sultan Sahi", ln=True, align='C')
                    pdf.ln(10)
                    
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
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 💳 Subscription Tiers & Direct HBL Bank Integration")
    st.markdown("Select any subscription tier below and complete your payment directly to our official corporate Habib Bank Limited (HBL) account.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="pricing-card">
            <h4>Starter Tier</h4>
            <h2>$29</h2>
            <p>1 Month Access</p>
            <hr>
            <p style="font-size:0.85rem;">Quick audits & basic compliance reports.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="pricing-card" style="border-color: #2563EB;">
            <h4>Professional</h4>
            <h2>$149</h2>
            <p>6 Months Access</p>
            <hr>
            <p style="font-size:0.85rem;">Extended access for regular exporters.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="pricing-card">
            <h4>Enterprise</h4>
            <h2>$249</h2>
            <p>1 Year Unlimited</p>
            <hr>
            <p style="font-size:0.85rem;">Full platform access & priority support.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 🏦 Linked HBL Payment Account Details:")
    st.markdown("""
    * **Bank Name:** Habib Bank Limited (HBL)
    * **Account Title:** Sultan Sahi
    * **Account Number:** `11317900687003`
    
    *After transferring the payment, please share your receipt via direct email or official channels to activate your chosen subscription tier.*
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📞 Direct Contact & Support")
    st.markdown("""
        * **Platform Owner & Architect:** Sultan Sahi
        * **Services:** Global Export Compliance, Trade Audits, & Logistics Portal
        * **Official HBL Account:** `11317900687003`
    """)
    st.markdown('</div>', unsafe_allow_html=True)
