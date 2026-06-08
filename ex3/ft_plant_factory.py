#!/usr/bin/env python3
class plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def print_info(self) -> None:
        print(f"{self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    plist: list[plant] = [
            plant("Rose", 25, 30),
            plant("Oak", 200, 356),
            plant("Cactus", 5, 90),
            plant("Sunflower", 80, 45),
            plant("Fern", 15, 120)]
    total: int = 0
    print("=== Plant Factory Output ===")
    for p in plist:
        print("Created: ", end="")
        p.print_info()
        total += 1
    print(f"\nTotal plants created: {total}")
