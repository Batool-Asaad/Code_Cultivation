#!/usr/bin/env python3
class plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.__name: str = name
        self.__height: float = height
        self.__age: int = age

    def print_info(self) -> None:
        print(f"{self.__name}: ({self.__height}cm, {self.__age} days)")

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_name(self, n: str) -> None:
        self.__name = n

    def set_height(self, h: float) -> None:
        if h >= 0:
            self.__height = h
            print(f"Height updated: {h}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected\n")

    def set_age(self, a: int) -> None:
        if a >= 0:
            self.__age = a
            print(f"Age updated: {a} days [OK]")
        else:
            print(f"\nInvalid operation attempted: age {a} days [REJECTED]")
            print("Security: Negative age rejected\n")


def print_current_info(p: plant) -> None:
    print("Current plant: ", end="")
    print(f"{p.get_name()} ({p.get_height()}cm, {p.get_age()} days)")


if __name__ == "__main__":
    print("=== Garden Security System ==")
    name: str = "Rose"
    height: float = 20
    age: int = 28
    p: plant = plant(name, height, age)
    print(f"Plant created: {p.get_name()}")
    p.set_height(25)
    p.set_age(30)
    print_current_info(p)
    p.set_height(-30)
    p.set_age(-31)
    print_current_info(p)
