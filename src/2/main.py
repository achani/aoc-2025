import math


def find_min(num):
  num = str(num)
  l = len(num)
  return 10 ** (l//2) if l%2 != 0 else int(num[0:math.ceil(l/2)]) 


def find_max(num):
  num = str(num)
  l = len(num)
  if l%2 != 0: 
    return int('9'* (l//2))
  first_half, second_half = int(num[0:l//2]) , int(num[l//2:])
  return first_half if second_half >= first_half else first_half - 1


with open("input.txt","r") as f:
  id_ranges = [(pair[0],pair[1]) for pair in [rng.split('-') for rng in f.read().split(',')]]


def sum_repeating_ids_in_range(start,end):
  ans = 0 
  for num in range(int(start), int(end)+1):
    id = str(num)
    l = len(id)
    for i in range(2,l+1):
      if l % i == 0 and id[0:l//i]*i == id:
          ans += int(id)
          break
  return ans


def solve_part1():
  ans = 0
  for rng in id_ranges:
    start, end = map(int, rng)
    if end < 10: continue
    min = start if start < 10 else find_min(start)
    max =  find_max(end)
    if max < min: 
      min, max = max, min
    for n in range(min, max + 1):
      invalid_id = n * 10**len(str(n)) + n
      if start <= invalid_id <= end:
        ans += invalid_id
  return ans


def solve_part2():
  ans = 0
  for rng in id_ranges:
    start, end = rng
    ans += sum_repeating_ids_in_range(start,end)
  return ans


print(solve_part1())
print(solve_part2())



