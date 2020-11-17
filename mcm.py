from functools import reduce

# 10 20 30 | 2
# 5  10 15 | 2
# 5  5  15 | 5
# 1  1  3  | 3
# 1  1  1

# 10 20 30 | 2
# 5  10 15 | 2
# 5  5  15 | 3
# 5  5  5  | 5
# 1  1  1

# 25 30 16 | 2
# 25 15  8 | 2
# 25 15  4 | 2
# 25 15  2 | 2
# 25 15  1 | 3
# 25  5  1 | 5
#  5  1  1 | 5
#  1  1  1 | 

def isDivisible(numbers, y):
    items = [x for x in numbers if x % y == 0]

    if len(items) == 0:
        # Ningun numero es divisible
        return False 
    # Hay numeros divisibles
    return True 

def calculate(x, y):
    if x % y == 0:
        return int(x / y)
    
    return x

def mcm(numbers):
    divisors = []
    maxNumber = max(numbers) + 1

    while True:
        for i in range(2, maxNumber):
            # validar si algun numero puede ser dividido por el valor de i
            if (isDivisible(numbers, i)):
                # 1. calcular nuevos valores de numbers, incrementar el valor de i y continuar
                numbers = list(map((lambda x: calculate(x, i)), numbers))
                # 2. agregar el valor de i a divisors
                divisors.append(i)
                break

        # validar si los numeros de array son iguales a 1

        if len([x for x in numbers if x == 1]) == len(numbers):
            break

    return reduce((lambda x, y: x * y), divisors)

#numbers = [25, 30, 16]
#numbers = [10, 20, 30]
numbers = [43, 39, 17]

print(mcm(numbers))