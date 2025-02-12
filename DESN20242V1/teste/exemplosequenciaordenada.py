n = int(input("Digite uma quantidade de números para ser analisada: "))
print("Informe o número")
anterior = int(input())

i = 1 #Leu um número
ordenado = True #Ordenado é a variável indicadora

for i in range(n-1):
    print("informe o número: ")
    atual = int(input())
    if (atual < anterior):
        ordenado = False
        break
if (ordenado):
    print("Sequência ordenada.")
else:
    print("Sequência não ordenada")
