n = int(input("Digite uma quantidade de numero para ser analisado "))
print("Informe o número: ")
anterior = int(input())

i = 1 # leu um numero
ordenado = True #ordenado é a variavel indicadora

while (i < n) and (ordenado) :
    print ("Informe o numero: ")
    atual = int(input())
    i = i + 1 # leu mais um numero
    if (atual < anterior):
        ordenado = False 
    anterior = atual

if (ordenado):
    print("Sequencia ordenada.")
else:
    print("sequencia nao ordenada.")   
     
    