class Nigiri:
    def __init__(self):
        pass

    def show_attributes(self):
        print("握り寿司")

class Katsuo(Nigiri):
    def __init__(self):
        super().__init__()
        self.topping = "生姜とねぎ"
        self.price = 100

    def show_attributes(self):
        super().show_attributes()
        print(f"トッピング: {self.topping}")
        print(f"価格: {self.price}円")

katsuo = Katsuo()
katsuo.show_attributes()
