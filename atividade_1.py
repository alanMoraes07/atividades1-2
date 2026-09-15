primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
item = 67
soma = 0

def pesquisa_binaria(primos, item):
  global soma
  baixo = 0
  alto = len(primos) - 1

  while baixo <= alto:
    soma += 1
    meio = (baixo + alto) // 2
    chute = primos[meio]
    if chute == item:
      return meio
    elif chute > item:
      alto = meio - 1
    else:
      baixo = meio + 1
  return None

resultado = pesquisa_binaria(primos, item)
print("Tentativas pesquisa binaria:", soma)
print("Numeros primos menores que '67':", resultado)