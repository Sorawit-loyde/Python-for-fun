import random

def calculate_zeny(character_level, monster_level):    
    zeny_received = random.randint(int(minimum_zeny(character_level, monster_level)), int(maximum_zeny(character_level, monster_level)))
    
    return zeny_received

def total_zeny(character_level, monster_level, iterations=500):
    total = 0
    for _ in range(iterations):
        total += calculate_zeny(character_level, monster_level)
    return total

def minimum_zeny(character_level, monster_level):
    min_zeny = (character_level + (monster_level * 8)) / 4
    return min_zeny

def maximum_zeny(character_level, monster_level):
    max_zeny = (character_level + (monster_level * 16)) / 2
    return max_zeny

character_level = int(input("Enter your Character Level: "))
monster_level = int(input("Enter the Monster Level: "))
total_reward = total_zeny(character_level, monster_level)
min_reward = int(minimum_zeny(character_level, monster_level))*500
max_reward = int(maximum_zeny(character_level, monster_level))*500

print(f"\nMinimum Zeny received after 500 Boxes: {min_reward}")
print(f"\nMaximum Zeny received after 500 Boxes: {max_reward}")
print(f"\nRadom Zeny received after 500 Boxes: {total_reward}")