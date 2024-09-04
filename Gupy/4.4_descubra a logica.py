num = int(input("Digite o número de elementos: "))
st = 2  
inc = 2 


cur = st
for i in range(num):
    print(cur ** 2)
    cur += inc
