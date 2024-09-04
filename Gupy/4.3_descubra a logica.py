num = int(input("Digite o número de elementos: "))
cur = 0  
inc = 1

for i in range(num):
    print(cur)
    cur = inc ** 2
    inc += 1