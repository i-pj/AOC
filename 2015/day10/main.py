def look_and_say(seq):
    result = []
    i = 0
    while i < len(seq):
        count = 1
        while i + 1 < len(seq) and seq[i] == seq[i+1]:
            i += 1
            count += 1
        result.append(str(count) + seq[i])
        i += 1
    return ''.join(result)

seq = '1113122113'
for _ in range(40):
    seq = look_and_say(seq)

print(len(seq))