import random           # for all things RNG

class Monster:
    def __init__(self, monster_type, monster_health):
        self.monster_type = monster_type
        self.monster_health = monster_health
        
    @classmethod    
    def generate_monster(cls):
        monster_types = ["rat", "goblin", "orc"]
        monster_type = random.choice(monster_types)
        if monster_type == "rat":
            monster_health = random.randint(50, 100)
        elif monster_type == "goblin":
            monster_health = random.randint(100, 200)
        elif monster_type == "orc":
            monster_health = random.randint(200, 400)
        return cls(monster_type, monster_health) 



def main():
    first_monster = Monster.generate_monster()
    print(first_monster.monster_type)
    print(first_monster.monster_health)

   

if __name__ == "__main__":
    main()
