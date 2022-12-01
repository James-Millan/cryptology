import subprocess

correct_ciphertext = "1a3d3c5d67daf2707ef74e38478d7fbf0c7648fae3e29264b147bfc5fdf00205"
current_answer = ""
answer_found = False
correct_plaintext = ""
initial_plaintext = "It is one of the blessings of old friends that you can afford to be stupid with "
message = initial_plaintext

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'z', 'y', '.']

subsets = itertools.combinations(alphabet, 16)

while not answer_found:
    message = initial_plaintext
    for i in range(subsets):
        message = initial_plaintext + subsets[i]
        number_to_pad = 96 - len(message)
        hex = number_to_pad.hex()
        for j in range(number_to_pad):
            message = message + str(hex).fromhex()
        current_answer = subprocess.run(["../cbc", "../publics/n1_cbc.txt", message])
        if correct_ciphertext == current_answer:
            correct_plaintext = message
            answer_found = True
            break;









