#1/usr/bin/env python3

with open('file.txt') as file:
  line_number = 1
  for line in file:
    print('{}: {}'.format(line_number, line.rstrip()))
    line_number += 1

unsort_file_name = 'animals.txt'
sorted_file_name = 'animals-sorted.txt'
animals = []

try:
  with open(unsort_file_name) as animals_file:
    for line in animals_file:
      animals.append(line)
  animals.sort()
except:
  print('Could not open {}.'.format(unsort_file_name))
try:
  with open(sorted_file_name, 'w') as animals_sorted_file:
    for animal in animals:
      animals_sorted_file.write(animal)
  print(animals)
except:
  print('Could not open {}.'.format(sorted_file_name))