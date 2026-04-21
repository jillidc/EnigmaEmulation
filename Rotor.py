class Rotor:
    def __init__(self, wiring, ring_setting):
        self.wiring = [0] * 26
        for i in range(len(wiring)):
            self.wiring[i] = ord(wiring[i]) - ord('A')

        self.inverse_wiring = [0] * 26
        for i in range(26):
            self.inverse_wiring[self.wiring[i]] = i
        self.offset = 0
        self.ring_setting = ring_setting

    def encode(self, letter):
        return (self.wiring[(letter + self.offset) % 26] - self.offset) % 26
    
    def reverse_encode(self, letter):
        return (self.inverse_wiring[(letter + self.offset) % 26] - self.offset) % 26
    
    def step(self):
        self.offset += 1

wiring1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
wiring2 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
wiring3 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
reflect = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

def letter(index):
    return chr(index+ord('A'))

Rotor1 = Rotor(wiring1, 0)
Rotor2 = Rotor(wiring2, 0)
Rotor3 = Rotor(wiring3, 1)
Reflector = Rotor(reflect, 0)
for i in range(1):
    Rotor3.step()
    char = Rotor3.encode(0)
    print(letter(char))
    char = Rotor2.encode(char)
    char = Rotor1.encode(char)
    char = Reflector.encode(char)
    char = Rotor1.reverse_encode(char)
    char = Rotor2.reverse_encode(char)
    char = Rotor3.reverse_encode(char)
    print(letter(char))
    # print(letter(Rotor1.reverse_encode(10)))
print("-----------")
# for i in range(26):
#     print("{0} encodes to {1}, reverse encodes to {2}".format(letter(i), letter(Rotor1.encode(i)), letter(Rotor1.reverse_encode(Rotor1.encode(i)))))

# Rotor1.step()
# print("---------------------")
# for i in range(26):
#     print("{0} encodes to {1}, reverse encodes to {2}".format(letter(i), letter(Rotor1.encode(i)), letter(Rotor1.reverse_encode(Rotor1.encode(i)))))