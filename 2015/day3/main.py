with open('input.txt', 'r') as f:
    directions = f.read().strip()

def count_houses(directions):
    x, y = 0, 0  
    houses = {(x, y)}  

    for direction in directions:
        if direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        elif direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        houses.add((x, y))

    return len(houses) 

print(count_houses(directions))  


def count_houses(directions):
    santa_x, santa_y = 0, 0  
    robo_x, robo_y = 0, 0  
    houses = {(0, 0)}  

    for i, direction in enumerate(directions):
        if i % 2 == 0:  # Santa's turn
            if direction == '^':
                santa_y += 1
            elif direction == 'v':
                santa_y -= 1
            elif direction == '>':
                santa_x += 1
            elif direction == '<':
                santa_x -= 1
            houses.add((santa_x, santa_y))
        else:  # Robo-Santa's turn
            if direction == '^':
                robo_y += 1
            elif direction == 'v':
                robo_y -= 1
            elif direction == '>':
                robo_x += 1
            elif direction == '<':
                robo_x -= 1
            houses.add((robo_x, robo_y)) 

    return len(houses)

print(count_houses(directions))  