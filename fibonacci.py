def fib_linear(num):
    #verifica se é maior que 0
    if num < 0:
        return 'O número precisa ser maior ou igual a 0'
    seq_fib = [0,1]
    #vai adicionando até chegar no num
    for i in range(2, num+1):
        seq_fib.append(seq_fib[i-1] + seq_fib[i-2])
    return seq_fib[num]

def fib_recursivo(num):
    if num < 0:
        return 'O número precisa ser maior ou igual a 0'
    # Caso para fib(0) e fib(1)
    elif num <= 1:
        return num
    #recursão ate chegar no caso inicial
    else:
        return fib_recursivo(num-1) + fib_recursivo(num-2)

#exemplos
print(fib_linear(6))
print(fib_recursivo(1))