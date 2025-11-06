# File: safe_demo_data.py
# Generates fake data for demonstrations - no real system access
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

class SafeDemoData:
    def __init__(self):
        self.demo_logs = []
    
    def generate_fake_security_logs(self, days=7):
        """Generate completely fake security logs for demo"""
        print("📊 Generating FAKE demo data...")
        
        log_types = ['login_success', 'login_failed', 'file_access', 'network_connection']
        users = ['admin', 'user1', 'user2', 'service_account']
        
        logs = []
        base_time = datetime.now() - timedelta(days=days)
        
        for i in range(1000):  # Generate 1000 fake log entries
            log_time = base_time + timedelta(minutes=i*10)
            
            log_entry = {
                'timestamp': log_time,
                'event_type': np.random.choice(log_types),
                'user': np.random.choice(users),
                'source_ip': f"192.168.1.{np.random.randint(1, 50)}",
                'details': 'DEMO_DATA - Not real',
                'is_malicious': False
            }
            
            # Make some entries suspicious for demo purposes
            if np.random.random() < 0.05:  # 5% are "suspicious"
                log_entry['is_malicious'] = True
                log_entry['details'] = 'SUSPICIOUS_ACTIVITY - DEMO'
            
            logs.append(log_entry)
        
        return pd.DataFrame(logs)
    
    def generate_network_traffic(self):
        """Generate fake network traffic patterns"""
        traffic_patterns = {
            'normal': {'packets_sec': (50, 200), 'ports': (10, 30), 'data_mb': (100, 1000)},
            'suspicious': {'packets_sec': (500, 1500), 'ports': (40, 80), 'data_mb': (5000, 15000)},
            'malicious': {'packets_sec': (1500, 3000), 'ports': (70, 100), 'data_mb': (15000, 30000)}
        }
        
        return traffic_patterns

# Usage
demo_data = SafeDemoData()
fake_logs = demo_data.generate_fake_security_logs()
print(f"📁 Generated {len(fake_logs)} FAKE log entries for demo")
print("🔒 No real data was accessed or collected")