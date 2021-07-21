from typing import OrderedDict
from question_1 import odds
word = 'LuxPMsoft'
new_word = ''
for i in range(8):
    new_word += word[i]
    new_word += str(odds[-i-1])
new_word += word[-1]
print(new_word)
# print('L39u37x35P33M31s29o27f25t' == 'L39u37x35P33M31s29o27f25t
# ')
