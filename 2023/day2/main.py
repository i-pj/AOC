max_cubes = {"red": 12, "green": 13, "blue": 14}
result = [] # list of games that are possible

with open("input.txt") as f:
    for line in f:
        game_id, sets = line.split(": ")
        #print(game_id)
        #print(sets)
        game_id = int(game_id.split()[1])
        #print(game_id)
        possible = True
        for s in sets.split("; "):
            #print(s)
            for cube in s.split(", "):
                #print(cube)
                count, color = cube.split()
                if int(count) > max_cubes[color]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            result.append(game_id)

print(sum(result))
