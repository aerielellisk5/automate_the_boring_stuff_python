
import pprint

message = 'It was a bright cold day in April, and the clocks were striking theirteen.'

count = {} # 'r':12

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
pprint.pprint(count)