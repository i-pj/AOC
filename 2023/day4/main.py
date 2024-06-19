import re
# 
# with open("input.txt") as f:
#     lines = f.read().strip().split("\n")
# 
# cards = [list(map(int, re.findall(r"\d+", line))) for line in lines]
# wins = [len(set(card[11:]) & set(card[1:11])) for card in cards]
# 
# print(sum(2 ** (match_count - 1) for match_count in wins if match_count > 0))

from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

cards = [list(map(int, re.findall(r"\d+", line))) for line in lines]
wins = [len(set(card[11:]) & set(card[1:11])) for card in cards]

card_counts = defaultdict(int)
for i, win in enumerate(wins, 1):
    card_counts[i] += 1
    for j in range(i + 1, i + win + 1):
        card_counts[j] += card_counts[i]

print(sum(card_counts.values()))
