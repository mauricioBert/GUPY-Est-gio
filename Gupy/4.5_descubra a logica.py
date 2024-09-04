valor = int(input("Digite a sequência de Fibonacci: "))
forn = [0,1]
i=2
while i < valor:
    valorProx = forn[i-1]+forn[i-2]
    forn.append(valorProx)
    i=i+1
    
print(forn)