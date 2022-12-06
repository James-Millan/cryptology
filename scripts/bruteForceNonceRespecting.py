import subprocess
import itertools
import wordlist

current_answer = ""
answer_found = False
correct_plaintext = "terminated without changing anything"
initial_plaintext = "The enemy knows "
message = initial_plaintext
ciphertext = "1a3d3c5d67daf2707ef74e38478d7fbf0c7648fae3e29264b147bfc5fdf00205"
c_block1 = "1a3d3c5d67daf2707ef74e38478d7fbf"
c_block2 = "0c7648fae3e29264b147bfc5fdf00205"
output = "ea486e17628aef1d009930c1b91f3ea41881692d1ee52ed63e73d70e1a8d00434fc2313a8e691c43046dc749153f08b7"
alphabet = "abcdefghijklmnopqrstuvwxyz "

message = initial_plaintext
nonce = ""
with open("../publics/n2_cbc.txt") as f:
    nonce = f.readline().strip()

words = []
with open("../words.txt") as w:
    for line in w:
        words.append(line.strip())



m = b'the system.'
l = 16 - len(m)
for i in range(l):
    m = m + l.to_bytes(1, "big")
print(m.hex())

expected_value = subprocess.run(["../cbc", c_block2, c_block1 ], stdout=subprocess.PIPE).stdout.decode()
actual_value = subprocess.run(["../cbc", c_block1, m], stdout=subprocess.PIPE).stdout.decode()[:32]
#print(expected_value)
print(actual_value)
print(c_block2)

for k in range(10):
    if answer_found:
        break
    for v in itertools.permutations(words, k):
        message = ""
        if answer_found:
            break
        message = " ".join(v)
        message = message + "."
        if message == "the system.":
            answer_found = True
            break
        current_answer = subprocess.run(["../cbc", message, nonce], stdout=subprocess.PIPE).stdout.decode()[:32]
        print(message, current_answer)
        if c_block2 == current_answer:
            correct_plaintext = initial_plaintext + message
            answer_found = True
            print("WE HAVE CRACKED IT!\n"*5)
            break

print(correct_plaintext)