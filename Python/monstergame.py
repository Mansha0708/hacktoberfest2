import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

def player_turn(player, monster):
    print(f"\n{player.name}'s turn!")
    action = input("Do you want to (A)ttack or (R)un? ").lower()
    if action == 'a':
        print(f"You attack the {monster.name}!")
        monster.health -= player.attack
        print(f"The {monster.name} has {monster.health} health left.")
    elif action == 'r':
        print("You ran away!")
        return False
    return True

def monster_turn(monster, player):
    print(f"\n{monster.name}'s turn!")
    if monster.is_alive():
        print(f"The {monster.name} attacks you!")
        player.health -= monster.attack
        print(f"You have {player.health} health left.")

def dungeon_adventure():
    print("Welcome to the Dungeon Adventure!")
    player_name = input("Enter your character's name: ")
    player = Character(player_name, health=100, attack=20)

    monsters = [
        Monster("Goblin", health=30, attack=10),
        Monster("Orc", health=50, attack=15),
        Monster("Dragon", health=100, attack=25)
    ]

    while player.is_alive() and monsters:
        monster = random.choice(monsters)
        print(f"\nA wild {monster.name} appears!")

        while monster.is_alive() and player.is_alive():
            if not player_turn(player, monster):
                print("You escaped the battle!")
                break
            monster_turn(monster, player)

        if not monster.is_alive():
            print(f"You defeated the {monster.name}!")
            monsters.remove(monster)

    if player.is_alive():
        print("You have cleared the dungeon! Congratulations!")
    else:
        print("You have been defeated. Game over!")

if __name__ == "__main__":
    dungeon_adventure()
