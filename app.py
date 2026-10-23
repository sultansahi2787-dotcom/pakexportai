import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="PakExport AI - B2B Trade & Export Portal",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS & HTML Dashboard Embedded inside Python
st.markdown("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PakExport AI - B2B Trade & Export Portal</title>
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            psw: {
              navy: '#002B49',
              slate: '#0F172A',
              accent: '#00A86B',
              gold: '#D4AF37',
              lightBg: '#F8FAFC',
              card: '#FFFFFF'
            }
          }
        }
      }
    }
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <!-- html2pdf.js for Client-Side Export PDF Generation -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>

  <!-- Inter Font -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap">

  <style>
    body {
      font-family: 'Inter', sans-serif;
      background-color: #F8FAFC;
    }
    .hero-bg {
      background: linear-gradient(135deg, rgba(0, 43, 73, 0.94) 0%, rgba(15, 23, 42, 0.96) 100%),
                  url('https://images.unsplash.com/photo-1578575437130-527eed3abbec?auto=format&fit=crop&w=1920&q=80');
      background-size: cover;
      background-position: center;
    }
    .glass-card {
      background: rgba(255, 255, 255, 0.07);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .card-chip {
      background: linear-gradient(135deg, #FFE082 0%, #FFB300 100%);
    }
  </style>
</head>
<body class="text-slate-800 antialiased min-h-screen flex flex-col justify-between">

  <!-- TOP OFFICIAL GOVT / TRADE STATUS BAR -->
  <div class="bg-psw-navy border-b border-slate-700 text-slate-300 text-xs py-2 px-4 sm:px-8">
    <div class="max-w-7xl mx-auto flex flex-wrap justify-between items-center gap-2">
      <div class="flex items-center space-x-4">
        <span class="flex items-center text-emerald-400 font-medium">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse mr-1.5"></span>
          Payment Gateway: ONLINE
        </span>
        <span class="hidden sm:inline border-r border-slate-600 h-3"></span>
        <span class="hidden sm:inline text-slate-300">Compliant Payment Gateway v2.5</span>
        <span class="hidden md:inline border-r border-slate-600 h-3"></span>
        <span class="hidden md:inline text-slate-300">PCI-DSS 3D-Secure 2.0</span>
      </div>
      <div class="flex items-center space-x-3 text-slate-400">
        <span>Managing Director: <strong class="text-white font-semibold">Sultan Sahi</strong>[cite: 1, 2]</span>
        <span>|</span>
        <span id="liveClock" class="font-mono text-slate-300"></span>
      </div>
    </div>
  </div>

  <!-- MAIN NAVIGATION HEADER -->
  <header class="bg-psw-slate text-white sticky top-0 z-40 shadow-xl border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-8 py-3.5 flex justify-between items-center">
      <!-- Brand Logo -->
      <div class="flex items-center space-x-3 cursor-pointer" onclick="switchTab('dashboard')">
        <div class="bg-gradient-to-tr from-emerald-500 to-teal-400 p-2.5 rounded-xl shadow-lg shadow-emerald-900/30">
          <i data-lucide="ship" class="w-6 h-6 text-slate-950"></i>
        </div>
        <div>
          <div class="flex items-center space-x-2">
            <h1 class="text-xl font-extrabold tracking-tight text-white">PakExport <span class="text-emerald-400">AI</span></h1>
            <span class="bg-emerald-950 text-emerald-300 border border-emerald-700/50 text-[10px] font-bold px-2 py-0.5 rounded-full uppercase">Trade Portal</span>
          </div>
          <p class="text-[11px] text-slate-400">Architected by <span class="text-slate-200 font-semibold">Sultan Sahi</span>[cite: 1, 2]</p>
        </div>
      </div>

      <!-- Navigation Tabs -->
      <nav class="hidden md:flex items-center space-x-1 bg-slate-800/80 p-1.5 rounded-xl border border-slate-700/60">
        <button id="nav-dashboard" onclick="switchTab('dashboard')" class="nav-btn px-4 py-2 text-xs font-semibold rounded-lg transition-all text-white bg-slate-700 shadow-sm flex items-center space-x-2">
          <i data-lucide="layout-dashboard" class="w-4 h-4"></i>
          <span>Dashboard</span>
        </button>
        <button id="nav-audit" onclick="switchTab('audit')" class="nav-btn px-4 py-2 text-xs font-semibold rounded-lg transition-all text-slate-300 hover:text-white flex items-center space-x-2">
          <i data-lucide="file-check-2" class="w-4 h-4"></i>
          <span>AI Compliance Audit</span>
        </button>
        <button id="nav-pricing" onclick="switchTab('pricing')" class="nav-btn px-4 py-2 text-xs font-semibold rounded-lg transition-all text-slate-300 hover:text-white flex items-center space-x-2">
          <i data-lucide="credit-card" class="w-4 h-4"></i>
          <span>Subscription Plans</span>
        </button>
      </nav>

      <!-- Active Plan Display -->
      <div class="flex items-center space-x-3">
        <div class="hidden sm:block text-right">
          <p class="text-[10px] text-slate-400 uppercase tracking-wider font-semibold">Free Audits Used</p>
          <p id="freeLimitBadge" class="text-xs font-bold text-emerald-400 flex items-center justify-end">
            <i data-lucide="shield-check" class="w-3.5 h-3.5 mr-1"></i> <span id="auditCountText">0</span> / 5 Used
          </p>
        </div>
        <button onclick="switchTab('pricing')" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 px-4 py-2 rounded-xl text-xs font-bold transition shadow-lg flex items-center space-x-1.5">
          <i data-lucide="zap" class="w-4 h-4"></i>
          <span>Pay & Upgrade</span>
        </button>
      </div>
    </div>
  </header>

  <!-- MAIN CONTENT VIEWS -->
  <main class="flex-grow">
    
    <!-- DASHBOARD VIEW -->
    <div id="tab-dashboard" class="tab-content">
      <!-- HERO SECTION -->
      <section class="hero-bg text-white py-16 px-4 sm:px-8 border-b border-slate-800">
        <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          <div class="lg:col-span-7 space-y-5">
            <div class="inline-flex items-center space-x-2 bg-emerald-950/80 border border-emerald-500/40 px-3 py-1 rounded-full text-xs font-medium text-emerald-300">
              <i data-lucide="credit-card" class="w-3.5 h-3.5"></i>
              <span>Automated Debit/Credit Card Billing System</span>
            </div>
            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black text-white leading-tight">
              B2B Trade Compliance & Automated Card Payments
            </h1>
            <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
              Verify trade shipping documents, verify HS codes, and seamlessly activate global export subscriptions using Visa, Mastercard, or direct Habib Bank Limited (HBL) transfer[cite: 1, 2].
            </p>
            <div class="pt-2 flex flex-wrap gap-3">
              <button onclick="switchTab('pricing')" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold px-6 py-3 rounded-xl text-xs sm:text-sm shadow-xl flex items-center space-x-2 transition-all transform hover:-translate-y-0.5">
                <i data-lucide="credit-card" class="w-4 h-4"></i>
                <span>Subscribe via ATM Card</span>
              </button>
              <button onclick="switchTab('audit')" class="bg-slate-800/90 hover:bg-slate-700 text-white font-semibold border border-slate-600 px-6 py-3 rounded-xl text-xs sm:text-sm shadow-lg flex items-center space-x-2 transition">
                <i data-lucide="file-search" class="w-4 h-4"></i>
                <span>Run Document Audit</span>
              </button>
            </div>
          </div>

          <!-- Merchant Card -->
          <div class="lg:col-span-5">
            <div class="glass-card p-6 rounded-2xl shadow-2xl text-white space-y-4 relative overflow-hidden">
              <div class="flex justify-between items-start border-b border-white/10 pb-3">
                <div>
                  <p class="text-[10px] text-slate-400 uppercase tracking-widest font-semibold">Official Bank Account</p>
                  <h3 class="text-base font-extrabold text-emerald-400">Habib Bank Limited (HBL)[cite: 1, 2]</h3>
                </div>
                <span class="bg-emerald-500/20 text-emerald-300 text-[10px] px-2.5 py-1 rounded-full font-mono font-bold border border-emerald-500/30">Verified</span>
              </div>

              <div class="space-y-3 text-xs">
                <div class="flex justify-between items-center bg-slate-900/60 p-2.5 rounded-lg border border-slate-700/50">
                  <span class="text-slate-400">Account Title:</span>
                  <span class="font-bold text-white">Sultan Sahi[cite: 1, 2]</span>
                </div>
                <div class="flex justify-between items-center bg-slate-900/60 p-2.5 rounded-lg border border-slate-700/50">
                  <span class="text-slate-400">Account Number:</span>
                  <span class="font-mono font-bold text-emerald-300">11317900687003[cite: 1, 2]</span>
                </div>
                <div class="flex justify-between items-center bg-slate-900/60 p-2.5 rounded-lg border border-slate-700/50">
                  <span class="text-slate-400">Managing Director:</span>
                  <span class="font-bold text-white">Sultan Sahi[cite: 1, 2]</span>
                </div>
              </div>

              <div class="pt-1 flex items-center justify-between text-[11px] text-slate-400">
                <span class="flex items-center"><i data-lucide="lock" class="w-3 h-3 mr-1 text-emerald-400"></i> PCI-DSS Compliant</span>
                <span class="flex items-center"><i data-lucide="shield-check" class="w-3 h-3 mr-1 text-emerald-400"></i> Instant Activation</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- METRICS SECTION -->
      <section class="max-w-7xl mx-auto px-4 sm:px-8 -mt-8 relative z-20 mb-12">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div class="bg-white p-5 rounded-2xl shadow-lg border border-slate-200 flex items-center justify-between">
            <div>
              <p class="text-xs font-medium text-slate-500">Audited Shipments</p>
              <h4 class="text-2xl font-black text-slate-900 mt-1">1,842</h4>
              <p class="text-[11px] text-emerald-600 font-semibold mt-1">↑ Active Port Declarations</p>
            </div>
            <div class="bg-blue-50 p-3 rounded-xl text-psw-navy">
              <i data-lucide="ship" class="w-6 h-6"></i>
            </div>
          </div>

          <div class="bg-white p-5 rounded-2xl shadow-lg border border-slate-200 flex items-center justify-between">
            <div>
              <p class="text-xs font-medium text-slate-500">Card Gateways</p>
              <h4 class="text-2xl font-black text-slate-900 mt-1">Visa & MC</h4>
              <p class="text-[11px] text-emerald-600 font-semibold mt-1">Debit & Credit Cards[cite: 1, 2]</p>
            </div>
            <div class="bg-indigo-50 p-3 rounded-xl text-indigo-600">
              <i data-lucide="credit-card" class="w-6 h-6"></i>
            </div>
          </div>

          <div class="bg-white p-5 rounded-2xl shadow-lg border border-slate-200 flex items-center justify-between">
            <div>
              <p class="text-xs font-medium text-slate-500">Compliance Rate</p>
              <h4 class="text-2xl font-black text-slate-900 mt-1">99.4%</h4>
              <p class="text-[11px] text-emerald-600 font-semibold mt-1">Customs Verified</p>
            </div>
            <div class="bg-emerald-50 p-3 rounded-xl text-emerald-600">
              <i data-lucide="check-circle-2" class="w-6 h-6"></i>
            </div>
          </div>

          <div class="bg-white p-5 rounded-2xl shadow-lg border border-slate-200 flex items-center justify-between">
            <div>
              <p class="text-xs font-medium text-slate-500">Portal Director</p>
              <h4 class="text-lg font-black text-slate-900 mt-1">Sultan Sahi[cite: 1, 2]</h4>
              <p class="text-[11px] text-slate-500 mt-1">Habib Bank Ltd Routing[cite: 1, 2]</p>
            </div>
            <div class="bg-amber-50 p-3 rounded-xl text-amber-600">
              <i data-lucide="user-check" class="w-6 h-6"></i>
            </div>
          </div>
        </div>
      </section>
    </div>

    <!-- AUDIT TOOL TAB -->
    <div id="tab-audit" class="tab-content hidden">
      <section class="max-w-7xl mx-auto px-4 sm:px-8 py-8">
        <div class="mb-8 flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border-b border-slate-200 pb-5">
          <div>
            <div class="flex items-center space-x-2">
              <span class="bg-psw-navy text-emerald-400 text-[10px] font-bold px-2 py-0.5 rounded">AI Compliance Engine</span>
            </div>
            <h2 class="text-2xl font-black text-slate-900 mt-1">Export Document AI Audit & Generator</h2>
            <p class="text-xs text-slate-500">Upload or input Commercial Invoices, Packing Lists, or Bills of Lading for verification.</p>
          </div>
          <div class="flex items-center space-x-2">
            <span class="text-xs text-slate-500 font-medium">Managing Director:</span>
            <span class="bg-slate-200 text-slate-800 text-xs font-bold px-3 py-1 rounded-full">Sultan Sahi[cite: 1, 2]</span>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
          <!-- Input Form Column -->
          <div class="lg:col-span-5 space-y-6">
            <div class="bg-white p-6 rounded-2xl shadow-md border border-slate-200 space-y-5">
              <h3 class="text-sm font-bold text-slate-900 flex items-center justify-between border-b border-slate-100 pb-3">
                <span class="flex items-center">
                  <i data-lucide="file-text" class="w-4 h-4 mr-2 text-psw-navy"></i>
                  Document Input Details
                </span>
                <span id="auditLimitNotice" class="text-[10px] font-bold bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full">
                  5 Free Audits Allowed
                </span>
              </h3>

              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Document Type</label>
                <select id="docType" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-medium focus:ring-2 focus:ring-emerald-500 focus:outline-none">
                  <option value="Commercial Invoice">Commercial Invoice (C/I)</option>
                  <option value="Bill of Lading">Bill of Lading (B/L)</option>
                  <option value="Packing List">Packing List (P/L)</option>
                  <option value="Certificate of Origin">Certificate of Origin (C/O)</option>
                </select>
              </div>

              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Exporter / Company Name</label>
                <input type="text" id="exporterName" value="Pak Trade Enterprises Pvt Ltd" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-medium focus:ring-2 focus:ring-emerald-500 focus:outline-none">
              </div>

              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">HS Code / Cargo Description</label>
                <input type="text" id="hsCode" value="HS Code: 5208.11 (Woven Cotton Fabrics) - 5,000 Yards" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-medium focus:ring-2 focus:ring-emerald-500 focus:outline-none">
              </div>

              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1">Document Contents / Raw Declaration</label>
                <textarea id="docContent" rows="5" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-3 text-xs font-medium focus:ring-2 focus:ring-emerald-500 focus:outline-none leading-relaxed">INVOICE NO: PTE-2026-904
DATE: 24 OCTOBER 2026
EXPORTER: Pak Trade Enterprises Pvt Ltd, Karachi, Pakistan
IMPORTER: Global Apparel Trading LLC, Hamburg, Germany
PORT OF LOADING: Karachi Port (PKKHI)
PORT OF DISCHARGE: Hamburg Container Terminal (DEHAM)
CARGO: 100% Cotton Bleached Fabrics (HS Code 5208.11)
QUANTITY: 5,000 Yards
TOTAL VALUE: USD $42,500</textarea>
              </div>

              <button onclick="runComplianceAudit()" class="w-full bg-psw-navy hover:bg-slate-800 text-white font-bold py-3 px-4 rounded-xl text-xs transition shadow-lg flex items-center justify-center space-x-2">
                <i data-lucide="sparkles" class="w-4 h-4 text-emerald-400"></i>
                <span>Run Compliance Audit</span>
              </button>
            </div>
          </div>

          <!-- Report PDF Canvas Column -->
          <div class="lg:col-span-7">
            <div id="auditLoader" class="hidden bg-white p-12 rounded-2xl shadow-md border border-slate-200 text-center space-y-4">
              <div class="inline-block animate-spin rounded-full h-10 w-10 border-4 border-emerald-500 border-t-transparent"></div>
              <p class="text-sm font-bold text-psw-navy">Auditing against global trade regulations...</p>
            </div>

            <!-- Upgrade Block Prompt when 5 Limit Reached -->
            <div id="limitReachedPrompt" class="hidden bg-amber-50 border-2 border-amber-400 p-8 rounded-2xl text-center space-y-4 shadow-xl">
              <div class="w-14 h-14 bg-amber-100 text-amber-600 rounded-full flex items-center justify-center mx-auto">
                <i data-lucide="lock" class="w-7 h-7"></i>
              </div>
              <h3 class="text-xl font-extrabold text-slate-900">5 Free Audits Limit Reached!</h3>
              <p class="text-xs text-slate-600 max-w-md mx-auto">
                Aap ne apne 5 Free Verifications use kar liye hain. Unlimited document audits ke liye kripya subscription upgrade karein[cite: 1, 2].
              </p>
              <button onclick="switchTab('pricing')" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black px-6 py-3 rounded-xl text-xs transition shadow-lg inline-flex items-center space-x-2">
                <i data-lucide="credit-card" class="w-4 h-4"></i>
                <span>Upgrade via ATM / Debit Card[cite: 1, 2]</span>
              </button>
            </div>

            <div id="reportContainer" class="bg-white p-6 rounded-2xl shadow-lg border border-slate-200 space-y-5">
              <div id="pdfExportArea" class="p-6 bg-white rounded-xl border border-slate-200 space-y-5">
                <div class="border-b-2 border-psw-navy pb-4 flex justify-between items-start">
                  <div>
                    <h3 class="text-lg font-black text-psw-navy">PakExport AI Portal[cite: 1, 2]</h3>
                    <p class="text-[11px] text-slate-500">Official Compliance & Verification Report</p>
                  </div>
                  <div class="text-right text-[11px] text-slate-600">
                    <p class="font-bold text-slate-800">Report: <span id="reportIdDisplay" class="font-mono text-psw-navy">AUD-8831</span></p>
                    <p>Director: <strong>Sultan Sahi[cite: 1, 2]</strong></p>
                  </div>
                </div>

                <div class="grid grid-cols-3 gap-3 text-xs bg-slate-50 p-3 rounded-xl border border-slate-200">
                  <div>
                    <span class="text-[10px] text-slate-400 uppercase font-bold block">Document</span>
                    <strong id="repDocType" class="text-slate-800">Commercial Invoice</strong>
                  </div>
                  <div>
                    <span class="text-[10px] text-slate-400 uppercase font-bold block">Exporter</span>
                    <strong id="repExporter" class="text-slate-800 truncate block">Pak Trade Ent.</strong>
                  </div>
                  <div>
                    <span class="text-[10px] text-slate-400 uppercase font-bold block">Compliance Status</span>
                    <strong class="text-emerald-600 font-extrabold">100% PASSED</strong>
                  </div>
                </div>

                <div class="space-y-3">
                  <h4 class="text-xs font-bold uppercase text-slate-500 border-b border-slate-100 pb-1">AI Regulatory Findings</h4>
                  <div id="aiAuditFindings" class="text-xs text-slate-700 space-y-2">
                    <div class="p-3 bg-emerald-50 rounded-lg border border-emerald-200 text-emerald-900">
                      <strong>✓ HS Code Validated:</strong> HS Code 5208.11 matches declared 100% Cotton Woven Fabrics cargo.
                    </div>
                  </div>
                </div>

                <div class="pt-4 border-t border-slate-200 flex justify-between items-center text-[10px] text-slate-400">
                  <p>Habib Bank Limited (HBL) Account: 11317900687003 | Sultan Sahi[cite: 1, 2]</p>
                  <p class="font-mono text-emerald-600 font-bold">STATUS: VERIFIED</p>
                </div>
              </div>

              <div class="flex justify-end gap-3">
                <button onclick="downloadPDFReport()" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-5 py-2.5 rounded-xl text-xs transition shadow-md flex items-center space-x-2">
                  <i data-lucide="download" class="w-4 h-4"></i>
                  <span>Download Official PDF Report</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>

    <!-- SUBSCRIPTION PRICING TAB (WITH ATM CARD PAYMENT INTEGRATION) -->
    <div id="tab-pricing" class="tab-content hidden">
      <section class="max-w-7xl mx-auto px-4 sm:px-8 py-12">
        <div class="text-center max-w-3xl mx-auto space-y-3 mb-12">
          <span class="bg-emerald-100 text-emerald-800 text-xs font-bold px-3.5 py-1 rounded-full uppercase tracking-wider">Automated Payment Portal</span>
          <h2 class="text-3xl font-black text-slate-900">Choose Plan & Pay via ATM / Credit Card[cite: 1, 2]</h2>
          <p class="text-xs sm:text-sm text-slate-500">
            Click on any plan below to open the **Automated ATM Debit / Credit Card Payment Gateway**. Instant activation with official payout routing to Habib Bank Limited (HBL)[cite: 1, 2].
          </p>
        </div>

        <!-- PRICING CARDS -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch">
          
          <!-- Starter Tier -->
          <div class="bg-white rounded-2xl shadow-md border border-slate-200 p-7 flex flex-col justify-between space-y-6 hover:shadow-xl transition">
            <div class="space-y-4">
              <span class="text-xs font-bold text-slate-400 uppercase tracking-widest">Starter Plan</span>
              <div class="flex items-baseline space-x-1">
                <span class="text-4xl font-black text-slate-900">$29</span>
                <span class="text-slate-500 text-xs font-medium">/ month</span>
              </div>
              <p class="text-xs text-slate-500 leading-relaxed">Ideal for small exporters processing document audits monthly.</p>
              <ul class="space-y-2.5 text-xs text-slate-600 pt-2">
                <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-emerald-500 mr-2"></i> Unlimited AI Audits</li>
                <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-emerald-500 mr-2"></i> PDF Audit Download</li>
                <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-emerald-500 mr-2"></i> Instant Card Activation[cite: 1, 2]</li>
              </ul>
            </div>
            <button onclick="openCheckoutModal('Starter Plan', 29)" class="w-full bg-slate-900 hover:bg-slate-800 text-white font-bold py-3.5 rounded-xl text-xs transition shadow-md flex justify-center items-center space-x-2">
              <i data-lucide="credit-card" class="w-4 h-4 text-emerald-400"></i>
              <span>Pay $29 via ATM / Card[cite: 1, 2]</span>
            </button>
          </div>

          <!-- Professional Tier (Featured) -->
          <div class="bg-psw-navy text-white rounded-2xl shadow-2xl border-2 border-emerald-500 p-7 flex flex-col justify-between space-y-6 relative overflow-hidden transform md:-translate-y-2">
            <div class="absolute top-0 right-0 bg-emerald-500 text-slate-950 font-black text-[10px] uppercase px-3 py-1 rounded-bl-xl tracking-wider">
              RECOMMENDED
            </div>
            <div class="space-y-4">
              <span class="text-xs font-bold text-emerald-400 uppercase tracking-widest">Professional Trader</span>
              <div class="flex items-baseline space-x-1">
                <span class="text-4xl font-black text-white">$149</span>
                <span class="text-slate-300 text-xs font-medium">/ month</span>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">Designed for active freight forwarders, textile houses, and global exporters.</p>
              <ul class="space-y-2.5 text-xs text-slate-200 pt-2">
                <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-emerald-400 mr-2"></i> Unlimited AI Compliance Audits</li>
                <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-emerald-400 mr-2"></i> Priority Verification</li>
                <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-emerald-400 mr-2"></i> Multi-User Access</li>
              </ul>
            </div>
            <button onclick="openCheckoutModal('Professional Trader', 149)" class="w-full bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black py-4 rounded-xl text-xs transition shadow-xl flex justify-center items-center space-x-2">
              <i data-lucide="zap" class="w-4 h-4"></i>
              <span>Pay $149 via ATM / Card[cite: 1, 2]</span>
            </button>
          </div>

          <!-- Enterprise Tier -->
          <div class="bg-white rounded-2xl shadow-md border border-slate-200 p-7 flex flex-col justify-between space-y-6 hover:shadow-xl transition">
            <div class="space-y-4">
              <span class="text-xs font-bold text-slate-400 uppercase tracking-widest">Enterprise Global</span>
              <div class="flex items-baseline space-x-1">
                <span class="text-4xl font-black text-slate-900">$249</span>
                <span class="text-slate-500 text-xs font-medium">/ month</span>
              </div>
              <p class="text-xs text-slate-500 leading-relaxed">Full portal integration with dedicated advisory by Managing Director Sultan Sahi[cite: 1, 2].</p>
              <ul class="space-y-2.5 text-xs text-slate-600 pt-2">
                <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-emerald-500 mr-2"></i> Unlimited Everything</li>
                <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-emerald-500 mr-2"></i> Dedicated Account Advisor</li>
                <li class="flex items-center"><i data-lucide="check" class="w-4 h-4 text-emerald-500 mr-2"></i> Custom API Access</li>
              </ul>
            </div>
            <button onclick="openCheckoutModal('Enterprise Global', 249)" class="w-full bg-slate-900 hover:bg-slate-800 text-white font-bold py-3.5 rounded-xl text-xs transition shadow-md flex justify-center items-center space-x-2">
              <i data-lucide="shield-check" class="w-4 h-4 text-emerald-400"></i>
              <span>Pay $249 via ATM / Card[cite: 1, 2]</span>
            </button>
          </div>

        </div>

        <!-- Official Merchant Notice -->
        <div class="mt-12 bg-slate-900 text-white p-6 rounded-2xl border border-slate-800 flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="space-y-1">
            <h4 class="text-sm font-bold text-emerald-400 flex items-center">
              <i data-lucide="landmark" class="w-4 h-4 mr-2"></i> Direct Habib Bank Limited (HBL) Routing[cite: 1, 2]
            </h4>
            <p class="text-xs text-slate-300">All card transactions process through Merchant Account Title: <strong>Sultan Sahi[cite: 1, 2]</strong> | Account No: <strong>11317900687003[cite: 1, 2]</strong></p>
          </div>
          <span class="bg-slate-800 text-slate-300 border border-slate-700 px-4 py-2 rounded-xl text-xs font-mono font-bold whitespace-nowrap">
            Habib Bank Limited (HBL)[cite: 1, 2]
          </span>
        </div>
      </section>
    </div>

  </main>

  <!-- REALISTIC ATM / CREDIT CARD PAYMENT MODAL -->
  <div id="checkoutModal" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-white w-full max-w-lg rounded-2xl shadow-2xl border border-slate-200 overflow-hidden transform transition-all">
      
      <!-- Modal Header -->
      <div class="bg-psw-navy text-white p-5 flex justify-between items-center border-b border-slate-800">
        <div class="flex items-center space-x-3">
          <div class="bg-emerald-500/20 p-2.5 rounded-xl text-emerald-400 border border-emerald-500/30">
            <i data-lucide="credit-card" class="w-5 h-5"></i>
          </div>
          <div>
            <h3 class="text-sm font-bold text-white">Automated Card Checkout</h3>
            <p class="text-[11px] text-slate-300">Selected Plan: <span id="modalPlanName" class="text-emerald-400 font-bold">Starter ($29/mo)</span></p>
          </div>
        </div>
        <button onclick="closeCheckoutModal()" class="text-slate-400 hover:text-white p-1 rounded-lg">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <!-- Payment Method Switcher Tabs -->
      <div class="flex border-b border-slate-200 bg-slate-50 text-xs font-bold">
        <button id="tabBtnCard" onclick="togglePaymentTab('card')" class="flex-1 py-3 border-b-2 border-emerald-500 text-emerald-600 flex justify-center items-center space-x-2">
          <i data-lucide="credit-card" class="w-4 h-4"></i>
          <span>ATM / Debit / Credit Card[cite: 1, 2]</span>
        </button>
        <button id="tabBtnHbl" onclick="togglePaymentTab('hbl')" class="flex-1 py-3 text-slate-500 hover:text-slate-800 flex justify-center items-center space-x-2">
          <i data-lucide="landmark" class="w-4 h-4"></i>
          <span>Direct HBL Transfer[cite: 1, 2]</span>
        </button>
      </div>

      <!-- CARD FORM -->
      <form id="cardPaymentForm" onsubmit="processCardPayment(event)" class="p-6 space-y-4">
        
        <!-- Live Virtual Card Visual Preview -->
        <div class="bg-gradient-to-r from-slate-900 to-psw-navy p-4 rounded-xl text-white shadow-md relative overflow-hidden space-y-3">
          <div class="flex justify-between items-center">
            <span class="text-[10px] uppercase font-mono tracking-widest text-slate-400">Debit / Credit Card[cite: 1, 2]</span>
            <span id="cardTypeBadge" class="text-[10px] font-black px-2 py-0.5 rounded bg-blue-600 text-white">VISA</span>
          </div>
          <div class="flex items-center space-x-3">
            <div class="card-chip w-9 h-6 rounded-md"></div>
            <i data-lucide="wifi" class="w-4 h-4 text-slate-400 rotate-90"></i>
          </div>
          <div class="font-mono text-sm tracking-wider font-bold text-slate-200" id="cardPreviewNum">
            •••• •••• •••• ••••
          </div>
          <div class="flex justify-between items-end text-[10px] font-mono">
            <div>
              <span class="text-slate-400 block text-[8px] uppercase">Cardholder</span>
              <span id="cardPreviewHolder" class="font-bold text-white uppercase">SULTAN SAHI[cite: 1, 2]</span>
            </div>
            <div>
              <span class="text-slate-400 block text-[8px] uppercase">Expires</span>
              <span id="cardPreviewExp" class="font-bold text-white">12/28</span>
            </div>
          </div>
        </div>

        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">Cardholder Full Name</label>
          <input type="text" id="cardName" required placeholder="Sultan Sahi[cite: 1, 2]" oninput="updateCardPreview()" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-semibold text-slate-800 focus:ring-2 focus:ring-emerald-500 focus:outline-none">
        </div>

        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">ATM / Debit / Credit Card Number[cite: 1, 2]</label>
          <input type="text" id="cardNumber" required maxlength="19" oninput="formatCardNumber(this)" placeholder="4000 1234 5678 9010" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-mono font-bold text-slate-800 focus:ring-2 focus:ring-emerald-500 focus:outline-none">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Expiry Date (MM/YY)</label>
            <input type="text" id="cardExpiry" required maxlength="5" placeholder="12/28" oninput="formatExpiry(this)" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2.5 text-xs font-mono font-bold text-slate-800 focus:ring-2 focus:ring-emerald-500 focus:outline-none text-center">
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">CVV Security Code</label>
            <input type="password" id="cardCvv" required maxlength="4" placeholder="888" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2.5 text-xs font-mono font-bold text-slate-800 focus:ring-2 focus:ring-emerald-500 focus:outline-none text-center">
          </div>
        </div>

        <!-- Direct Payout Confirmation Badge -->
        <div class="bg-emerald-50 p-3 rounded-xl border border-emerald-200 text-[11px] text-emerald-900 flex items-start space-x-2">
          <i data-lucide="shield-check" class="w-4 h-4 text-emerald-600 mt-0.5 flex-shrink-0"></i>
          <div>
            <p><strong>Merchant Transfer Routing:</strong> Automated payout destination Habib Bank Limited (HBL) Account: <strong>11317900687003[cite: 1, 2]</strong> (Sultan Sahi[cite: 1, 2]).</p>
          </div>
        </div>

        <button type="submit" class="w-full bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black py-3.5 rounded-xl text-xs transition shadow-xl flex justify-center items-center space-x-2">
          <i data-lucide="lock" class="w-4 h-4"></i>
          <span>Confirm & Pay Now</span>
        </button>

      </form>

      <!-- DIRECT HBL TAB CONTENT -->
      <div id="hblTransferContent" class="p-6 space-y-4 hidden">
        <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-3 text-xs">
          <h4 class="font-bold text-slate-900 border-b border-slate-200 pb-2">Habib Bank Limited (HBL) Official Transfer[cite: 1, 2]</h4>
          <div class="flex justify-between">
            <span class="text-slate-500">Bank Name:</span>
            <strong class="text-slate-800">Habib Bank Limited (HBL)[cite: 1, 2]</strong>
          </div>
          <div class="flex justify-between">
            <span class="text-slate-500">Account Title:</span>
            <strong class="text-slate-800">Sultan Sahi[cite: 1, 2]</strong>
          </div>
          <div class="flex justify-between">
            <span class="text-slate-500">Account Number:</span>
            <strong class="font-mono text-emerald-700">11317900687003[cite: 1, 2]</strong>
          </div>
        </div>
        <p class="text-[11px] text-slate-500">After sending transfer, enter your transaction reference number below for manual instant activation.</p>
        <input type="text" id="hblRefNo" placeholder="Enter HBL Transaction Reference ID" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-mono text-slate-800 focus:ring-2 focus:ring-emerald-500 focus:outline-none">
        <button onclick="submitHblTransfer()" class="w-full bg-psw-navy hover:bg-slate-800 text-white font-bold py-3.5 rounded-xl text-xs transition shadow-lg">
          Submit HBL Payment Reference[cite: 1, 2]
        </button>
      </div>

      <!-- PROCESSING OVERLAY -->
      <div id="paymentProcessing" class="p-10 text-center space-y-4 hidden">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-4 border-emerald-500 border-t-transparent"></div>
        <h4 class="text-base font-bold text-slate-900">Processing Card Payment...</h4>
        <p class="text-xs text-slate-500">Connecting to Habib Bank Limited (HBL) Gateway[cite: 1, 2]</p>
      </div>

      <!-- SUCCESS RECEIPT MODAL -->
      <div id="paymentSuccess" class="p-8 text-center space-y-4 hidden">
        <div class="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto shadow-inner">
          <i data-lucide="check" class="w-8 h-8"></i>
        </div>
        <h4 class="text-lg font-black text-slate-900">Payment Approved & Plan Activated!</h4>
        <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 text-left text-xs space-y-2">
          <div class="flex justify-between">
            <span class="text-slate-500">Activated Plan:</span>
            <strong id="recPlan" class="text-slate-900">Professional Trader</strong>
          </div>
          <div class="flex justify-between">
            <span class="text-slate-500">Amount Charged:</span>
            <strong id="recAmount" class="font-mono text-emerald-600">$149.00 USD</strong>
          </div>
          <div class="flex justify-between">
            <span class="text-slate-500">Merchant Routing:</span>
            <strong class="text-slate-800">HBL Account 11317900687003[cite: 1, 2]</strong>
          </div>
          <div class="flex justify-between">
            <span class="text-slate-500">Account Title:</span>
            <strong class="text-slate-800">Sultan Sahi[cite: 1, 2]</strong>
          </div>
        </div>
        <button onclick="closeCheckoutModal()" class="w-full bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black py-3 rounded-xl text-xs transition">
          Return to Portal
        </button>
      </div>

    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div id="toast" class="fixed bottom-6 right-6 bg-psw-navy text-white px-5 py-3 rounded-xl shadow-2xl border border-slate-700 flex items-center space-x-3 transition-all duration-300 opacity-0 pointer-events-none z-50">
    <i id="toastIcon" data-lucide="check-circle" class="w-5 h-5 text-emerald-400"></i>
    <span id="toastMessage" class="text-xs font-semibold">Message</span>
  </div>

  <!-- FOOTER -->
  <footer class="bg-psw-slate text-slate-400 border-t border-slate-800 py-8 px-4 sm:px-8 text-xs">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-4">
      <div class="flex items-center space-x-3">
        <div class="bg-emerald-500/20 p-2 rounded-lg text-emerald-400">
          <i data-lucide="ship" class="w-4 h-4"></i>
        </div>
        <div>
          <p class="font-bold text-white">PakExport AI Portal[cite: 1, 2]</p>
          <p class="text-[11px] text-slate-500">Architected by Sultan Sahi[cite: 1, 2]</p>
        </div>
      </div>
      <div class="text-center sm:text-right text-[11px] text-slate-500">
        <p>Merchant Payout: Habib Bank Limited (HBL) | Account No: 11317900687003[cite: 1, 2]</p>
      </div>
    </div>
  </footer>

  <!-- MAIN APPLICATION JAVASCRIPT -->
  <script>
    // Initialize Icons
    lucide.createIcons();

    // Usage State (Max 5 Free)
    let auditCount = 0;
    const MAX_FREE_AUDITS = 5;

    // Clock
    function updateClock() {
      const now = new Date();
      document.getElementById('liveClock').innerText = now.toUTCString().replace('GMT', 'UTC');
    }
    setInterval(updateClock, 1000);
    updateClock();

    // App State
    let selectedPlan = { name: 'Starter Plan', price: 29 };

    // Navigation Switcher
    function switchTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      document.getElementById(`tab-${tabId}`).classList.remove('hidden');

      document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('bg-slate-700', 'text-white', 'shadow-sm');
        btn.classList.add('text-slate-300');
      });

      const activeNav = document.getElementById(`nav-${tabId}`);
      if (activeNav) {
        activeNav.classList.add('bg-slate-700', 'text-white', 'shadow-sm');
        activeNav.classList.remove('text-slate-300');
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Toast Engine
    function showToast(msg, isSuccess = true) {
      const toast = document.getElementById('toast');
      const toastMsg = document.getElementById('toastMessage');
      const toastIcon = document.getElementById('toastIcon');

      toastMsg.innerText = msg;
      if (isSuccess) {
        toastIcon.setAttribute('data-lucide', 'check-circle');
        toastIcon.className = 'w-5 h-5 text-emerald-400';
      } else {
        toastIcon.setAttribute('data-lucide', 'alert-triangle');
        toastIcon.className = 'w-5 h-5 text-amber-400';
      }
      lucide.createIcons();

      toast.classList.remove('opacity-0', 'pointer-events-none');
      setTimeout(() => {
        toast.classList.add('opacity-0', 'pointer-events-none');
      }, 4000);
    }

    // Compliance Audit Engine with 5 Limit Control
    async function runComplianceAudit() {
      if (auditCount >= MAX_FREE_AUDITS) {
        document.getElementById('reportContainer').classList.add('hidden');
        document.getElementById('limitReachedPrompt').classList.remove('hidden');
        showToast('5 Free Limit Reached! Please upgrade plan.', false);
        return;
      }

      const docType = document.getElementById('docType').value;
      const exporter = document.getElementById('exporterName').value;
      const content = document.getElementById('docContent').value;

      if (!content.trim()) {
        showToast('Please enter document details.', false);
        return;
      }

      document.getElementById('auditLoader').classList.remove('hidden');
      document.getElementById('reportContainer').classList.add('hidden');

      setTimeout(() => {
        auditCount++;
        document.getElementById('auditCountText').innerText = auditCount;

        document.getElementById('repDocType').innerText = docType;
        document.getElementById('repExporter').innerText = exporter;
        document.getElementById('reportIdDisplay').innerText = `AUD-${Math.floor(1000 + Math.random() * 9000)}`;

        document.getElementById('auditLoader').classList.add('hidden');
        document.getElementById('reportContainer').classList.remove('hidden');

        if (auditCount >= MAX_FREE_AUDITS) {
          showToast('Audit Completed! (Free Limit Reached: 5/5)');
        } else {
          showToast(`Audit Completed! (${auditCount}/5 Used)`);
        }
      }, 1200);
    }

    function downloadPDFReport() {
      const element = document.getElementById('pdfExportArea');
      const reportId = document.getElementById('reportIdDisplay').innerText;
      const opt = {
        margin: 0.5,
        filename: `PakExport_Audit_${reportId}.pdf`,
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
      };
      html2pdf().set(opt).from(element).save();
      showToast('Downloading Official PDF Report...');
    }

    // ATM CARD MODAL LOGIC
    function openCheckoutModal(planName, price) {
      selectedPlan = { name: planName, price: price };
      document.getElementById('modalPlanName').innerText = `${planName} ($${price}/mo)`;
      
      document.getElementById('checkoutModal').classList.remove('hidden');
      document.getElementById('cardPaymentForm').classList.remove('hidden');
      document.getElementById('hblTransferContent').classList.add('hidden');
      document.getElementById('paymentProcessing').classList.add('hidden');
      document.getElementById('paymentSuccess').classList.add('hidden');

      togglePaymentTab('card');
    }

    function closeCheckoutModal() {
      document.getElementById('checkoutModal').classList.add('hidden');
    }

    function togglePaymentTab(type) {
      const cardBtn = document.getElementById('tabBtnCard');
      const hblBtn = document.getElementById('tabBtnHbl');
      const cardForm = document.getElementById('cardPaymentForm');
      const hblContent = document.getElementById('hblTransferContent');

      if (type === 'card') {
        cardBtn.className = "flex-1 py-3 border-b-2 border-emerald-500 text-emerald-600 flex justify-center items-center space-x-2";
        hblBtn.className = "flex-1 py-3 text-slate-500 hover:text-slate-800 flex justify-center items-center space-x-2";
        cardForm.classList.remove('hidden');
        hblContent.classList.add('hidden');
      } else {
        hblBtn.className = "flex-1 py-3 border-b-2 border-emerald-500 text-emerald-600 flex justify-center items-center space-x-2";
        cardBtn.className = "flex-1 py-3 text-slate-500 hover:text-slate-800 flex justify-center items-center space-x-2";
        hblContent.classList.remove('hidden');
        cardForm.classList.add('hidden');
      }
    }

    function updateCardPreview() {
      const holder = document.getElementById('cardName').value;
      document.getElementById('cardPreviewHolder').innerText = holder.trim() ? holder.toUpperCase() : 'SULTAN SAHI[cite: 1, 2]';
    }

    function formatCardNumber(input) {
      let val = input.value.replace(/\D/g, '').substring(0, 16);
      let formatted = val.match(/.{1,4}/g)?.join(' ') || val;
      input.value = formatted;
      document.getElementById('cardPreviewNum').innerText = formatted || '•••• •••• •••• ••••';

      const badge = document.getElementById('cardTypeBadge');
      if (val.startsWith('4')) {
        badge.innerText = 'VISA';
        badge.className = 'text-[10px] font-black px-2 py-0.5 rounded bg-blue-600 text-white';
      } else if (val.startsWith('5')) {
        badge.innerText = 'MASTERCARD';
        badge.className = 'text-[10px] font-black px-2 py-0.5 rounded bg-amber-600 text-white';
      } else if (val.startsWith('62')) {
        badge.innerText = 'UNIONPAY';
        badge.className = 'text-[10px] font-black px-2 py-0.5 rounded bg-teal-600 text-white';
      } else {
        badge.innerText = 'CARD';
        badge.className = 'text-[10px] font-black px-2 py-0.5 rounded bg-slate-700 text-white';
      }
    }

    function formatExpiry(input) {
      let val = input.value.replace(/\D/g, '');
      if (val.length >= 2) {
        input.value = val.substring(0, 2) + '/' + val.substring(2, 4);
      } else {
        input.value = val;
      }
      document.getElementById('cardPreviewExp').innerText = input.value || '12/28';
    }

    // Process Simulated Payment
    function processCardPayment(e) {
      e.preventDefault();

      document.getElementById('cardPaymentForm').classList.add('hidden');
      document.getElementById('paymentProcessing').classList.remove('hidden');

      setTimeout(() => {
        document.getElementById('paymentProcessing').classList.add('hidden');
        document.getElementById('paymentSuccess').classList.remove('hidden');

        document.getElementById('recPlan').innerText = selectedPlan.name;
        document.getElementById('recAmount').innerText = `$${selectedPlan.price}.00 USD`;

        // Reset Limit on Successful Payment
        auditCount = 0;
        document.getElementById('auditCountText').innerText = '0 (Unlimited)';
        document.getElementById('limitReachedPrompt').classList.add('hidden');

        showToast(`Payment of $${selectedPlan.price} Approved! Plan Activated.`);
      }, 2000);
    }

    function submitHblTransfer() {
      const ref = document.getElementById('hblRefNo').value;
      if (!ref.trim()) {
        showToast('Please enter HBL reference number.', false);
        return;
      }

      showToast('HBL Transfer Reference Submitted! Activating...');
      setTimeout(() => {
        closeCheckoutModal();
        auditCount = 0;
        document.getElementById('auditCountText').innerText = '0 (Unlimited)';
        document.getElementById('limitReachedPrompt').classList.add('hidden');
      }, 1200);
    }
  </script>
</body>
</html>
""", unsafe_allow_html=True)
