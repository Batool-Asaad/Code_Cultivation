#!/usr/bin/env python3
class plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def print_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def p_grow(self) -> None:
        self.height += 1

    def p_age(self) -> None:
        self.age += 1

    def week_growth(self, before: int, after: int) -> None:
        print(f"Growth this week: +{after - before}cm")


if __name__ == "__main__":
    plist: list[plant] = [plant("Rose", 25, 30),
                          plant("Sunflower", 80, 45),
                          plant("Cactus", 15, 120)]
    print("=== Garden Plant Registry ===")
    week_before: int = {p.name: p.height for p in plist}
    for day in range(1, 71):
        if day % 7 == 1 or day == 1:
            week_before: int = {p.name: p.height for p in plist}
        if day % 7 == 0 or day == 1:
            print(f"=== Day {day} ===")
            for p in plist:
                p.print_info()
                if day % 7 == 0:
                    p.week_growth(week_before[p.name], p.height)
        for p in plist:
            p.p_grow()
            p.p_age()
