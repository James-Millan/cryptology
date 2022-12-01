import subprocess
import itertools

correct_ciphertext = "5a1c0f72262c9030e1b00c2d54c0613ed3eff00d0bb7d4494f1bcb43149a25ff31961240ea892fcc5b04f9c93a83606c77d47f23879023200bf7ec6a62e1484dfcefc5848a37c132ff060c80b959a845f55aabeb80be12040c3f3a5a3c432323"

current_answer = ""
answer_found = False
correct_plaintext = ""
initial_plaintext = "It is one of the blessings of old friends that you can afford to be stupid with "
message = initial_plaintext
# alphabet = "them."
alphabet = "abcdefghijklmnopqrstuvwxyz."
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



