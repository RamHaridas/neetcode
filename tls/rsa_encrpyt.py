
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import binascii

def encrypt_hello():
    # 1. Open the certificate file
    print("Reading server.pem...")
    with open("server.pem", "rb") as f:
        pem_data = f.read()

    # Parse the X.509 certificate
    cert = x509.load_pem_x509_certificate(pem_data, default_backend())
    public_key = cert.public_key()

    # Ensure it's actually an RSA key
    if not isinstance(public_key, rsa.RSAPublicKey):
        raise ValueError("The certificate does not contain an RSA public key.")

    # 2. Extract the math variables (e and n)
    public_numbers = public_key.public_numbers()
    e = public_numbers.e
    n = public_numbers.n

    print(f"\n[Extracted Variables]")
    print(f"Exponent (e): {e}")
    print(f"Modulus (n): {n}\n")

    # 3. Convert the word "hello" into an integer (m)
    message = b"hello"
    # Convert bytes to hex, then hex to integer
    m = int(binascii.hexlify(message), 16)
    
    print(f"[Math Preparation]")
    print(f"Message (m): {m}")

    # 4. The RSA Math: c = m^e mod n
    print("\nCalculating c = m^e mod n ...")
    # ** is the exponent operator (m to the power of e)
    # % is the modulo operator (remainder when divided by n)
    c = (m ** e) % n

    print(f"\n[Final Ciphertext]")
    print(f"Ciphertext (c): {c}")

if __name__ == "__main__":
    encrypt_hello()