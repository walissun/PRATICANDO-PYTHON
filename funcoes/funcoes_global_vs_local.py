def funcao():
    variavel_local = 10
    print(variavel_local)  # Deve imprimir 10

variavel_global = 20

def funcao2():
    print(variavel_global)  # Deve imprimir 20

funcao()                   # Imprime 10
funcao2()                  # Imprime 20
print(variavel_global)     # Imprime 20
print(variavel_local) # Gera um erro, a variável não está definida neste escopo.