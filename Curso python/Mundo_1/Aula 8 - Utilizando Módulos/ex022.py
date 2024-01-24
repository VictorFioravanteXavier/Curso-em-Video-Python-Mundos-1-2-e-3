nome = str(input('digite seu nome completo: ')).title()
dividido = nome.split()
junto = ''.join(dividido)
print(f'''Nome: {nome}
Seu nome com todas as letras maiúsculas: {nome.upper()};
Seu nome com todas as letras minúsculas: {nome.lower()};
Seu nome tem {len(junto)} letras;
Seu primeiro nome é {dividido[0]} e tem {len(dividido[0])} letras.
''')
