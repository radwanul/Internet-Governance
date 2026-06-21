import requests
from urllib.parse import urlparse
import re

# Known tracker and analytics domains
KNOWN_TRACKERS = {
    "google-analytics.com": "Google Analytics",
    "analytics.google.com": "Google Analytics",
    "googletagmanager.com": "Google Tag Manager",
    "facebook.com": "Facebook Tracker",
    "connect.facebook.net": "Facebook Connect",
    "doubleclick.net": "DoubleClick (Google Ads)",
    "hotjar.com": "Hotjar",
    "segment.com": "Segment Analytics",
    "mixpanel.com": "Mixpanel Analytics",
    "amplitude.com": "Amplitude Analytics",
    "intercom.io": "Intercom",
    "zendesk.com": "Zendesk",
    "optimizely.com": "Optimizely",
    "crazyegg.com": "Crazy Egg",
    "drift.com": "Drift Chat",
    "twitter.com": "Twitter",
    "cdn.jsdelivr.net": "Third-party CDN",
    "cloudflare.com": "Cloudflare",
}

def normalize_url(url):
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url

def parse_cookie(cookie_str):
    """Parse cookie string and extract attributes"""
    parts = [p.strip() for p in cookie_str.split(";")]
    cookie_name_value = parts[0]
    attributes = {}
    
    for part in parts[1:]:
        if "=" in part:
            key, value = part.split("=", 1)
            attributes[key.strip().lower()] = value.strip()
        else:
            attributes[part.strip().lower()] = True
    
    return cookie_name_value, attributes

def detect_trackers(url):
    """Detect trackers and cookies by fetching the website"""
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    print("\n=================================")
    print(" WEBSITE COOKIE & TRACKER ANALYZER")
    print("=================================")
    
    print(f"\nTarget Website: {domain}")
    print(f"Secure Connection (HTTPS): {'Yes' if parsed_url.scheme == 'https' else 'No'}")
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        
        # Extract cookies from response headers
        print("\n" + "="*40)
        print("COOKIES DETECTED:")
        print("="*40)
        
        cookies_found = False
        if "Set-Cookie" in response.headers:
            for cookie in response.headers.getlist("Set-Cookie"):
                cookies_found = True
                cookie_name_value, attributes = parse_cookie(cookie)
                print(f"\n📍 {cookie_name_value}")
                for key, value in attributes.items():
                    print(f"   └─ {key}: {value}")
        
        if not cookies_found:
            print("No Set-Cookie headers found in initial response.")
        
        # Detect trackers by analyzing page content and links
        print("\n" + "="*40)
        print("TRACKERS DETECTED:")
        print("="*40)
        
        detected_trackers = set()
        
        # Check response headers for tracker domains
        for header_value in response.headers.values():
            if isinstance(header_value, str):
                for tracker_domain, tracker_name in KNOWN_TRACKERS.items():
                    if tracker_domain in header_value.lower():
                        detected_trackers.add((tracker_name, tracker_domain))
        
        # Analyze HTML content for tracker scripts
        try:
            html = response.text
            # Look for common tracker patterns in scripts
            for tracker_domain, tracker_name in KNOWN_TRACKERS.items():
                if tracker_domain in html.lower():
                    detected_trackers.add((tracker_name, tracker_domain))
        except:
            pass
        
        if detected_trackers:
            for i, (tracker_name, tracker_domain) in enumerate(sorted(detected_trackers), 1):
                print(f"{i}. {tracker_name} ({tracker_domain})")
        else:
            print("No known trackers detected in this initial scan.")
        
        print("\n" + "="*40)
        print("PRIVACY ANALYSIS:")
        print("="*40)
        print(f"Total Cookies Set: {len(response.headers.getlist('Set-Cookie')) if 'Set-Cookie' in response.headers else 0}")
        print(f"Total Trackers Detected: {len(detected_trackers)}")
        
        if detected_trackers:
            print("\n⚠️  Privacy Recommendations:")
            print("- This website uses tracking services")
            print("- Consider blocking third-party trackers in browser settings")
            print("- Review and manage cookie preferences")
            print("- Use privacy-focused browser extensions (uBlock Origin, Privacy Badger)")
        else:
            print("\n✓ No major tracking services detected")
        
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error fetching website: {e}")

# Main execution
url = input("Enter website URL: ").strip()
normalized_url = normalize_url(url)
detect_trackers(normalized_url)