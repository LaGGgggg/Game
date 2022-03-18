class EnemyCreature:

    def __init__(self, health, damage, ranged_damage, close_fight_radius, ranged_combat_radius, moving_speed,
                 healing_power, max_health):
        self.health = health
        self.damage = damage
        self.close_fight_radius = close_fight_radius
        self.ranged_combat_radius = ranged_combat_radius
        self.ranged_damage = ranged_damage
        self.moving_speed = moving_speed
        self.healing_power = healing_power
        self.max_health = max_health

    def close_fight(self, player_creature):

        player_creature.health -= self.damage

        return player_creature.health, self.damage

    def heal(self):

        if self.health > self.max_health:
            self.health = self.max_health
            return self.health, self.max_health

        else:
            self.health += self.healing_power
            return self.health, self.healing_power

    def ranged_combat(self, player_creature):

        player_creature.health -= self.ranged_damage

        return player_creature.health, self.ranged_damage


Baron = EnemyCreature(11, 1, 1, 1, 1, 1, 1, 10)
Baron_1 = EnemyCreature(11, 1, 1, 1, 1, 1, 1, 10)
Baron_2 = EnemyCreature(11, 1, 1, 1, 1, 1, 1, 10)
Baron_3 = EnemyCreature(11, 1, 1, 1, 1, 1, 1, 10)
Baron_4 = EnemyCreature(11, 1, 1, 1, 1, 1, 1, 10)
Baron_5 = EnemyCreature(11, 1, 1, 1, 1, 1, 1, 10)
Baron_6 = EnemyCreature(11, 1, 1, 1, 1, 1, 1, 10)
Baron_7 = EnemyCreature(11, 1, 1, 1, 1, 1, 1, 10)
Baron_8 = EnemyCreature(11, 1, 1, 1, 1, 1, 1, 10)
Baron_9 = EnemyCreature(11, 1, 1, 1, 1, 1, 1, 10)
Baron_10 = EnemyCreature(11, 1, 1, 1, 1, 1, 1, 10)
Elsa = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_1 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_2 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_3 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_4 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_5 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_6 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_7 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_8 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_9 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Elsa_10 = EnemyCreature(200, 1, 2, 1, 1, 1, 1, 200)
Lucius = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_1 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_2 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_3 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_4 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_5 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_6 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_7 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_8 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_9 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
Lucius_10 = EnemyCreature(100, 10, 0, 2, 0, 2, 20, 100)
enemies_dict_const = {"easy": ["Baron"], "medium": ["Elsa"], "hard": ["Elsa", "Baron", "Lucius"]}
enemies_dict_names = {"Baron": Baron, "Baron 1": Baron_1, "Elsa": Elsa, "Elsa 1": Elsa_1, "Elsa 2": Elsa_2, "Elsa 3": Elsa_3, "Elsa 4": Elsa_4, "Elsa 5": Elsa_5, "Elsa 6": Elsa_6, "Elsa 7": Elsa_7, "Elsa 8": Elsa_8, "Elsa 9": Elsa_9, "Elsa 10": Elsa_10, "Baron 2": Baron_2, "Baron 3": Baron_3, "Baron 4": Baron_4, "Baron 5": Baron_5, "Baron 6": Baron_6, "Baron 7": Baron_7, "Baron 8": Baron_8, "Baron 9": Baron_9, "Baron 10": Baron_10, "Lucius": Lucius, "Lucius 1": Lucius_1, "Lucius 2": Lucius_2, "Lucius 3": Lucius_3, "Lucius 4": Lucius_4, "Lucius 5": Lucius_5, "Lucius 6": Lucius_6, "Lucius 7": Lucius_7, "Lucius 8": Lucius_8, "Lucius 9": Lucius_9, "Lucius 10": Lucius_10}
