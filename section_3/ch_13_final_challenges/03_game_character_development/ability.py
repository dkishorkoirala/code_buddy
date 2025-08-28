class Ability:
    def __init__(self, name, mana_cost, damage):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage

    def use(self, character, target):
        if character.mana < self.mana_cost:
            print(f"{character.name} doesn't have enough mana to use {self.name}")
            return 0

        character.mana -= self.mana_cost

        # Calculate damage
        if hasattr(character, "intelligence"):
            # Scale with intelligence for magical abilities
            damage = self.damage + (character.intelligence * 0.5)
        else:
            damage = self.damage

        damage_dealt = target.take_damage(damage)
        print(
            f"{character.name} used {self.name} on {target.name} for {damage_dealt:.1f} damage!"
        )

        return damage_dealt
