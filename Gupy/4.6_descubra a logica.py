num = int(input("Digite o número de elementos na sequência: "))
sequence = [2, 10, 12, 16, 17, 18, 19]  

if num <= len(sequence):
    
    print(" ".join(map(str, sequence[:num])))
else:
    last_number = sequence[-1]
    next_number = last_number + 1
    
    while True:
        is_prime = True
        if next_number < 2:
            is_prime = False
        else:
            for i in range(2, int(next_number**0.5) + 1):
                if next_number % i == 0:
                    is_prime = False
                    break
        if not is_prime:
            sequence.append(next_number)
            break
        next_number += 1
    