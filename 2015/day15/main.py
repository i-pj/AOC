import itertools

def parse_input(filename):
    with open(filename, 'r') as f:
        ingredients = {}
        for line in f:
            name, props = line.strip().split(': ')
            props = props.split(', ')
            ingredients[name] = {}
            for prop in props:
                key, value = prop.split(' ')
                ingredients[name][key] = int(value.split()[0])
        return ingredients

def calculate_score(ingredients, amounts):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for ingredient, amount in zip(ingredients.keys(), amounts):
        capacity += amount * ingredients[ingredient]['capacity']
        durability += amount * ingredients[ingredient]['durability']
        flavor += amount * ingredients[ingredient]['flavor']
        texture += amount * ingredients[ingredient]['texture']
        calories += amount * ingredients[ingredient]['calories']
    capacity = max(0, capacity)
    durability = max(0, durability)
    flavor = max(0, flavor)
    texture = max(0, texture)
    return capacity * durability * flavor * texture, calories

def main():
    ingredients = parse_input('input.txt')
    max_score_part1 = 0
    max_score_part2 = 0
    for amounts in itertools.product(range(101), repeat=len(ingredients)):
        if sum(amounts) == 100:
            score, calories = calculate_score(ingredients, amounts)
            if calories == 500:
                max_score_part2 = max(max_score_part2, score)
            max_score_part1 = max(max_score_part1, score)
    print("Part 1:", max_score_part1)
    print("Part 2:", max_score_part2)

if __name__ == '__main__':
    main()