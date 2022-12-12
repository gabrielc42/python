#!/usr/bin/env python3

makeup = [
  ('líčidla', 'Czech'), 
  ('trang điểm', 'Vietnamese'),
  ('meik', 'Estonian'),
  ('isqurxin', 'Somali')
]

for (word, language) in makeup:
  print('The word makeup in {} is {}.'.format(language, word))