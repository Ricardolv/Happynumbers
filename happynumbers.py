"""
Os números felizes são definidos pelo seguinte procedimento.
Começando com qualquer número inteiro positivo, o número é substituído pela soma dos quadrados dos seus dígitos,
e repetir o processo até que o número seja igual a 1 ou até que ele entre num ciclo infinito que não inclui um ou seja
a somo dos quadrados dos algarismos do quadrado de um número positivo inicial.
Os números no fim do processo de extremidade com 1, são conhecidos como números feliz,
mas aqueles que não terminam com um 1 são números chamados infelizes.


Exemplo:

7 é um número feliz:[3]

72 = 49
42 + 92 = 97
92 + 72 = 130
12 + 32 + 02 = 10
12 + 02 = 1.

Se n não é feliz, a soma dos quadrados nunca dará 1, serão gerados infinitos termos.

4, 16, 37, 58, 89, 145, 42, 20, 4, ...

"""

def happy(number):
    next_ = sum([int(char) ** 2 for char in str(number)])
    return number in (1, 7) if number < 10 else happy(next_)

assert all(happy(n) for n in (1, 10, 100, 130, 97))
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))
