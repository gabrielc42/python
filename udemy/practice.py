# pigeon = 'pigeon'
# carrot = 'carrot'
# cobalt = 'cobalt'

# print("Here is an animal, a vegetable, and a mineral. \n{} \n{} \n{}".format(pigeon, carrot, cobalt))

# input = input("Please type something and press enter: ")
# print("You entered: \n", input)

# get input from user
text = input('What did the cat say?')

# determine length of input
text_length = len(text)

# make border same size as input
print('           {}'.format('_' * text_length))
print('         < {} >'.format(text))
print('           {}'.format('-' * text_length))
print('          /')
print('  /\_/\  /')
print(' ( o.o )')
print('  > ^ <')