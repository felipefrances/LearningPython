#eleger um pivô para fazer comparações

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist, primeiro, ultimo):
   if primeiro < ultimo:

       splitpoint = partition(alist, primeiro, ultimo)

       quickSortHelper(alist, primeiro, splitpoint - 1)
       quickSortHelper(alist, splitpoint + 1, ultimo)


def partition(alist, primeiro, ultimo):
   pivo = alist[primeiro]

   esquerda = primeiro + 1
   direita = ultimo

   done = False
   while not done:

       while esquerda <= direita and alist[esquerda] <= pivo:
           esquerda = esquerda + 1

       while alist[direita] >= pivo and direita >= esquerda:
           direita = direita -1

       if direita < esquerda:
           done = True
       else:
           temp = alist[esquerda]
           alist[esquerda] = alist[direita]
           alist[direita] = temp

   temp = alist[primeiro]
   alist[primeiro] = alist[direita]
   alist[direita] = temp


   return direita

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
