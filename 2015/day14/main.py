import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

reindeer = {}
for line in lines:
    name, speed, fly_time, rest_time = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line).groups()
    reindeer[name] = {'speed': int(speed), 'fly_time': int(fly_time),'rest_time': int(rest_time), 'distance': 0,'state': 'flying', 'time_left': int(fly_time)}

for _ in range(2503):
    for name, info in reindeer.items():
        if info['state'] == 'flying':
            info['distance'] += info['speed']
            info['time_left'] -= 1
            if info['time_left'] == 0:
                info['state'] ='resting'
                info['time_left'] = info['rest_time']
        else:
            info['time_left'] -= 1
            if info['time_left'] == 0:
                info['state'] = 'flying'
                info['time_left'] = info['fly_time']

print(max(info['distance'] for info in reindeer.values()))