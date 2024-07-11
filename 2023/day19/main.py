from typing import Dict, List, Tuple


def parse_workflows(workflows_str: str) -> Dict[str, List[Tuple[str, str, int, str]]]:
    workflows = {}
    for line in workflows_str.split("\n"):
        name, rules_str = line.strip("}").split("{")
        rules = []
        for rule in rules_str.split(","):
            if ":" in rule:
                condition, destination = rule.split(":")
                category = condition[0]
                operator = condition[1]
                value = int(condition[2:])
                rules.append((category, operator, value, destination))
            else:
                rules.append(("", "", 0, rule))
        workflows[name] = rules
    return workflows


def count_accepted_combinations(
    workflows: Dict[str, List[Tuple[str, str, int, str]]],
    workflow: str,
    ranges: Dict[str, Tuple[int, int]],
) -> int:
    if workflow == "R":
        return 0
    if workflow == "A":
        product = 1
        for low, high in ranges.values():
            product *= high - low + 1
        return product

    total = 0
    for category, operator, value, destination in workflows[workflow]:
        if category == "":
            total += count_accepted_combinations(workflows, destination, ranges)
        else:
            low, high = ranges[category]
            if operator == "<":
                if low < value:
                    new_ranges = ranges.copy()
                    new_ranges[category] = (low, min(high, value - 1))
                    total += count_accepted_combinations(
                        workflows, destination, new_ranges
                    )
                ranges[category] = (max(low, value), high)
            elif operator == ">":
                if high > value:
                    new_ranges = ranges.copy()
                    new_ranges[category] = (max(low, value + 1), high)
                    total += count_accepted_combinations(
                        workflows, destination, new_ranges
                    )
                ranges[category] = (low, min(high, value))

    return total


# Read and parse the input file
with open("input.txt", "r") as file:
    workflows_str, _ = file.read().strip().split("\n\n")

workflows = parse_workflows(workflows_str)

# Initialize ranges for each category
initial_ranges = {category: (1, 4000) for category in "xmas"}

# Count the number of accepted combinations
total_accepted = count_accepted_combinations(workflows, "in", initial_ranges)

print(
    "The number of distinct combinations of ratings that will be accepted is:",
    total_accepted,
)
