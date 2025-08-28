from character import Character


class Mage(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        # Mages have more mana and intelligence, less health and strength
        self.max_health = 80
        self.health = 80
        self.max_mana = 150
        self.mana = 150
        self.strength = 5
        self.intelligence = 20
        self.defense = 3

    def level_up(self):
        result = super().level_up()
        # Extra intelligence bonus for mages
        self.intelligence += 2
        self.max_mana += 15  # Extra mana for mages
        self.mana = self.max_mana
        return result

    def attack(self, target):
        # Mages use intelligence for basic attacks
        damage = self.intelligence * 0.4
        damage_dealt = target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")

        # Mages regain some mana on basic attacks
        mana_regen = 5
        self.mana = min(self.max_mana, self.mana + mana_regen)

        return damage_dealt
