from character import Character


class Rogue(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        # Rogues have more agility, balanced other stats
        self.max_health = 100
        self.health = 100
        self.max_mana = 60
        self.mana = 60
        self.strength = 12
        self.intelligence = 8
        self.agility = 18
        self.defense = 4

    def level_up(self):
        result = super().level_up()
        # Extra agility bonus for rogues
        self.agility += 2
        return result

    def attack(self, target):
        # Rogues use agility for stronger attacks
        damage = self.strength * 0.5 + self.agility * 0.7
        damage_dealt = target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")
        return damage_dealt
