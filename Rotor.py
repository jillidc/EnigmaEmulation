from util import *
import json

class Rotor:
    def __init__(self, wiring, ring_setting, notch_letters, next_rotor):
        self.wiring = [0] * 26
        for i in range(len(wiring)):
            self.wiring[i] = num(wiring[i])
        self.inverse_wiring = [0] * 26
        for i in range(26):
            self.inverse_wiring[self.wiring[i]] = i

        self.notch_letters = []
        for letter in notch_letters:
            self.notch_letters.append(num(letter))

        self.offset = 0
        self.ring_setting = ring_setting
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
        if self.offset in self.notch_letters and self.next_rotor != None:
            self.next_rotor.step()
        self.offset = (self.offset + 1) % 26

rotorNum = ["III", "III", "VIII"]
reflectorName = "UKW-B"
ringSettings = [0, 0, 0]

with open("wirings.json") as file:
    data = json.load(file)
    rotors = data["rotors"]
    reflectors = data["reflectors"]

    Rotor1 = Rotor(rotors[rotorNum[0]]["wiring"], ringSettings[0], rotors[rotorNum[0]]["notch"], None)
    Rotor2 = Rotor(rotors[rotorNum[1]]["wiring"], ringSettings[1], rotors[rotorNum[1]]["notch"], Rotor1)
    Rotor3 = Rotor(rotors[rotorNum[2]]["wiring"], ringSettings[2], rotors[rotorNum[2]]["notch"], Rotor2)

    Reflector = Rotor(reflectors[reflectorName]["wiring"], 0, " ", None)


text = "the quick brown fox jumped over the lazy dog the quick brown fox jumped over the lazy dog"
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