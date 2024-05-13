def primo_recursivo(num, i=2):
    if num < 2:
        return 'O número precisa ser maior que 1'
    if num <= 2:
        return [num]
    elif num == i:
        return primo_recursivo(num-1) + [num]
    elif num % i == 0:
        return primo_recursivo(num-1)
    else:
        return primo_recursivo(num, i + 1)
    
def primo_linear(num):
    if num < 2:
        return 'O número precisa ser maior que 1'
    lista_primos = []
    for num in range(2, num+1):
        primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                primo = False
                break
        if primo:
            lista_primos.append(num)
    return lista_primos

print(primo_recursivo(20))
print(primo_linear(20))
    