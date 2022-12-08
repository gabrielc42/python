# prompt input
input = input('How far would you like to travel in miles? ')
distance = int(input)

if (distance < 3):
  print('You should walk to your destination.')

if (distance > 3 & distance < 300):
  print('You should drive to your location!')

if (distance > 300):
  print('You should fly to your destination!')

if (distance == 3 or distance == 300):
  print('Teleport')