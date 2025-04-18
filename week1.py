# Pet class
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        print(f"{self.name} is eating... 🍽️")
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)

    def sleep(self):
        print(f"{self.name} is sleeping... 😴")
        self.energy = min(self.energy + 5, 10)

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play. 🥱")
            return
        print(f"{self.name} is playing! 🐾")
        self.energy = max(self.energy - 2, 0)
        self.happiness = min(self.happiness + 2, 10)
        self.hunger = min(self.hunger + 1, 10)

    def train(self, trick):
        print(f"{self.name} learned a new trick: {trick}! 🎓")
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 1, 10)

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")

    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Tricks: {self.tricks if self.tricks else 'None'}")


# Main function
def main():
    my_pet = Pet("Max")
    print(f"Creating pet: {my_pet.name} 🐶")

    my_pet.eat()
    my_pet.play()
    my_pet.sleep()

    my_pet.train("roll over")
    my_pet.train("play dead")

    my_pet.get_status()
    my_pet.show_tricks()


if __name__ == "__main__":
    main()

