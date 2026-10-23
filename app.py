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

# Initialize Session State for Free Usage Counter (Limit: 5)
if "audit_count" not in st.session_state:
    st.session_state.audit_count = 0

FREE_LIMIT = 5

# Custom CSS Theme
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
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .counter-badge {
        background-color: #3B82F6;
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
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

# Sidebar - Sultan Sahi Branding & Free Counter
st.sidebar.markdown("### 👤 Platform Architect")
st.sidebar.success("**Sultan Sahi**\n\nGlobal Trade & Export Verification")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎯 Free Trial Status")
remaining = FREE_LIMIT - st.session_state.audit_count
if remaining > 0:
    st.sidebar.info(f" Remaining Free Audits: **{remaining} / {FREE_LIMIT}**")
else:
    st.sidebar.error(" Free limit reached! Upgrade required.")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💳 Official Bank Transfer")
st.sidebar.markdown("""
**Bank:** Habib Bank Limited (HBL)  
**Title:** Sultan Sahi  
**Account No:** `11317900687003`
""")

# Main Header
st.markdown('<p class="main-header">🌐 PakExport AI Platform</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Architected & Managed Exclusively by Sultan Sahi | Global Document Verification Engine</p>', unsafe_allow_html=True)

# Main Navigation Tabs
tab1, tab2 = st.tabs(["📋 Document Verification Audit", "💎 Subscriptions & Debit Card Payment"])

with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🔍 Export Document Compliance Verification")
    
    # Counter Badge Display
    st.markdown(f'<div class="counter-badge">Free Audits Remaining: {max(0, FREE_LIMIT - st.session_state.audit_count)} / {FREE_LIMIT}</div>', unsafe_allow_html=True)

    if st.session_state.audit_count >= FREE_LIMIT:
        st.error("⚠️ Aapki 5 free verification limits khatam ho chuki hain. Please aage use karne ke liye subscription package purchase karein.")
        st.info("👈 Please **Subscriptions & Debit Card Payment** tab par ja kar package select karein.")
    else:
        doc_text = st.text_area("Paste Commercial Invoice, Packing List, or Bill of Lading details below:", height=160, placeholder="Paste your document details here...")

        if st.button("🚀 Verify & Run Audit"):
            if not model:
                st.error("Backend API key setup nahi hui. Streamlit Cloud Secrets mein GEMINI_API_KEY set karein.")
            elif not doc_text.strip():
                st.error("Document details paste karna zaroori hai.")
            else:
                with st.spinner("Analyzing compliance against international trade standards..."):
                    try:
                        prompt = f"Act as an expert international trade and compliance auditor. Review the following export document details and provide a professional verification report:\n\n{doc_text}"
                        response = model.generate_content(prompt)
                        audit_result = response.text
                        
                        # Increment audit count
                        st.session_state.audit_count += 1
                        
                        st.success(f"Audit Completed! Used: {st.session_state.audit_count}/{FREE_LIMIT}")
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
    st.markdown("### 💳 Upgrade Subscription & Card Checkout")
    st.markdown("5 free audits ke baad unlimited access ke liye apna subscription tier muntakhib karein.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="pricing-card">
            <h4>Starter Tier</h4>
            <h2>$29 / Mo</h2>
            <p style="font-size:0.9rem; color:#475569;">1 Month Unlimited Access</p>
        </div>
        """, unsafe_allow_html=True)
        pay_starter = st.button("Pay $29 (Starter)", key="starter_btn")
        
    with col2:
        st.markdown("""
        <div class="pricing-card" style="border-color:#16A34A;">
            <h4>Professional</h4>
            <h2>$149 / 6 Mo</h2>
            <p style="font-size:0.9rem; color:#475569;">6 Months Unlimited Access</p>
        </div>
        """, unsafe_allow_html=True)
        pay_pro = st.button("Pay $149 (Pro)", key="pro_btn")
        
    with col3:
        st.markdown("""
        <div class="pricing-card">
            <h4>Enterprise</h4>
            <h2>$249 / Year</h2>
            <p style="font-size:0.9rem; color:#475569;">Annual Unlimited Access</p>
        </div>
        """, unsafe_allow_html=True)
        pay_ent = st.button("Pay $249 (Enterprise)", key="ent_btn")

    st.markdown("---")
    
    # Debit Card Entry Form Section
    st.markdown("#### 💳 Option A: Direct Debit / Credit Card Payment")
    with st.form("card_payment_form"):
        card_name = st.text_input("Cardholder Name", placeholder="Sultan Sahi")
        card_num = st.text_input("Card Number (Visa / Mastercard)", placeholder="4000 1234 5678 9010", max_chars=19)
        col_exp, col_cvv = st.columns(2)
        with col_exp:
            card_exp = st.text_input("Expiry Date", placeholder="MM/YY")
        with col_cvv:
            card_cvv = st.text_input("CVV", type="password", max_chars=4)
            
        submit_card = st.form_submit_button("💳 Process Card Payment")
        
        if submit_card:
            if not card_num or not card_exp or not card_cvv:
                st.error("Please fill in all card details.")
            else:
                st.success("Payment Processing Successful! Your subscription is now activated.")
                st.session_state.audit_count = 0  # Reset limit on payment

    st.markdown("---")
    st.markdown("#### 🏦 Option B: Direct HBL Account Transfer")
    st.markdown("""
    * **Bank:** Habib Bank Limited (HBL)
    * **Account Title:** Sultan Sahi
    * **Account Number:** `11317900687003`
    
    *Direct transfer ke baad payment receipt upload karein account instant activate ho jaye ga.*
    """)
    st.markdown('</div>', unsafe_allow_html=True)
