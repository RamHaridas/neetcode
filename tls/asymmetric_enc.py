
def calculate_next_chr(char: str, key: int) -> str:
    pos = ord(char) - ord("a")
    new_pos = (pos + key) % 26
    return chr(new_pos + ord("a"))

def encrypt(input:str, key:int) -> str:
    '''
    Accepts an input string and replaces each char with the char at +5 pos
    For example: ram --> wfr
    '''
    input = input.lower()
    cipher = []
    for i in input:
        cipher.append(calculate_next_chr(i, key))
    return "".join(cipher)

def decrypt(input:str, key:int) -> str:
    '''
    Accepts an input string and replaces each char with the char at +21 pos
    For example: wfr --> ram
    '''
    input = input.lower()
    plain = []
    for i in input:
        plain.append(calculate_next_chr(i, key))
    return "".join(plain)

plain = "ram"
enc_key = 5
dec_key = 21
print(f"PLAIN: {plain}")
cipher = encrypt(plain, enc_key)
print(f"CIPHER: {cipher}")
plain = decrypt(cipher, dec_key)
print(f"DECRYPTED: {plain}")
