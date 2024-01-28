import random

opposition_leaders = ["John", "Jane", "Mike", "Sarah"]
neutralized_leaders = []

for leader in opposition_leaders:
    if random.random() < 0.5:
        neutralized_leaders.append(leader)

print("Neutralized leaders:", neutralized_leaders)