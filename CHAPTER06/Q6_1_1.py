class cat:
    def __init__(self, cry="ニャー", legs=4, is_animal=True):
        self.cry = cry
        self.legs = legs
        self.is_animal = is_animal

neko = cat()

print(neko.cry)
print(neko.legs)
print(neko.is_animal)
