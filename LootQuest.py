import random           # for all things RNG

class Monster:
    def __init__(self, type, health):
        self.type = type
        self.health = health
        self.monster_types = [rat, goblin, orc]

    @classmethod    
    def generate_monster(cls):
        type = random.choice(monster_types)
        if type == "rat":
            health = random.randint(50, 100)
        elif type == "goblin":
            health = random.randint(100, 200)
        elif type == "orc":
            health = random.randint(200, 400)
        return cls(type, health) 



def main():
    first_monster = Monster.generate_monster()
    print(first_monster.type)
    print(first_monster.health)

   

if __name__ == "__main__":
    main()
