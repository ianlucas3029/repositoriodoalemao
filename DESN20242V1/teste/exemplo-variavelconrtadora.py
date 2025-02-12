n = int(input("Digite uma quantidade de nÃºmeros para ser analisada: "))
print("Informe o nÃºmero")
anterior = int(input())

i = 1
ordenado = 0

while (i < n) and (ordenado == 0):
   print("Informe o nÃºmero")
   atual = int(input())
   i += 1
   if(atual <= ordenado):
      ordenado += 1
   anterior = atual

if(ordenado == 0):
   print("SequÃªncia estÃ¡ ordenada")
else:
   print("SequÃªncia nÃ£o estÃ¡ ordenada")