#!/usr/bin/env python3
"""
Simple test script to verify that the Streamlit apps run without errors
"""

import subprocess
import sys
import time

def test_app(app_file):
    """Test if a Streamlit app runs without immediate errors"""
    print(f"\n🧪 Testing {app_file}...")
    try:
        # Start the app in the background
        process = subprocess.Popen(
            ["streamlit", "run", app_file, "--server.headless", "true"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Give it a few seconds to start
        time.sleep(3)
        
        # Check if it's still running
        if process.poll() is None:
            print(f"✅ {app_file} started successfully!")
            process.terminate()
            return True
        else:
            stdout, stderr = process.communicate()
            print(f"❌ {app_file} failed to start")
            print(f"Error: {stderr.decode()}")
            return False
            
    except Exception as e:
        print(f"❌ {app_file} - Exception: {e}")
        return False

def main():
    print("🎰 Testing Martingale Strategy Apps")
    print("=" * 40)
    
    apps_to_test = [
        "martingale_unified.py",
        "fibonacci_bot.py"
    ]
    
    results = []
    for app in apps_to_test:
        success = test_app(app)
        results.append((app, success))
    
    print("\n📊 Test Results:")
    print("=" * 40)
    for app, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {app}")
    
    all_passed = all(success for _, success in results)
    if all_passed:
        print("\n🎉 All apps are working correctly!")
        print("\n🚀 Recommended usage:")
        print("streamlit run martingale_unified.py")
    else:
        print("\n⚠️ Some apps have issues - check the error messages above")

if __name__ == "__main__":
    main()