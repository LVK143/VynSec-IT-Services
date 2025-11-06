# File: safe_threat_detector.py
# This runs 100% locally - no data leaves your computer
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

class SafeThreatDetector:
    def __init__(self):
        
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.is_trained = False
        self.threat_log = []
    
    def train_with_sample_data(self):
        """Train with completely fake sample data"""
        print("🤖 Training AI with LOCAL sample data only...")
        
        # Generate fake normal behavior data
        np.random.seed(42)  # For consistent results
        normal_data = np.random.normal(100, 20, (100, 3))  # Fake network data
        
        self.model.fit(normal_data)
        self.is_trained = True
        print("✅ AI trained successfully - ALL DATA STAYS LOCAL")
        return True
    
    def detect_threats_safe(self, manual_input):
        """Detect threats using only manual input - no system access"""
        if not self.is_trained:
            return {"error": "Train the model first"}
        
        # Convert manual input to features
        test_data = np.array([[manual_input['packets'], 
                              manual_input['ports'], 
                              manual_input['data_transfer']]])
        
        # Local prediction only
        prediction = self.model.predict(test_data)
        anomaly_score = self.model.decision_function(test_data)
        
        result = {
            'is_threat': prediction[0] == -1,
            'confidence': float(abs(anomaly_score[0])),
            'threat_type': self.safe_rule_check(manual_input),
            'data_usage': 'LOCAL_ONLY - No external calls'
        }
        
        if result['is_threat']:
            self.threat_log.append(result)
            print(f"🚨 THREAT DETECTED (Locally): {result}")
        
        return result
    
    def safe_rule_check(self, input_data):
        """Rule-based checks using only provided input"""
        threats = []
        
        if input_data['packets'] > 1000:
            threats.append('possible_flooding')
        if input_data['ports'] > 50:
            threats.append('possible_port_scan')
        if input_data['data_transfer'] > 10000:
            threats.append('possible_data_theft')
            
        return threats

# SAFE TEST - No real system data
if __name__ == "__main__":
    detector = SafeThreatDetector()
    detector.train_with_sample_data()  # Uses fake data
    
    # Test with manual values
    test_input = {
        'packets': 1500,      # You control this value
        'ports': 65,          # You control this value  
        'data_transfer': 15000 # You control this value
    }
    
    result = detector.detect_threats_safe(test_input)
    print("🔒 SAFE Result:", result)