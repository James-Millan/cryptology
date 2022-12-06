import subprocess
import itertools
import wordlist

current_answer = ""
answer_found = False
correct_plaintext = ""
initial_plaintext = "The enemy knows "
message = initial_plaintext
ciphertext = "1a3d3c5d67daf2707ef74e38478d7fbf0c7648fae3e29264b147bfc5fdf00205"
c_block1 = "1a3d3c5d67daf2707ef74e38478d7fbf"
c_block2 = "0c7648fae3e29264b147bfc5fdf00205"
output = "ea486e17628aef1d009930c1b91f3ea41881692d1ee52ed63e73d70e1a8d00434fc2313a8e691c43046dc749153f08b7"
alphabet = "abcdefghijklmnopqrstuvwxyz "
words = wordlist.Generator(alphabet).generate(2,6)
message = initial_plaintext
nonce = ""
with open("../publics/n2_cbc.txt") as f:
    nonce = f.readline().strip()


expected_value = subprocess.run(["../cbc", c_block2, c_block1 ], stdout=subprocess.PIPE).stdout.decode()
print(expected_value)

for k in range(3):
    subsets = itertools.permutations(words, k)
    if answer_found:
        break
    for v in subsets:
        message = ""
        #print(v)
        if answer_found:
            break
        for i in v:
            message = message + i
            message = message + "."
        current_answer = subprocess.run(["../cbc", message, nonce], stdout=subprocess.PIPE).stdout.decode()
        if output == current_answer:
            correct_plaintext = initial_plaintext + message
            answer_found = True
            print("WE HAVE CRACKED IT!\n"*5)
            break

print(correct_plaintext)










# message = "It is one of the blessings of old friends that you can afford to be stupid with them."
# with open("../publics/n1_cbc.txt") as f:
#     nonce = f.readline().strip()
#     print(subprocess.run(["../cbc", nonce, message]))


#6a504d5b09959d3137bea0fd93b1f4b99fc884e8cd7a3
