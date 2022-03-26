import itertools



string = input('Palavra a ser permutada: ')

#permuta as letras da palavra fornecida no input e as imprime


resultado= itertools.permutations(string,len(string) )


for i in resultado:
    print(''.join(i))