class Character:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

        # Base stats - will be adjusted by subclasses
        self.max_health = 100
        self.health = 100
        self.max_mana = 50
        self.mana = 50
        self.strength = 10
        self.intelligence = 10
        self.agility = 10
        self.defense = 5

        self.abilities = []

    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        self.max_mana += 5
        self.mana = self.max_mana
        self.strength += 1
        self.intelligence += 1
        self.agility += 1
        self.defense += 1
        return f"{self.name} leveled up to level {self.level}!"

    def attack(self, target):
        damage = self.strength * 0.8
        damage_dealt = target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")
        return damage_dealt

    def take_damage(self, amount):
        effective_damage = max(1, amount - self.defense * 0.5)
        self.health = max(0, self.health - effective_damage)
        return effective_damage

    def is_alive(self):
        return self.health > 0

    def learn_ability(self, ability):
        self.abilities.append(ability)

    def use_ability(self, ability_index, target):
        if ability_index < 0 or ability_index >= len(self.abilities):
            return 0

        ability = self.abilities[ability_index]
        return ability.use(self, target)
