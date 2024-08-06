class Person:
    def __init__(self, name, nationality, birth, address):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("名前:", self.name)
        print("国籍:", self.nationality)
        print("生年:", self.birth)
        print("住所:", self.address)

person1 = Person("田中太郎", "日本", 1990, "東京都")
person1.show_attributes()

person2 = Person("John Doe", "アメリカ", 1985, "ニューヨーク")
person2.show_attributes()
