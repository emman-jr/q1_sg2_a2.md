class hero:
    def __init__(self, name, attribute):
        self.name = name
        self.attribute = attribute
        self.hp = 100

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        print(f"{self.name}'s health is now {self.hp}/100!")


heroes = []
user_decision = 1

while user_decision != 3:
    if user_decision == 1:
        name = input("Enter the name of your hero: ")
        attribute = input("Enter an attribute your hero has: ")
        heroes.append(hero(name, attribute))
    elif user_decision == 2:
        if not heroes:
            print("Create a hero first.")
        else:
            for index, hero in enumerate(heroes, start=1):
                print(f"{index}. {hero.name}")

            hero_number = int(input("Who do you want to damage? Enter number: "))
            damage = int(input("Enter damage: "))

            if 1 <= hero_number <= len(heroes):
                heroes[hero_number - 1].take_damage(damage)
            else:
                print("That hero number is not valid.")

    for hero in heroes:
        print(f"{hero.name}, with the attribute {hero.attribute}, has {hero.hp}/100 hp left!")

    user_decision = int(input('''Enter "1" to make another hero
Enter "2" to damage your heroes
Enter "3" to escape program
'''))

        
        
        
