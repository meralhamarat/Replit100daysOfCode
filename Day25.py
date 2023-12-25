import random
print("\n--- Character Health Stats Generator ---")
def roll_dice(sides):
    return random.randint(1, sides)


def generate_health_stats():
    six_sided_dice = roll_dice(6)
    eight_sided_dice = roll_dice(8)
    health_stats = six_sided_dice * eight_sided_dice
    return health_stats


while True:
    character_name = input("Enter the character's name: ")

    health_stats = generate_health_stats()

    health = generate_health_stats()
    print("Their health is ", health_stats, "hp")

    play_again = input("\nDo you want to generate health stats for another character? (yes/no): ").lower()
    if play_again != 'yes':
        break