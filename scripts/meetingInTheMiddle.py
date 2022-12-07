from Crypto.Cipher import AES

message = bytes.fromhex("0123456789abcdef0123456789abcdef")
ciphertext = bytes.fromhex("1a7f3e8d067c8a281cac681b815333a7")
print(ciphertext)

c1_list = set()
k1_list = {}
k2_list = {}
c2_list = set()
for i in range(0, 65537):
    hexKey = i.to_bytes(32, 'big')
    aesE = AES.new(hexKey, AES.MODE_ECB)
    k1_cipher = aesE.encrypt(message)
    c1_list.add(k1_cipher)
    k1_list[k1_cipher] = i

for j in range(0, 65537):
    hexKey = j.to_bytes(32, 'big')
    aesD = AES.new(hexKey, AES.MODE_ECB)
    k2_cipher = aesD.decrypt(ciphertext)
    c2_list.add(k2_cipher)
    k2_list[k2_cipher] = hexKey
    if k2_cipher in c1_list:
        print("FOUND "*5)
        candidate_key_1 = k1_list[k2_cipher]
        candidate_key_2 = j
        print("key 1 is:- " + str(candidate_key_1))
        print("key 2 is:- " + str(candidate_key_2))
