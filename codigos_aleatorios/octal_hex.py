# Números octais e hexadecimais

# Há duas convenções adicionais em Python que são desconhecidas para o mundo da matemática. 
# A primeira nos permite usar números em uma representação octal.

# Se um número inteiro for precedido por um prefixo 0O ou 0o (zero-o), 
# ele será tratado como um valor octal. Isso significa que o número deve conter 
# dígitos retirados apenas do intervalo [0..7].

# 0o123 é um número octal com um valor (decimal) igual a 83.

# A função print() faz a conversão automaticamente. Tente isto:

print(0o123)

# A segunda convenção nos permite usar números hexadecimais. 
# Esses números devem ser precedidos pelo prefixo 0x ou 0X (zero-x).

# 0x123 é um número hexadecimal com um valor (decimal) igual a 291. 
# A função print() também pode gerenciar esses valores. Tente isto:

print(0x123)

print(3e2)