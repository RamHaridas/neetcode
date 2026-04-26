# openssl rsa -in server.key -noout -text

from cryptography.hazmat.primitives import serialization


def decrypt_message(cipher:str):
    cipher = int(cipher)
    print(f"Cipher: {cipher}\n")
    with open("server.key", "rb") as key_file:
        key = serialization.load_pem_private_key(key_file.read(), password=None)
    
    private_numbers = key.private_numbers()
    public_numbers = private_numbers.public_numbers
    
    # Decryption requires the PRIVATE exponent (d), not the public exponent (e)!
    d = private_numbers.d
    modulo = public_numbers.n
    
    print(f"Private Exponent (d):\n{d}\n")
    print(f"Modulo (n):\n{modulo}\n")

    integer_value = pow(cipher, d, modulo)

    byte_length = (integer_value.bit_length() + 7) // 8
    byte_array = integer_value.to_bytes(byte_length, byteorder='big')
    text_string = byte_array.decode("utf-8")

    print(f"Decrypted message: {text_string}")
    


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cipher", help="Cipher to decrypt")
    args = parser.parse_args()
    decrypt_message(args.cipher)