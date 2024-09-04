nome = input("Digite um nome: ")
ct = 0

for i in nome:
    if i.lower() == 'a':
        ct +=1
    elif i.upper()== 'a':
        ct +=1

if ct >0:
    print(f"A letra 'a' foi encontrada {ct} vezes")
else:
    print(f"A letra 'a' não foi encontrada")