from character import Character


class Warrior(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        # Warriors have more health and strength, less mana and intelligence
        self.max_health = 150
        self.health = 150
        self.max_mana = 30
        self.mana = 30
        self.strength = 15
        self.intelligence = 5
        self.defense = 8

    def level_up(self):
        result = super().level_up()
        # Extra strength bonus for warriors
        self.strength += 2
        self.max_health += 10  # Extra health for warriors
        self.health = self.max_health
        return result

    def attack(self, target):
        # Warriors have a stronger basic attack
        damage = self.strength * 1.2
        damage_dealt = target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")
        return damage_dealt
