# Projeto: FizzBuzz (com reviravolta "Almost Fizz")
#
# Regras da função fizzbuzz(n):
# - divisível por 3 E por 7        -> "FizzBuzz"
# - divisível só por 3             -> "Fizz"
# - divisível só por 7             -> "Buzz"
# - contém o dígito "3" na escrita
#   (e não é divisível por 3/7)    -> "Almost Fizz"
# - nenhum dos casos acima         -> o próprio número como string
#
# O programa lê um número e imprime o resultado do FizzBuzz para
# cada número de 1 até esse número (inclusive).

print("Welcome to FizzBuzz!")

def FizzBuzz(n):
    if n % 3 == 0 and n % 7 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 7 == 0:
        return "Buzz"
    elif "3" in str(n):
        return "Almost Fizz"
    else:
        return str(n)

numero = int(input())

for i in range(1, numero + 1):
    print(FizzBuzz(i))
