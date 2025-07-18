import streamlit as st
import os
import json


st.set_page_config(layout="wide", page_title="Smart Contract Vulnerability Analyzer")

with st.sidebar:
    st.markdown("## 📂 Upload Solidity Smart Contract")
    st.markdown("Upload a `.sol` file and click Submit to analyze it.")

    uploaded_file = st.file_uploader(
        "Choose a .sol file",
        type=["sol"],
        label_visibility="collapsed",
        help="Only Solidity (.sol) files allowed",
    )

    submit_button = st.button("🚀 Submit & Analyze")

st.markdown("<h1 style='font-size: 36px;'>🔎 Smart Contract Vulnerability Analyzer</h1>", unsafe_allow_html=True)

if uploaded_file and submit_button:
    file_path = os.path.join("uploads", uploaded_file.name)
    os.makedirs("uploads", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"✅ File `{uploaded_file.name}` uploaded successfully.")

    st.markdown("<h2 style='font-size: 28px;'>🧠 Analysis Output</h2>", unsafe_allow_html=True)
    st.info("Running LLM vulnerability analysis on the uploaded smart contract...")

    # --- Replace with actual call to your LLM pipeline ---
    # from your_analysis_module import analyze_contract
    # result = analyze_contract(file_path)

    result = {
        "contract": uploaded_file.name,
        "suspicious_regions": [
            {
                "line_range": "12-18",
                "violation": "Reentrancy Risk"
            },
            {
                "line_range": "42-45",
                "violation": "Unchecked Low-level Call"
            }
        ]
    }

    st.json(result)

    os.makedirs("output", exist_ok=True)
    json_path = os.path.join("output", "analysis_report.json")
    with open(json_path, "w") as f:
        json.dump(result, f, indent=2)

    st.download_button(
        label="📥 Download JSON Report",
        data=json.dumps(result, indent=2),
        file_name="analysis_report.json",
        mime="application/json"
    )

else:
    st.markdown(
        "<p style='font-size: 20px;'> Upload a smart contract from the left panel and click 'Submit & Analyze'.</p>",
        unsafe_allow_html=True
    )
