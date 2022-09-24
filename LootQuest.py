import random           # for all things RNG

class Monster:
    def __init__(self, type, health):
        self.type = type
        self.health = health
        self.monster_types = [rat, goblin, orc]

    @classmethod    
    def generate_monster(cls):
        monster = Monster()
        monster.type = random.choice(Monster.monster_types)
        if monster.type == "rat":
            monster.health = random.randint(50, 100)
        elif monster.type == "goblin":
            monster.health = random.randint(100, 200)
        elif monster.type == "orc":
            monster.health = random.randint(200, 400)    



def main():
    first_monster = Monster.generate_monster()
    print(first_monster.type)
    print(first_monster.health)

   

if __name__ == "__main__":
    main()
