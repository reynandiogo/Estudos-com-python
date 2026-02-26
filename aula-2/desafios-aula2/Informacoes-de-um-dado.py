dado = input('digite uma palavra: ')
print('seu dado é do tipo {}'.format(type(dado)))
print('agora para cada afirmação abaixo haverá ( false) para falso e (true) para verdadeiro')

print('seu dado possue apenas letras: {}'.format(dado.isalpha()))

print('seu dado apenas possue numeros: {}'.format(dado.isnumeric()))

print('e finalizamos aqui')