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

# Initialize Session State for Free Verification Limit (Max 5)
if "audit_count" not in st.session_state:
    st.session_state.audit_count = 0

FREE_LIMIT = 5

# Custom Background & CSS Theme (International Maritime/Shipping Theme)
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.88), rgba(15, 23, 42, 0.88)), 
                          url('https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .main-header {
        font-size: 2.4rem;
        color: #FFFFFF;
        font-weight: 800;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #CBD5E1;
        font-weight: 500;
        margin-bottom: 25px;
    }
    .card {
        background: rgba(255, 255, 255, 0.96);
        padding: 22px;
        border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.35);
        margin-bottom: 20px;
        color: #0F172A;
    }
    .pricing-card {
        background: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        border: 2px solid #2563EB;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 10px;
    }
    .counter-badge {
        background-color: #2563EB;
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Pre-configured Backend API Key Setup (No input box for users)
BACKEND_GEMINI_KEY = os.getenv("GEMINI_API_KEY", "YOUR_DEFAULT_API_KEY_HERE")
if BACKEND_GEMINI_KEY != "YOUR_DEFAULT_API_KEY_HERE":
    genai.configure(api_key=BACKEND_GEMINI_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
else:
    model = None

# Sidebar Setup
st.sidebar.markdown("### 👤 Platform Architect")
st.sidebar.success("**Sultan Sahi**\n\nGlobal Trade & Export Verification")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎯 Free Verification Limit")
remaining = FREE_LIMIT - st.session_state.audit_count
if remaining > 0:
    st.sidebar.info(f"Remaining Free Verifications: **{remaining} / {FREE_LIMIT}**")
else:
    st.sidebar.error(" Free Limit Reached! Please Upgrade.")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💳 Official Linked Bank")
st.sidebar.markdown("""
**Bank Name:** Habib Bank Limited (HBL)  
**Account Title:** Sultan Sahi  
**Account No:** `11317900687003`
""")

# Main Header
st.markdown('<p class="main-header">🌐 PakExport AI Platform</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Architected Exclusively by Sultan Sahi | Global Document Verification & Compliance Engine</p>', unsafe_allow_html=True)

st.markdown("---")

# Main Navigation Tabs
tab1, tab2, tab3 = st.tabs(["📋 Document Verification Audit", "💳 Subscription Tiers & Card Payment", "📞 Direct Contact"])

with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🔍 Export Document Compliance Verification")
    
    # Usage Counter Badge
    st.markdown(f'<div class="counter-badge">Free Audits Remaining: {max(0, FREE_LIMIT - st.session_state.audit_count)} / {FREE_LIMIT}</div>', unsafe_allow_html=True)

    if st.session_state.audit_count >= FREE_LIMIT:
        st.error("⚠️ Aapki 5 free verification limit poori ho chuki hain. Aage verification ke liye kripya subscription package upgrade karein.")
        st.info("👈 Please **Subscription Tiers & Card Payment** tab par ja kar package select karein.")
    else:
        doc_text = st.text_area("Paste Commercial Invoice, Packing List, or Bill of Lading details below:", height=160, placeholder="Paste your document details here...")

        if st.button("🚀 Verify & Run Audit"):
            if not model:
                st.error("Backend API key setup nahi hai. Streamlit Cloud Secrets mein GEMINI_API_KEY add karein.")
            elif not doc_text.strip():
                st.error("Please document details enter karein.")
            else:
                with st.spinner("Analyzing document compliance against international trade standards..."):
                    try:
                        prompt = f"Act as an expert international trade and compliance auditor. Review the following export document details and provide a professional verification report:\n\n{doc_text}"
                        response = model.generate_content(prompt)
                        audit_result = response.text
                        
                        # Increment Free Counter
                        st.session_state.audit_count += 1
                        
                        st.success(f"Audit Completed Successfully! ({st.session_state.audit_count}/{FREE_LIMIT} used)")
                        st.markdown("### 📊 Verification Report")
                        st.markdown(audit_result)
                        
                        # PDF Generation
                        pdf = fpdf.FPDF()
                        pdf.add_page()
                        pdf.set_font("Arial", size=12)
                        pdf.cell(200, 10, txt="PakExport AI - Official Verification Report", ln=True, align='C')
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
                        st.error(f"Error occurred: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 💎 Subscription Plans & Automated Card Payment")
    st.markdown("5 free audits ke baad unlimited document verifications ke liye apna plan choose karein.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="pricing-card">
            <h4>Starter Tier</h4>
            <h2>$29</h2>
            <p style="font-size:0.85rem; color:#475569;">1 Month Access</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="pricing-card" style="border-color:#16A34A;">
            <h4>Professional</h4>
            <h2>$149</h2>
            <p style="font-size:0.85rem; color:#475569;">6 Months Access</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="pricing-card">
            <h4>Enterprise</h4>
            <h2>$249</h2>
            <p style="font-size:0.85rem; color:#475569;">1 Year Unlimited Access</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Card Payment Checkout Form
    st.markdown("#### 💳 Automated ATM / Debit Card Payment")
    with st.form("card_checkout_form"):
        card_holder = st.text_input("Cardholder Name", placeholder="Sultan Sahi")
        card_number = st.text_input("Card Number (Visa / Mastercard)", placeholder="4000 1234 5678 9010", max_chars=19)
        col_exp, col_cvv = st.columns(2)
        with col_exp:
            expiry = st.text_input("Expiry Date", placeholder="MM/YY")
        with col_cvv:
            cvv = st.text_input("CVV Code", type="password", max_chars=4)
            
        btn_pay = st.form_submit_button("💳 Pay & Activate Subscription")
        
        if btn_pay:
            if not card_number or not expiry or not cvv:
                st.error("Please enter complete card details.")
            else:
                st.success("Payment Received Successfully! Your subscription has been activated.")
                st.session_state.audit_count = 0  # Limit reset on payment

    st.markdown("---")
    st.markdown("#### 🏦 Direct HBL Bank Account Transfer")
    st.markdown("""
    * **Bank:** Habib Bank Limited (HBL)
    * **Account Title:** Sultan Sahi
    * **Account Number:** `11317900687003`
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📞 Direct Contact & Support")
    st.markdown("""
        * **Platform Architect:** Sultan Sahi
        * **Platform:** PakExport AI — Global Document Verification Engine
        * **Official HBL Account:** `11317900687003`
    """)
    st.markdown('</div>', unsafe_allow_html=True)
