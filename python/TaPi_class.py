class Vegetables:
    def __init__(self, name, color, root):
        self.name = name
        self.color = color
        self.root = root

    def describe(self):
        root = "root" if self.root else "not root"
        print(f"{self.name} is a {root} vegetable and its color is {self.color}.")

    def is_orange(self):
        return self.color == "orange"


if __name__ == "__main__":
    carrot = Vegetables("carrot", "orange", True)
    cucumber = Vegetables("cucumber", "green", False)

    carrot.describe()
    cucumber.describe()

    print(f"Is carrot an orange vegetable? {carrot.is_orange()}")
    print(f"Is cucumber an orange vegetable? {cucumber.is_orange()}")
