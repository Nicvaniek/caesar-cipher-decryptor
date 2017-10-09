import pprint

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# message = "2XQM5QN7A10QYUXXU104M0P59146T1R5TM4Q5M0PNQOM4QR7X01661NQ5QQ0NA6TQM7564MXUM0S18Q40YQ06M0P2XQM5QNQ8USUXM06"
# message = "MNYMJWJNFRFYJXYRJXXFLJ" # meetmeatthegatearound4oclock
# message = "kMYM567PQ06M66TQw0U8Q45U6a1Rr4Q614UM567PaU0Se1Y276Q4uOUQ0OQ5U0OQECDH" # IamastudentattheUniversityofPretoriastudyingComputerSciencesince2015
message = "MJQQTYMJWJR3SFRJNXSTYPST1SG3mUJTUQJ"
message_list = list(message)

finals = []
exes = []
jays = []
for x in range(0, len(alphabet)):
    for j in range(0, len(alphabet)):
        temp = message_list[:]
        for k in range(0, len(temp)):
            index = alphabet.index(temp[k])
            if temp[k].isdigit():
                new_index = (index + j) % len(alphabet)
            else:
                new_index = (index + x) % len(alphabet)
            temp[k] = alphabet[new_index]
        result = ''.join(temp)
        # print(result)
        finals.append(result)
        exes.append(x)
        jays.append(j)
# print(len(finals))
letter_frequencies = [
    'th', 'he', 'an', 'in', 'er', 'on', 're', 'ed', 'nd', 'ha', 'at', 'en', 'es', 'of', 'nt', 'ea', 'ti', 'to',
    'io', 'le', 'is', 'ou', 'ar', 'as', 'de', 'rt', 've',
    'ss', 'ee', 'tt', 'ff', 'll', 'mm', 'oo',
    'the', 'and', 'tha', 'ent', 'ion', 'tio', 'for', 'nde', 'has', 'nce', 'tis', 'oft', 'men',
    'e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u',
    'm', 'f', 'p', 'g', 'w', 'y', 'b', 'v', 'k', 'x', 'j', 'q', 'z'
]
scores = {}
for string in finals:
    for thing in letter_frequencies:
        scores[string] = scores.get(string, 0) + string.count(thing) * (len(letter_frequencies) - letter_frequencies.index(thing))

best_effort = max(scores, key=scores.get)
index = finals.index(best_effort)
print("Ciphertext: " + message)
print("Best Guess Plaintext: " + best_effort)
print("alpha key: " + str(len(alphabet) - exes[index]))
print("digit key: " + str(len(alphabet) - jays[index]))
# pprint.pprint(scores)
finals.sort()
pprint.pprint(finals)
print(scores[best_effort])
