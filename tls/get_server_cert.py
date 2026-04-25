# This script is for educational purposes only
# https://badssl.com/ can be used for testing this script
# It will generate server.pem file and save it
# Use `openssl x509 -in server.pem -text -noout` to read the cert
# For RSA, look for modu
import ssl
import argparse
import sys
from urllib.parse import urlparse

def get_server_cert(url, output_file=None):
    # Parse the URL to get the hostname and port
    parsed_url = urlparse(url)
    
    # If the user didn't provide a scheme, urlparse might parse it incorrectly
    if not parsed_url.scheme:
        url = 'https://' + url
        parsed_url = urlparse(url)
        
    hostname = parsed_url.hostname
    port = parsed_url.port or 443

    if not hostname:
        print(f"Error: Could not extract hostname from URL: {url}")
        sys.exit(1)

    print(f"Connecting to {hostname}:{port}...")

    try:
        # Download the full certificate in PEM format
        pem_cert = ssl.get_server_certificate((hostname, port))
        
        print("\n--- Server Certificate ---")
        print(pem_cert.strip())
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(pem_cert)
            print(f"\n[+] Certificate successfully saved to {output_file}")
            
        return pem_cert

    except Exception as e:
        print(f"Error retrieving certificate: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a server's certificate from a given URL.")
    parser.add_argument("url", help="The URL or hostname of the server (e.g., https://example.com or example.com)")
    parser.add_argument("-o", "--output", help="File path to save the certificate to.", default="server.pem")
    args = parser.parse_args()
    
    get_server_cert(args.url, args.output)
