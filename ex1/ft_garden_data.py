#!/usr/bin/env python3
class plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def print_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plist: list[plant] = [plant("Rose", 25, 30),
                          plant("Sunflower", 80, 45),
                          plant("Cactus", 15, 120)]
    print("=== Garden Plant Registry ===")
    for p in plist:
        p.print_info()
