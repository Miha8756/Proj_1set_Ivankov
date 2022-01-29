print(open('text18-7.txt').read() + str(sum(map(str.islower, open('text18-7.txt').read()))))
print('\n'.join(open('text18-7.txt').read().splitlines()[:2]), '\n' + open('text18-7.txt').read().splitlines()[-1],
      '\n' + '\n'.join(open('text18-7.txt').read().splitlines()[2:6]), file=open('new-text18-7.txt', 'w'))
