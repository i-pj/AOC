with open("input.txt", "r") as file:
    workflows_str, parts_str = file.read().strip().split("\n\n")

# Parse workflows
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

# Parse parts
parts = []
for line in parts_str.split("\n"):
    part = {
        item.split("=")[0]: int(item.split("=")[1])
        for item in line.strip("{}").split(",")
    }
    parts.append(part)

# Process parts through workflows
total_rating = 0
for part in parts:
    current_workflow = "in"
    while current_workflow not in ("A", "R"):
        for category, operator, value, destination in workflows[current_workflow]:
            if category == "":
                current_workflow = destination
                break
            if operator == "<" and part[category] < value:
                current_workflow = destination
                break
            if operator == ">" and part[category] > value:
                current_workflow = destination
                break

    if current_workflow == "A":
        total_rating += sum(part.values())

# Print the result
print("The sum of ratings for accepted parts is:", total_rating)
