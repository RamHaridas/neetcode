def encode(strs):
    encoded_text = ""
    for s in strs:
        temp_enc = f"{len(s)}\n{s};"
        encoded_text += temp_enc
    return encoded_text

def decode(s):
    strlist = s.split(";")
    strlist.pop()
    decoded = list()
    for s in strlist:
        s_split = s.split("\n")
        if s_split[0] == 0:
            decoded.append('')
        else:
            decoded.append(s_split[1])
    return decoded



Input = ["ram","loves","you"]
Input = ["we","say",":","yes","!@#$%^&*()"]
res = encode(Input)
print(f"Encoded: {res}")
res = decode(res)
print(f"Decoded: {res}")
