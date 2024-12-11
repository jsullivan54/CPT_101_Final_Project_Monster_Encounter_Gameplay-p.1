# Name: Johnathan Sullivan
# Date: 11/10/2024
# Project Title: The Final Project

# Program Description: The world of Eryndor Battle Game Part One Monster Encounter


#Import Random


import random

#define the main function
def main():
    # This main function handles the game  simulation
    print("Welcome to the Battle Royal Master Wayne_Jung: ")
    player_health, player_damage_range, player_dodge_chance = player_generator()
    monster_health = 70
    monster_damage_range = (4, 13)
    monster_dodge_chance = 0.15

    round_number = 0
    winner = None

    # Run the game until there is a winner
    while winner is None:
        round_number += 1
        print(f"\nRound {round_number} begins!")

        # Player attacks
        damage_to_monster = turn_damage(*player_damage_range)
        if dodge_check(monster_dodge_chance):
            damage_to_monster //= 2  # Monster dodges part of the attack
            print(f"Monster dodges! Takes reduced damage: {damage_to_monster}")
        monster_health -= damage_to_monster
        print(f"Monster receives {damage_to_monster} damage. Remaining HP: {monster_health}")

        # Check for winner after player's turn
        winner = check_for_winner(player_health, monster_health)
        if winner:
            continue

        # Monster's turn to attack
        if not dodge_check(player_dodge_chance):
            damage_to_player = turn_damage(*monster_damage_range)
            player_health -= damage_to_player
            print(f"Player is hit by Monster! Takes {damage_to_player} damage.")
        else:
            print("Player dodges the attack!")

        print(f"Player's HP: {player_health}, Monster's HP: {monster_health}")
        winner = check_for_winner(player_health, monster_health)

    if winner == "Player":
        print(f"\nCongratulations! You defeated the monster in {round_number} rounds!")
    else:
        print("\nYou were defeated by the monster.")

    print("\nThank you for playing!")

# Define player_generator(): per clients request
def player_generator():
    # Select a character class and return its attributes
    DODGE_INCREMENT = 2.5 / 100

    character_classes = {
        "Fighter": (80, (5, 10), 0.05 + (10 * DODGE_INCREMENT)),
        "Wizard": (50, (8, 15), 0.05 + (14 * DODGE_INCREMENT)),
        "Rogue": (65, (7, 12), 0.05 + (17 * DODGE_INCREMENT)),
        "Cleric": (70, (6, 11), 0.05 + (12 * DODGE_INCREMENT)),
        "Barbarian": (85, (4, 12), 0.05 + (7 * DODGE_INCREMENT))
    }

    print("Choose your character class:")
    class_names = list(character_classes.keys())
    for idx in range(len(class_names)):
        print(f"{idx + 1}. {class_names[idx]}")

    selected_class = None
    valid_selection = False
    while not valid_selection:
        choice = input("Enter the number of your chosen class: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(character_classes):
            selected_class = class_names[int(choice) - 1]
            valid_selection = True
        else:
            print("Invalid selection. Please choose a valid class number.")

    health, damage_range, dodge_chance = character_classes[selected_class]
    print(f"\nYou have chosen {selected_class}!")
    print(f"Health: {health}")
    print(f"Damage Range: {damage_range[0]}-{damage_range[1]}")
    print(f"Dodge Chance: {dodge_chance:.2%}")
    return health, damage_range, dodge_chance

# Define the function turn damage (x , y) per clients request
def turn_damage(x, y):
    return random.randint(x, y)

# Define the function doge_check(chance_doge) per clients request
def dodge_check(chance_dodge):
    return random.random() < chance_dodge

# Define the check_winner (player_health, monster_health): per clients request
def check_for_winner(player_health, monster_health):
    # Check for a winner
    if player_health <= 0:
        return "Monster"
    elif monster_health <= 0:
        return "Player"
    return None


if __name__ == "__main__":
    main()