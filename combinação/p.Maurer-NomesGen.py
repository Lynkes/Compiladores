###  pip install br-nome-gen

import time
import matplotlib.pyplot as plt
import numpy
from br_nome_gen import Pessoa, pessoa_random

Lista=[]
ListaLida=[]
#   pessoa.nome for pessoa in pessoas

def geranomes():
    for i in range(size):
        Lista.append(pessoa_random())
    # Open the file in append mode
    with open('names2.txt', 'a') as file:
    # Iterate over the names and write them to the file
        nomes = [Pessoa.nome for Pessoa in Lista]
        for Pessoa.nome in nomes:
            file.write(str(Pessoa.nome) + '\n')

def n_length_combo(lst, n):
     
    if n == 0:
        return [[]]
     
    l =[]
    for i in range(0, len(lst)):
        m = lst[i]
        remLst = lst[i + 1:]
         
        remainlst_combo = n_length_combo(remLst, n-1)
        for p in remainlst_combo:
             l.append([m, *p])
    return l

 
def n_length_comboV2(iterable, r):
    char = tuple(iterable)
    n = len(char)
     
    if r > n:
        return
     
    index = numpy.arange(r)
    yield tuple(char[i] for i in index)
     
    while True:
         
        for i in reversed(range(r)):
            if index[i] != i + n - r:
                break
        else:
            return
         
        index[i] += 1
         
        for j in range(i + 1, r):
             
            index[j] = index[j-1] + 1
             
        yield tuple(char[i] for i in index)


#############################################ARUMAR LEITURA##################################################################################
##### ARRUMAR QUICKSORT######
def read_txt():
    # Open the file in read mode
    with open('names2.txt', 'r') as file:
    # Read all lines from the file and append each line to the names list
        ListaLida = [line.strip() for line in file.readlines()]
        # Print the names list3
    #print('Test'+str(ListaLida))

if __name__ == "__main__":
    tempos=[]
    #size = input("NUMERO DE NOMES> ")
    size = 30
    geranomes()
    read_txt()
    ini = time.time()
    print(n_length_combo([x for x in ListaLida], 2))
    fim = time.time()
    tempos.append(fim-ini)
    print('SEGUNDO')
    ini1 = time.time()
    print([x for x in n_length_comboV2(ListaLida, 2)])
    fim1 = time.time()
    tempos.append(fim1-ini1)
    #print('Tamanhos 1=',len(n_length_combo),'2=',len(n_length_comboV2))
    print('Tempos',tempos)
    