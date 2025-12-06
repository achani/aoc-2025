with open('input.txt', 'r') as f: 
  rotations = f.read().splitlines()

position = 50
part1 = part2 = 0
for rotation in rotations: 
  total_clicks = int(rotation[1:])
  full_turns, clicks = divmod(total_clicks , 100)
  if rotation[0] == "L":
    if clicks > position > 0: # 0 crossing
      part2 += 1
    position -= clicks
  else: 
    if clicks > (100 - position): # 0 crossing
      part2 += 1
    position += clicks
  position = position % 100
  if position == 0:
    part1 += 1
    part2 += 1
  part2 += full_turns
print(f"Part 1: {part1}, Part 2: {part2}")