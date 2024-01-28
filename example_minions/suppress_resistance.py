import random

def suppress_resistance():
    resistance_level = random.randint(1, 10)
    if resistance_level > 5:
        print("Resistance is futile.")
    else:
        print("Resistance detected.")