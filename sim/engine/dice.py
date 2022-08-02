import random

def roll_d6(number, roll_number):
    results = []
    for n in range(0, number):
        result = []
        for m in range(0, roll_number):
            result.append(random.randint(1, 6))
        results.append(result)
    return results
