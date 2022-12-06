from Crypto.Cipher import AES


message = "22222222222222222222222222222222"
ciphertext = "c35129a775ddcf8396fade0573bccfb7"

key = "password"
aes = AES.new(key, AES.MODE_EBC)

k1_list = []
k2_list = []
for i in range(65537):
    aes = AES.new(i, AES.MODE_EBC)
    k1_cipher = aes.encrypt(message)
    k1_list.append(k1_cipher)

for j in range(65537):
    aes = AES.new(j, AES.MODE_EBC)
    k2_cipher = aes.decrypt(ciphertext)
    k2_list.append(k2_cipher)
    if k2_cipher in k1_list:
        candidate_key_1 = k1_list[k2_cipher].index()
        candidate_key_2 = j
        aes1 = AES.new(candidate_key_1, AES.MODE_EBC)
        if aes.encrypt(aes1.encrypt(message)) == ciphertext:
            print("key 1 is:- " + str(candidate_key_1))
            print("key 2 is:- " + str(candidate_key_2))