class Rotor:
    def __init__(self, wiring, ring_setting, notch_letter, next_rotor):
        self.wiring = [0] * 26
        for i in range(len(wiring)):
            self.wiring[i] = num(wiring[i])

        self.inverse_wiring = [0] * 26
        for i in range(26):
            self.inverse_wiring[self.wiring[i]] = i
        self.offset = 0
        self.ring_setting = ring_setting
        self.notch_letter = num(notch_letter)
        self.next_rotor = next_rotor

    #Takes letter as number input
    def encode(self, letter):
        step = (letter + self.offset - self.ring_setting) % 26 # Input to wiring array
        wired = self.wiring[step] # Output of wiring array
        return (wired - self.offset + self.ring_setting) % 26 # Undo offset to get input to next rotor
    
    def reverse_encode(self, letter):
        step = (letter + self.offset - self.ring_setting) % 26
        wired = self.inverse_wiring[step]
        return (wired - self.offset + self.ring_setting) % 26
    
    def step(self):
        if self.offset == self.notch_letter and self.next_rotor != None:
            self.next_rotor.step()
        self.offset = (self.offset + 1) % 26

    
wiring1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
wiring2 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
wiring3 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
reflect = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

def letter(index):
    return chr(index+ord('A'))

def is_letter(char):
    return (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z')

def num(letter):
    if letter >= 'A' and letter <= 'Z':
        return ord(letter) - ord('A')
    else:
        return ord(letter) - ord('a')

Rotor1 = Rotor(wiring1, 6, "Q", None)
Rotor2 = Rotor(wiring2, 3, "Q", Rotor1)
Rotor3 = Rotor(wiring3, 7, "Q", Rotor2)
Reflector = Rotor(reflect, 0, "Q", None)

text = "We will advance tomorrow. Heil Shitler"
output = ""
n = 0

for char in text:
    if not is_letter(char):
        continue
    char = num(char)
    Rotor3.step()
    char = Rotor3.encode(char)
    char = Rotor2.encode(char)
    char = Rotor1.encode(char)
    char = Reflector.encode(char)
    char = Rotor1.reverse_encode(char)
    char = Rotor2.reverse_encode(char)
    char = Rotor3.reverse_encode(char)
    output += letter(char)
    n += 1
    if n % 5 == 0:
        output += " "
print(output)