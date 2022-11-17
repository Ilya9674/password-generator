import itertools

for i in itertools.combinations_with_replacement('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM', 4):
    print(''.join(i))
