with open('input.txt') as f:
    q = f.read().strip()

platform = [list(x) for x in q.split('\n')]
platform.insert(0, ['#']*len(platform[0]))
for i in range(len(platform)):
    for j in range(len(platform[0])):
        if platform[i][j] == 'O':
            for k in range(i-1, -1, -1):
                if platform[k][j] == '#':
                    break
                elif platform[k][j] == '.':
                    platform[k][j] = 'O'
                    platform[k+1][j] = '.'
            else:
                platform[0][j] = '.'
print('Part 1:',sum([sum([1 for x in p if x == 'O'])*(i+1) for i,p in enumerate(platform[::-1])]))
