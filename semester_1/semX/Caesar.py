class Caesar:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, key):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
            self._decode = {x: y for x, y in zip(self._encode.values(), self._encode.keys())}

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])


key = int(input('Enter the key:'))
cipher = Caesar(key)
with open('Caesar.txt', 'a+') as file:
    while 1:
        line = input()
        if line == '.': break
        file.write(f'{cipher.decode(line)}\n')
