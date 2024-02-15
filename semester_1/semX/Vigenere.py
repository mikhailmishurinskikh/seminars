class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    
    def __init__(self, keyword):
        self.alphaindex = {ch: index for index, ch in enumerate(self.alphabet)}
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]
        
    def caesar(self, letter, shift):
        if letter in self.alphaindex:  # строчная буква
            index = (self.alphaindex[letter] + shift)%len(self.alphabet)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # заглавная буква
            cipherletter = self.caesar(letter.lower(), shift).upper()
        else:
            cipherletter = letter
        return cipherletter
    
    def encode(self, line):
        ciphertext = []
        for i, letter in enumerate(line):
            shift = self.key[i % len(self.key)]
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter)
            
        return ''.join(ciphertext)
    def decode(self, line):
        decoded_text = []
        for i, letter in enumerate(line):           
            shift = self.key[i % len(self.key)]
            decodedletter = self.caesar(letter, 33 - shift)
            decoded_text.append(decodedletter)
        return ''.join(decoded_text)
    
    
keyword = input('keyword=')
cipher = Vigenere(keyword)

with open('Vigenere.txt', 'a+') as file:
    while 1:
        line = input()
        if line == '.': break
        true_line = ''
        for i in list(line):
            if i != ' ': true_line += i
        file.write(f'{cipher.decode(true_line)}\n')
