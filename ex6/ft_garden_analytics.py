#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float) -> None:
        self.name: str = name
        self.height: float = height
        self.p_type: str = "regular"

    def grow(self) -> int:
        self.height += 1
        return 1

    def info(self) -> str:
        return f"{self.name}: {self.height}cm"


class Flowering_plant(Plant):
    def __init__(self, name: str, height: float, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.p_type: str = "flowering"

    def info(self) -> str:
        return f"{super().info()}, {self.color} flowers (blooming)"


class Prize_flower(Flowering_plant):
    def __init__(self, name: str, height: float,
                 color: str, points: int) -> None:
        super().__init__(name, height, color)
        self.points: int = points
        self.p_type: str = "prize"

    def info(self) -> str:
        return f"{super().info()}, Prize points: {self.points}"


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list = []
        self.total_growth: int = 0

    def add_plant(self, p: Plant) -> None:
        self.plants += [p]
        print(f"Added {p.name} to {self.owner}’s garden")

    def grow_all(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for p in self.plants:
            print(f"{p.name} grew {p.grow()}cm")
            self.total_growth += 1

    def report(self) -> None:
        total_plants: int = 0
        for p in self.plants:
            total_plants += 1
        print("Plants in garden:")
        for p in self.plants:
            print(p.info())
        print(f"\nPlants added: {total_plants}, ", end="")
        print(f"Total growth: {self.total_growth}cm")

    def score(self) -> float:
        total_height: float = 0
        for p in self.plants:
            total_height += p.height
        return total_height + self.total_growth


class Garden_manager:
    class Garden_stats:
        def __init__(self) -> None:
            self.regular: int = 0
            self.flowering: int = 0
            self.prize: int = 0

    def __init__(self) -> None:
        self.gardens: list = []
        self.owners: list = []
        self.g_count: int = 0
        self.stats = Garden_manager.Garden_stats()

    @classmethod
    def create_garden_network(cls) -> "Garden_manager":
        return cls()

    @staticmethod
    def height_validation_test(h: float) -> bool:
        return h > 100

    def add_garden(self, owner: str) -> None:
        self.gardens += [Garden(owner)]
        self.owners += [owner]
        self.g_count += 1

    def find_garden(self, owner: str) -> int:
        for i in range(self.g_count):
            if self.owners[i] == owner:
                return i
        return -1

    def add_plant(self, owner: str, p: Plant) -> None:
        i: int = self.find_garden(owner)
        if i == -1:
            return
        self.gardens[i].add_plant(p)
        if p.p_type == "regular":
            self.stats.regular += 1
        elif p.p_type == "flowering":
            self.stats.flowering += 1
        elif p.p_type == "prize":
            self.stats.prize += 1

    def grow(self, owner: str) -> None:
        i: int = self.find_garden(owner)
        if i == -1:
            return
        self.gardens[i].grow_all()

    def report(self, owner: str) -> None:
        i: int = self.find_garden(owner)
        if i == -1:
            return
        print(f"\n==={owner}'s Garden Report ===")
        self.gardens[i].report()
        print(f"Plant types: {self.stats.regular} regular, ", end="")
        print(f"{self.stats.flowering} flowering, ", end="")
        print(f"{self.stats.prize} prize flowers")

    def print_score(self) -> None:
        print("Garden scores - ", end="")
        for i in range(self.g_count):
            owner: str = self.owners[i]
            score: float = self.gardens[i].score()
            print(f"{owner}: {score}", end="")
            if i != self.g_count - 1:
                print(", ", end="")
        print()


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    manager = Garden_manager.create_garden_network()
    manager.add_garden("Alice")
    manager.add_garden("Bob")
    manager.add_plant("Alice", Plant("Oak Tree", 100))
    manager.add_plant("Alice", Flowering_plant("Rose", 25, "red"))
    manager.add_plant("Alice", Prize_flower("Sunflower", 50, "yellow", 10))
    manager.grow("Alice")
    manager.report("Alice")
    print()
    i: int = manager.find_garden("Alice")
    total_height: float = 0
    for p in manager.gardens[i].plants:
        total_height += p.height
    print("Height validation test: ",
          Garden_manager.height_validation_test(total_height))
    manager.print_score()
    print("Total gardens managed:", manager.g_count)
