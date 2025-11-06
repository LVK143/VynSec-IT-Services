# Save as: client_demo_1.py
from safe_threat_detector import SafeThreatDetector

def basic_threat_demo():
    print("🎬 VynSec AI Cybersecurity Demo")
    print("=" * 50)
    
    # Initialize AI
    ai = SafeThreatDetector()
    ai.train_with_sample_data()
    
    # Demo scenarios
    scenarios = [
        ("Normal Office Traffic", 100, 20, 500),
        ("Port Scanning Attack", 300, 65, 1000),
        ("DDoS Attack", 2500, 30, 5000),
        ("Data Theft Attempt", 200, 25, 25000)
    ]
    
    for name, packets, ports, data in scenarios:
        result = ai.detect_threats_safe({
            'packets': packets,
            'ports': ports,
            'data_transfer': data
        })
        
        status = "🚨 BLOCKED" if result['is_threat'] else "✅ ALLOWED"
        print(f"{name:<20} {status}")
        print(f"  Details: {result['threat_type']}")
        print(f"  Confidence: {result['confidence']:.1%}\n")

if __name__ == "__main__":
    basic_threat_demo()