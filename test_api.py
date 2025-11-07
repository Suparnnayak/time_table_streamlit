"""
Test script to verify Flask API is working correctly
Run this while Flask server is running
"""
import requests
import json

BASE_URL = "http://localhost:5000"

def test_health_endpoint():
    """Test the health check endpoint"""
    print("=" * 50)
    print("Testing Health Endpoint...")
    print("=" * 50)
    
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("✅ Health endpoint is working!")
            return True
        else:
            print("❌ Health endpoint returned an error")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Could not connect to Flask server!")
        print("   Make sure Flask server is running on http://localhost:5000")
        return False
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False

def test_chat_endpoint():
    """Test the chat endpoint"""
    print("\n" + "=" * 50)
    print("Testing Chat Endpoint...")
    print("=" * 50)
    
    test_message = "What is Python programming?"
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/chat",
            json={"message": test_message},
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Test Message: {test_message}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Chat endpoint is working!")
            print(f"Response Preview: {data.get('response', '')[:100]}...")
            print(f"\nFull Response:")
            print(json.dumps(data, indent=2))
            return True
        else:
            print(f"❌ Chat endpoint returned error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Could not connect to Flask server!")
        print("   Make sure Flask server is running on http://localhost:5000")
        return False
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("\n" + "🚀 Flask API Test Suite")
    print("=" * 50)
    print("Make sure Flask server is running before running these tests!")
    print("Run: python app.py")
    print("=" * 50 + "\n")
    
    # Test health endpoint
    health_ok = test_health_endpoint()
    
    if health_ok:
        # Test chat endpoint
        chat_ok = test_chat_endpoint()
        
        # Summary
        print("\n" + "=" * 50)
        print("Test Summary")
        print("=" * 50)
        print(f"Health Endpoint: {'✅ PASS' if health_ok else '❌ FAIL'}")
        print(f"Chat Endpoint: {'✅ PASS' if chat_ok else '❌ FAIL'}")
        
        if health_ok and chat_ok:
            print("\n🎉 All tests passed! Your Flask API is working correctly!")
        else:
            print("\n⚠️  Some tests failed. Check the errors above.")
    else:
        print("\n❌ Health check failed. Make sure Flask server is running!")

if __name__ == "__main__":
    main()

