frutas = ["maçã","tomate","laranja","abacaxi"]

frutas.append("pera")
print(frutas)

frutas.insert(1, "uva")
print(frutas)

frutas.remove("tomate")
print(frutas)

fruta_removida = frutas.pop(2)
print(frutas)
print(fruta_removida)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)