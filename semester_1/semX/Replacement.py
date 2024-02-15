import random
from frequency import freq_analysys

file = 'encoded_text.txt'
class Monoalphabet:
    alphabet = "аоитевнрлсмкпызфдяшубьчгжхйцюкёщъ"
    
    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)
        lower_decode = {y: x for x, y in zip(self.alphabet, freq_analysys(file))}
        upper_decode = {y.upper(): x.upper() for x, y in zip(self.alphabet, freq_analysys(file))}
        self._decode = lower_decode
        self._decode.update(upper_decode)
        
    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])

p = input('1 for decode\n0 for encode\n')
key = list(Monoalphabet.alphabet)
random.shuffle(key)
cipher = Monoalphabet(key)
if not p:
    line = input()
    while line:
        print(cipher.encode(line))
        line = input()
else:
    with open('Replacement.txt', 'a+') as file:
        while 1:
            line = input()
            if line == '.': break
            file.write(f'{cipher.decode(line)}\n')
