#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        self.height += 1
        print(f"{self.name} is blooming beautifully!")

    def print_flower(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, ", end="")
        print(f"{self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        shade: float = self.height * self.age / self.trunk_diameter
        print(f"{self.name} provides {shade} square meters of shade")

    def print_tree(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, ", end="")
        print(f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def print_vegetable(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, ", end="")
        print(f"{self.age} days, {self.harvest_season} harvest")
        print(self.nutritional_value, "\n")


if __name__ == "__main__":
    flower1: Flower = Flower("Rose", 25, 30, "red")
    flower2: Flower = Flower("Tulip", 10, 15, "pink")
    tree1: Tree = Tree("Oak", 500, 1825, 50)
    tree2: Tree = Tree("Olive", 550, 2798, 100)
    vegetable1: Vegetable = Vegetable("Tomato", 80, 90, "summer",
                                      "Tomato is rich in vitamin C")
    vegetable2: Vegetable = Vegetable("Carrot", 70, 30, "summer",
                                      "Carrot is rich in vitamin A")
    print("=== Garden Plant Types ===\n")
    flower1.print_flower()
    flower1.bloom()
    flower2.print_flower()
    flower2.bloom()
    print()
    tree1.print_tree()
    tree1.produce_shade()
    tree2.print_tree()
    tree2.produce_shade()
    print()
    vegetable1.print_vegetable()
    vegetable2.print_vegetable()
