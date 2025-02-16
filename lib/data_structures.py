spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return[food["name"] for food in spicy_foods]
get_names(spicy_foods)


def get_spiciest_foods(spicy_foods):
    return[food for food in spicy_foods if food["heat_level"] > 5]
get_spiciest_foods(spicy_foods)


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_emoji = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")
print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
get_spicy_food_by_cuisine(spicy_foods, "American")


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            heat_emoji = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")
print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
     total_heat_level = sum(food["heat_level"] for food in spicy_foods)
     num_spicy_foods = len(spicy_foods)
     average = total_heat_level / num_spicy_foods
     return average
get_average_heat_level(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

new_food = {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10}

updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
print(updated_spicy_foods)
