#!/usr/bin/env python3

def get_word(word_type):
  """Return a word input"""

  # lower() function converts string to lowercase
  if word_type.lower() == 'adjective':
    # use 'an' or 'a' in front of 'adjective'
    a_or_an = 'an'
  else:
    a_or_an = 'a'
  return input('Enter a word that is {0} {1}: '.format(a_or_an, word_type))

def fill_in_blanks(noun, verb, adj):
  """fills in blanks and returns story"""

  story = "In this course you will learn how to {1}. " \
          "{0}. " \
          " Trust me, it will be very {2}.".format(noun, verb, adj)
  return story

def display_story(story):
    """displays story"""
    print()
    print('a story...')
    print()
    print(story)

def create_story():
  """Creates a story via input and displaying finished story."""
  noun = get_word('noun')
  verb = get_word('verb')
  adj = get_word('adjective')

  the_story = fill_in_blanks(noun, verb, adj)
  display_story(the_story)

create_story()