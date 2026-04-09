
def calculate_next_chr(char: str, key: int, op: str) -> str:
    pos = ord(char) - ord("a")
    if op.lower() == "add":
        new_pos = (pos + key) % 26
    else:
        new_pos = (pos - key) % 26
    return chr(new_pos + ord("a"))

def encrypt(input:str, key:int) -> str:
    '''
    Accepts an input string and replaces each char with the char at +5 pos
    For example: ram --> wfr
    '''
    input = input.lower()
    cipher = []
    for i in input:
        cipher.append(calculate_next_chr(i, key, "add"))
    return "".join(cipher)

def decrypt(input:str, key:int) -> str:
    '''
    Accepts an input string and replaces each char with the char at -5 pos
    For example: wfr --> ram
    '''
    input = input.lower()
    plain = []
    for i in input:
        plain.append(calculate_next_chr(i, key, "sub"))
    return "".join(plain)

plain = "ram"
symmetric_key = 5
print(f"PLAIN: {plain}")
cipher = encrypt(plain, symmetric_key)
print(f"CIPHER: {cipher}")
plain = decrypt(cipher, symmetric_key)
print(f"DECRYPTED: {plain}")