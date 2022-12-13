#!/usr/bin/env python3
def displayFacts(facts):
  for fact in facts:
    print('{}: {}'.format(fact, facts[fact]))
    print()
facts = {
 'Leopards': 'solitary animals',
 'Mars': 'atmosphere made of carbon dioxide, nitrogen, and argon',
 'Artemisia Gentileschi': 'painted Judith Slaying Holofernes',
 'Fyodor Dostoevsky': 'He was epileptic',
 'Python': 'programming language named after Monty Python'
}
  
displayFacts(facts)
facts['Minnesota'] = 'name comes from a Sioux word meaning "sky-tinted water'
facts['Maryam Mirzakhani'] = 'an Iranian mathematician and professor at Stanford, researched Teichmuller theory, hyperbolic geometry, ergodic theory, and symplectic geometry'
displayFacts(facts)