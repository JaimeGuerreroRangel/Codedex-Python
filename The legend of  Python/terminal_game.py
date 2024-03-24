import random

# Program: Wrestler Battles Simulator with Attack and Defense Options
# Description: This program simulates battles between wrestlers with varied attributes and types.
# Players choose a wrestler and battle against all other available wrestlers.
# The player wins if their wrestler survives all battles. Players can choose to attack or defend each turn.

# Definition of wrestlers with varied attributes and types
wrestlers = [
    {"name": "John Cena", "hp": random.randint(1, 100), "attack": random.randint(18, 22), "defense": random.randint(8, 12), "type": "Power"},
    {"name": "Triple HHH", "hp": random.randint(1, 100), "attack": random.randint(16, 20), "defense": random.randint(13, 17), "type": "Power"},
    {"name": "Shawn Michaels", "hp": random.randint(1, 100), "attack": random.randint(19, 23), "defense": random.randint(6, 10), "type": "Agility"},
    {"name": "CM Punk", "hp": random.randint(1, 100), "attack": random.randint(20, 24), "defense": random.randint(10, 14), "type": "Technique"},
    {"name": "Chris Jericho", "hp": random.randint(1, 100), "attack": random.randint(17, 21), "defense": random.randint(9, 13), "type": "Technique"},
]

# Player chooses a wrestler
print("Select your wrestler:")
for i, wrestler in enumerate(wrestlers, 1):
    print(f"{i}. {wrestler['name']} - HP: {wrestler['hp']}, Attack: {wrestler['attack']}, Defense: {wrestler['defense']}, Type: {wrestler['type']}")

try:
    selection = int(input("Write the number corresponding to your wrestler: "))
    player = wrestlers[selection - 1]
except (ValueError, IndexError):
    print("Invalid selection. Choose a number from the list.")
    exit()

# Battle mechanics including type advantage
type_advantages = {
    "Power": "Technique",
    "Technique": "Agility",
    "Agility": "Power"
}

# Battles
for i, opponent in enumerate(wrestlers):
    if opponent != player:
        print(f"Battle {i+1} against {opponent['name']}!")
        while player['hp'] > 0 and opponent['hp'] > 0:
            print(f"{player['name']} - HP: {player['hp']} vs. {opponent['name']} - HP: {opponent['hp']}")
            
            action = input("Choose action: 1 for attack, 2 for defense: ")
            
            is_defending = action == "2"
            if is_defending:
                print(f"{player['name']} is defending and will take half damage this turn.")
            
            # Calculate damage with type advantage
            damage = max(0, player['attack'] - opponent['defense'])
            if type_advantages[player['type']] == opponent['type']:
                print(f"Type advantage! {player['name']}'s attacks are more effective.")
                damage += 5 

            # Apply damage considering if defending or not
            if not is_defending:
                opponent['hp'] -= damage
                print(f"{player['name']} attacks {opponent['name']} and deals {damage} damage.")
            else:
                damage = max(0, damage // 2)  # Halve the damage if defending
                opponent['hp'] -= damage
                print(f"{player['name']} defends and reduces the damage to {damage}.")

            if opponent['hp'] <= 0:
                print(f"{opponent['name']} has been defeated.")
                break

            # Opponent's turn
            damage = max(0, opponent['attack'] - player['defense'])
            if not is_defending:
                player['hp'] -= damage
            else:
                damage = max(0, damage // 2)  # Halve the damage if defending
                player['hp'] -= damage
            print(f"{opponent['name']} attacks {player['name']} and deals {damage} damage.")

            if player['hp'] <= 0:
                print(f"{player['name']} has been defeated.")
                break

if player['hp'] > 0:
    print(f"Congratulations! {player['name']} survived all battles and emerged victorious!")
else:
    print(f"Game over! {player['name']} was defeated in battle.")