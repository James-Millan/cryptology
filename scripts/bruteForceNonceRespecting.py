import subprocess
import itertools

current_answer = ""
answer_found = False
correct_plaintext = ""
initial_plaintext = "It is one of the blessings of old friends that you can afford to be stupid with "
message = initial_plaintext
# alphabet = "them."
alphabet = "abcdefghijklmnopqrstuvwxyz "
message = initial_plaintext
nonce = ""
with open("../publics/n1_cbc.txt") as f:
    nonce = f.readline().strip()

for k in range(6):
    subsets = itertools.permutations(alphabet, k)
    if answer_found:
        break
    for v in subsets:
        message = initial_plaintext
        #print(v)
        if answer_found:
            break
        for i in v:
            #print(i)
            message = message + i
        # number_to_pad = 96 - len(message)
        # hex_number = hex(number_to_pad)
        # for j in range(number_to_pad):
        #     message = message + str(hex_number)
        print(message)
        #print(subprocess.run(["../cbc", nonce, message]))

        current_answer = subprocess.run(["../cbc", nonce, message], stdout=subprocess.PIPE).stdout.decode()
        if correct_ciphertext == current_answer:
            correct_plaintext = message
            answer_found = True
            print("WE HAVE CRACKED IT!\n"*5)
            break

print(correct_plaintext)









# message = "It is one of the blessings of old friends that you can afford to be stupid with them."
# with open("../publics/n1_cbc.txt") as f:
#     nonce = f.readline().strip()
#     print(subprocess.run(["../cbc", nonce, message]))



