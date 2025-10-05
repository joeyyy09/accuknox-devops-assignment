import requests
import sys

def check_app_health(url):
    """Checks the health of an application by its URL."""
    try:
        # Send a GET request to the URL with a 5-second timeout
        response = requests.get(url, timeout=5)
        
        # Check if the status code is 200 (OK)
        if response.status_code == 200:
            print(f"✅ Application at '{url}' is UP.")
            print(f"   Status Code: {response.status_code}")
        else:
            # Any other status code indicates a potential issue
            print(f"⚠️ Application at '{url}' may be DOWN or has an issue.")
            print(f"   Status Code: {response.status_code}")
            
    except requests.ConnectionError:
        # Handle cases where the server is not reachable
        print(f"❌ Application at '{url}' is DOWN. Connection failed.")
    except requests.Timeout:
        # Handle cases where the request times out
        print(f"❌ Application at '{url}' is DOWN. Request timed out.")
    except requests.RequestException as e:
        # Handle any other request-related errors
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    # Check if a URL was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python3 health_checker.py <URL>")
        # Use a default URL if none is provided
        target_url = "https://www.google.com"
        print(f"\nNo URL provided. Checking default: {target_url}")
    else:
        target_url = sys.argv[1]

    check_app_health(target_url)