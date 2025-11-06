import streamlit as st
import numpy as np
from safe_threat_detector import SafeThreatDetector

def business_value_section():
    st.markdown("---")
    st.header("💰 Business Value Demonstration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔄 Before VynSec AI")
        st.metric("Annual Cost", "₹36,00,000")
        st.metric("Security Team", "2 Engineers")
        st.metric("Daily Alerts", "10,000")
        st.metric("False Positives", "9,000 (90%)")
        st.metric("Response Time", "45 minutes")
        st.metric("Coverage", "8 hours/day")
    
    with col2:
        st.subheader("🚀 After VynSec AI")
        st.metric("Annual Cost", "₹6,00,000", "-67%")
        st.metric("Security Team", "1 Engineer + AI", "-50%")
        st.metric("Daily Alerts", "1,500", "-85%")
        st.metric("False Positives", "150", "-98%")
        st.metric("Response Time", "3 seconds", "-99%")
        st.metric("Coverage", "24/7/365", "+300%")
    
    # ROI Calculation
    st.subheader("📈 Return on Investment (ROI)")
    
    savings_per_year = 3600000 - 600000
    monthly_savings = savings_per_year / 12
    
    st.success(f"""
    **Annual Savings: ₹{savings_per_year:,}**  
    **Monthly Savings: ₹{monthly_savings:,.0f}**  
    **ROI: 500% in first year**
    """)
    
    # Cost Breakdown
    st.subheader("🧮 Cost Breakdown")
    
    cost_data = {
        'Expense': ['Security Engineers', 'AI System', 'Tool Licenses', 'Training', 'Total'],
        'Traditional': ['₹36,00,000', '₹0', '₹4,00,000', '₹2,00,000', '₹42,00,000'],
        'With VynSec': ['₹18,00,000', '₹6,00,000', '₹1,00,000', '₹50,000', '₹25,50,000']
    }
    
    st.table(cost_data)

def main():
    st.set_page_config(page_title="VynSec AI - BUSINESS VALUE", layout="wide")
    
    st.title("🛡️ VynSec AI Cybersecurity - Business Value")
    st.warning("🔒 **SAFE MODE**: All processing happens locally on your computer")
    
    # Initialize detector
    if 'detector' not in st.session_state:
        st.session_state.detector = SafeThreatDetector()
        st.session_state.detector.train_with_sample_data()
    
    # Threat Detection Section
    st.header("🤖 Live Threat Detection Demo")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        packets = st.slider("Packets/Second", 0, 2000, 100)
    with col2:
        ports = st.slider("Unique Ports", 0, 100, 20) 
    with col3:
        data_transfer = st.slider("Data Transfer (MB)", 0, 20000, 500)
    
    if st.button("Check for Threats"):
        manual_input = {
            'packets': packets,
            'ports': ports,
            'data_transfer': data_transfer
        }
        
        result = st.session_state.detector.detect_threats_safe(manual_input)
        
        if result['is_threat']:
            st.error(f"🚨 THREAT DETECTED: {result['threat_type']}")
            st.info(f"Confidence: {result['confidence']:.2%}")
        else:
            st.success("✅ No threats detected")
    
    # ADD BUSINESS VALUE SECTION
    business_value_section()

if __name__ == "__main__":
    main()